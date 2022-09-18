def construct_perceptron(weights, bias):
    """Returns a perceptron function using the given paramers."""
    def perceptron(input):
        sum_vec = 0
        for i, k in enumerate(input):
            sum_vec += weights[i] * k
            
        a = sum_vec + bias
        
        if a >= 0:
            return 1
        else:
            return 0
    
    return perceptron # this line is fine


def accuracy(classifier, inputs, expected_outputs):
    output = []
    for i in inputs:
        output.append(classifier(i))
        
    result = 0
    for i in range(len(output)):
        if output[i] == expected_outputs[i]:
            result += 1
            
    return result/len(inputs)



perceptron = construct_perceptron([-1, 3], 2)
inputs = [[1, -1], [2, 1], [3, 1], [-1, -1]]
targets = [0, 1, 1, 0]

print(accuracy(perceptron, inputs, targets))