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

weights = [2, -4]
bias = 0
perceptron = construct_perceptron(weights, bias)

print(perceptron([1, 1]))
print(perceptron([2, 1]))
print(perceptron([3, 1]))
print(perceptron([-1, -1]))