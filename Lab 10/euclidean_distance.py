
def euclidean_distance(v1, v2):
    return sum([(v1[i]-v2[i])**2 for i in range(len(v1))])**(1/2)
    

print(euclidean_distance([0, 3, 1, -3, 4.5],[-2.1, 1, 8, 1, 1]))