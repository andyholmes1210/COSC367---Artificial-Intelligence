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




def cost(x):
    return x**2

def neighbours(x):
    return [x - 1, x + 1]

for state in greedy_descent(4, neighbours, cost):
    print(state)



def cost(x):
    return x**2

def neighbours(x):
    return [x - 1, x + 1]

for state in greedy_descent(-6.75, neighbours, cost):
    print(state)