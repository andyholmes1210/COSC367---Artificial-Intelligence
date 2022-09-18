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



def learn_perceptron_parameters(weights, bias, training_examples, learning_rate, max_epochs):
    perceptron = construct_perceptron(weights, bias)
    epochs = 0
    while epochs <= max_epochs:
        for x, t in training_examples:
            y = perceptron(x)
            if t != y:
                weights = [(weights[i] + learning_rate * x[i] * (t - y)) for i in range(len(x))]
                bias += learning_rate * (t - y)
                perceptron = construct_perceptron(weights, bias)
        epochs += 1
    return (weights, bias)
        

weights = [2, -4]
bias = 0
learning_rate = 0.5
examples = [
  ((0, 0), 0),
  ((0, 1), 0),
  ((1, 0), 0),
  ((1, 1), 1),
  ]
max_epochs = 50

weights, bias = learn_perceptron_parameters(weights, bias, examples, learning_rate, max_epochs)
print(f"Weights: {weights}")
print(f"Bias: {bias}\n")

perceptron = construct_perceptron(weights, bias)

print(perceptron((0,0)))
print(perceptron((0,1)))
print(perceptron((1,0)))
print(perceptron((1,1)))
print(perceptron((2,2)))
print(perceptron((-3,-3)))
print(perceptron((3,-1)))