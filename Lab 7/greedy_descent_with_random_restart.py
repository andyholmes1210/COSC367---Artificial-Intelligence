from itertools import combinations
import random

def n_queens_cost(state):
    num_conflict = 0
    for pairs in list(combinations(state, 2)):
        i, j = pairs[0], pairs[1]
        x, y = state.index(i), state.index(j)
        if abs(i - j) == abs(x - y):
            num_conflict += 1
    return num_conflict



def n_queens_neighbours(state):
    neighbours = []
    for i , j in combinations(range(len(state)), 2):
        neighbour = list(state)
        neighbour[i], neighbour[j] =  state[j], state[i]
        neighbours.append(tuple(neighbour))
    return sorted(neighbours)



def greedy_descent(initial_state, neighbours, cost):
    current = initial_state
    states = []
    current_cost = cost(current)
    result = True
    while result:
        states.append(current)
        neighbour_list = neighbours(current)
        if len(neighbour_list) < 1:
            result = False
        else:
            cost_states = [cost(i) for i in neighbour_list]
            smallest_cost = min(cost_states)
            if smallest_cost < current_cost:
                current = neighbour_list[cost_states.index(smallest_cost)]
                current_cost = smallest_cost
            else:
                result = False
    return states


def greedy_descent_with_random_restart(random_state, neighbours, cost):
    current = random_state()

    result = True
    while result:
        states = greedy_descent(current, neighbours, cost)
        for i in states:
            print(i)
        if cost(states[-1]) > 0:
            print("RESTART")
            current= random_state()
        else:
            result = False
        


import random

N = 6
random.seed(0)

def random_state():
    return tuple(random.sample(range(1,N+1), N))

greedy_descent_with_random_restart(random_state, n_queens_neighbours, n_queens_cost)
        
    