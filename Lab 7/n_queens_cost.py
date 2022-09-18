from itertools import combinations

def n_queens_cost(state):
    num_conflict = 0
    for pairs in list(combinations(state, 2)):
        i, j = pairs[0], pairs[1]
        x, y = state.index(i), state.index(j)
        if abs(i - j) == abs(x - y):
            num_conflict += 1
    return num_conflict
        


    
print(n_queens_cost((1, 2)))


print(n_queens_cost((1, 2, 3, 4, 5, 6, 7, 8)))


print(n_queens_cost((1,)))