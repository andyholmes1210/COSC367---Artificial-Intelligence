from search import *
import heapq
import re 
import math

class RoutingGraph(Graph):
    
    def __init__(self, mapstring):
        resultMatrix = []
        matrixElement = []       
        self.mapstring = mapstring
        for i in self.mapstring:
            if i != "\n":
                matrixElement.append(i)
            else:
                resultMatrix.append(matrixElement)
                matrixElement = []
        self.mapstring = resultMatrix
        
        self.goal_nodes = []
        for row, line in enumerate(self.mapstring):
            indices = [i for i, j in enumerate(line) if j == 'G']
            for col in indices:
                self.goal_nodes.append((row, col))
        
        self.rowlimit = len(self.mapstring) - 1
        self.collimit = len(self.mapstring[0]) - 1   
        
    def is_goal(self, node):
        row, column, fuel = node
        return self.mapstring[row][column] == "G"
        
    def starting_nodes(self):
        start_node = []
        for i, row in enumerate(self.mapstring):
            for j, col in enumerate(row):
                finding_num = re.search('[0-9]', col)
                if col == "S":
                    start_node.append((i, j, math.inf))
                if finding_num:
                    start_node.append((i, j, int(finding_num.group()))) 
        return start_node
    
    def outgoing_arcs(self, tail_node):
        arcs = []
        arc_list = [('N' , -1, 0),
                    ('E' ,  0, 1),
                    ('S' ,  1, 0),
                    ('W' ,  0, -1)]
        
        boundries = ["X", "|", "-", "+"]
        
        row, column, fuel = tail_node  
        for i, j, k in arc_list:
            newrow = row + j 
            newcol = column + k
            if 0 < newrow < self.rowlimit and 0 < newcol < self.collimit:
                if fuel > 0:
                    if self.mapstring[newrow][newcol] not in boundries:
                        new_position = (newrow, newcol, fuel - 1)
                        arcs.append(Arc(tail_node, new_position, i, 5))
        if self.mapstring[row][column] == "F" and fuel < 9:
            arcs.append(Arc(tail_node, (row, column, 9), 'Fuel up', 15))
        return arcs
        
    def estimated_cost_to_goal(self, node):
        row, column, fuel = node
        node_cost = []
        for nodes in self.goal_nodes:
            goalrow, goalcol = nodes
            cost = abs(row - goalrow) + abs(column - goalcol)
            node_cost.append(cost)
        return min(node_cost) * 5 
            
        
class AStarFrontier(Frontier):
    def __init__(self, graph):
        self.graph = graph
        self.container = []
        self.node_pruning = set()
        self.priority = 0
        
    def add(self, path):
        node_cost = 0
        for tail, head, action, cost in path:
            node_cost += cost
        node_cost += self.graph.estimated_cost_to_goal(path[-1].head)
        if path not in self.container:
            self.container.append((node_cost, self.priority, path))
            self.priority += 1
            heapq.heapify(self.container)
            
    def __next__(self):
        while len(self.container) != 0:
            path = heapq.heappop(self.container)[2]
            if path[-1].head not in self.node_pruning:
                self.node_pruning.add(path[-1].head)
                return path
        else:
            raise StopIteration
           
        
   
def print_map(graph, frontier, solution):
    """Prints the map graph and the search paths taken"""
    map_solutions = ""
    map_string = graph.mapstring
    for i, node in enumerate(frontier.node_pruning):
        row, column, fuel = node
        if  map_string[row][column] == " ":
            map_string[row][column] = "."
            
    if solution:
        for i, j in enumerate(solution):
            row, column, fuel = j.head
            if i == 0:
                map_string[row][column] = "S"
            if map_string[row][column] not in ["S", "G"]:
                map_string[row][column] = "*"
        
        map_string[row][column] = "G" 

    for line in map_string:
        result=''.join([str(mapping) for mapping in line])
        print(result)


map_str = """\
+----------------+
|                |
|                |
|                |
|                |
|                |
|                |
|        S       |
|                |
|                |
|     G          |
|                |
|                |
|                |
+----------------+
"""


map_graph = RoutingGraph(map_str)
# changing the heuristic so the search behaves like LCFS
map_graph.estimated_cost_to_goal = lambda node: 0

frontier = AStarFrontier(map_graph)

solution = next(generic_search(map_graph, frontier), None)
print_map(map_graph, frontier, solution)