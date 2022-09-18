from itertools import combinations

def n_queens_neighbours(state):
    neighbours = []
    for i , j in combinations(range(len(state)), 2):
        neighbour = list(state)
        neighbour[i], neighbour[j] =  state[j], state[i]
        neighbours.append(tuple(neighbour))
    return sorted(neighbours)




print(n_queens_neighbours((1, 2)))


for neighbour in n_queens_neighbours((1, 2, 3, 4, 5, 6, 7, 8)):
    print(neighbour)


print(n_queens_neighbours((1, 2, 3)))