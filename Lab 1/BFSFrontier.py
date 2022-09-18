from search import *
from collections import deque

class DFSFrontier(Frontier):
    """Implements a frontier container appropriate for depth-first
    search."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty stack."""
        self.container = []

    def add(self, path):
        self.container.append(path)

    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional state for iteration."""
        return self
        
    def __next__(self):
        if len(self.container) > 0:
            return self.container.pop()
        else:
            raise StopIteration   # don't change this one

class BFSFrontier(DFSFrontier):
    """Implements a frontier container appropriate for breadth-first
    search."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty deque."""
        self.container = deque()
  
    def __next__(self):
        """Selects, removes, and returns a path on the frontier if there is
        any. If there nothing to return this should raise a
        StopIteration exception.
        """
        if len(self.container) > 0:
            return self.container.popleft()
        else:
            raise StopIteration


print("-----------------------------")
graph = ExplicitGraph(nodes=set('SAG'),
                      edge_list = [('S','A'), ('S', 'G'), ('A', 'G')],
                      starting_nodes = ['S'],
                      goal_nodes = {'G'})

solutions = generic_search(graph, BFSFrontier())
solution = next(solutions, None)
print_actions(solution)
print("-----------------------------")
flights = ExplicitGraph(nodes=['Christchurch', 'Auckland', 
                               'Wellington', 'Gold Coast'],
                        edge_list = [('Christchurch', 'Gold Coast'),
                                 ('Christchurch','Auckland'),
                                 ('Christchurch','Wellington'),
                                 ('Wellington', 'Gold Coast'),
                                 ('Wellington', 'Auckland'),
                                 ('Auckland', 'Gold Coast')],
                        starting_nodes = ['Christchurch'],
                        goal_nodes = {'Gold Coast'})

my_itinerary = next(generic_search(flights, BFSFrontier()), None)
print_actions(my_itinerary)