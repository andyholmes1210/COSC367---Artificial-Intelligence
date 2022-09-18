
def euclidean_distance(v1, v2):
    return sum([(v1[i]-v2[i])**2 for i in range(len(v1))])**(1/2)
    
    
def majority_element(labels):
    result = {}
    for i in labels:
        try:
            result[i] += 1
        except KeyError:
            result[i] = 1
    for key, value in result.items():
        if value == max(result.values()):
            return key
        


def knn_predict(input, examples, distance, combine, k):
    new_dis, new_list, operator_list = [], [], []
    for i in examples:
        distance_eu = distance(input, i[0])
        new_dis.append((distance_eu, i[1]))
        
    sorted_new_dis = sorted(new_dis) 
    
    k_list = sorted_new_dis[:k]
    length_list = sorted_new_dis[k:]

    for i, value in enumerate(length_list):
        if k_list[-1][0] == length_list[i][0]:
            k_list.append(value)
        else:
            break

    for i in range(len(k_list)):
        operator_list.append(k_list[i][1])
        
    return combine(operator_list)
 
    
examples = [
    ([2], '-'),
    ([3], '-'),
    ([5], '+'),
    ([8], '+'),
    ([9], '+'),
]

distance = euclidean_distance
combine = majority_element

for k in range(1, 6, 2):
    print("k =", k)
    print("x", "prediction")
    for x in range(0,10):
        print(x, knn_predict([x], examples, distance, combine, k))
    print()