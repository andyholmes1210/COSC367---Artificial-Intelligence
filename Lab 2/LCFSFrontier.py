from search import *
from math import *

class LocationGraph(ExplicitGraph):
    def __init__(self, nodes, locations, edges, starting_nodes, goal_nodes):
        self.nodes = nodes
        self.locations = locations
        self.edges = edges
        self.start = starting_nodes
        self.goal = goal_nodes
        
    def starting_nodes(self):
        """Returns a sequence of starting nodes."""
        return self.start

    def is_goal(self, node):
        """Returns true if the given node is a goal node."""
        return node in self.goal 
        
    def outgoing_arcs(self, node):
        result = []
        for node_edge in self.edges:
            if len(node_edge) == 2:  
                tail_node, head_node = node_edge
                cost_of_arc = self.arcs_cost(node_edge)  
            else:
                tail_node, head_node, cost_of_arc = node_edge
            if head_node == node:
                arcs = Arc(head_node, tail_node, str(head_node) + '->' + str(tail_node), cost_of_arc)
                if arcs not in result:
                    result.append(arcs)       
            if tail_node == node:
                arcs = Arc(tail_node, head_node, str(tail_node) + '->' + str(head_node), cost_of_arc)
                if arcs not in result:
                    result.append(arcs)   
        return sorted(result)
    
    def arcs_cost(self, points):
        i, j = points
        point1_i = self.locations[i][0]
        point1_j = self.locations[i][1]
        point2_j = self.locations[j][0]
        point2_i = self.locations[j][1]  
        return sqrt((point2_j - point1_i)**2 + (point2_i - point1_j)**2)


class LCFSFrontier(Frontier):
    def __init__(self):
        self.container = []

    def add(self, path):
        self.container.append(path)

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.container) > 0:
            if len(self.container) != 1:
                self.container.sort(key=lambda x: sum(i.cost for i in x))
                return self.container.pop(0)
            else:
                return self.container.pop(0)
        else:
            raise StopIteration 



graph = LocationGraph(nodes=set('ABC'),
                      locations={'A': (),
                                 'C': (3,0, 0),
                                 'B': (3, 0 4)},
                      edges={('A', 'B'), ('B','C'),
                             ('B', 'A')},
                      starting_nodes=['A'],
                      goal_nodes={'C'})

solution = next(generic_search(graph, LCFSFrontier()))
print_actions(solution)