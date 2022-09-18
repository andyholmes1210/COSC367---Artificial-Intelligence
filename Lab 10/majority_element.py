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
        
        
print(majority_element([0, 0, 0, 0, 0, 1, 1, 1]))
print(majority_element("ababc") in "ab")