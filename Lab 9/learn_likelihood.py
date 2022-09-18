import csv

def learn_likelihood(file_name, pseudo_count=0):
    with open(file_name) as in_file:
        training_examples = [tuple(row) for row in csv.reader(in_file)] 
    training_examples = training_examples[1:]
    

    likelihood = [[0,0] for i in range((len(training_examples[0]) - 1))]
    
    for i in range(len(likelihood)):
        for obs in training_examples:
            if (obs[i], obs[-1]) == ("1", "1"):
                likelihood[i][1] += 1
            elif (obs[i], obs[-1]) == ("1", "0"):
                likelihood[i][0] += 1
                
                
    for n in likelihood:
        n[0] = (n[0] + pseudo_count)/ ((len(training_examples) - 51) + pseudo_count*2)
        n[1] = (n[1] + pseudo_count)/ (51 + (pseudo_count*2))
        n = tuple(n)
    return tuple(likelihood)



likelihood = learn_likelihood("spam-labelled.csv")

print("P(X1=True | Spam=False) = {:.5f}".format(likelihood[0][False]))
print("P(X1=False| Spam=False) = {:.5f}".format(1 - likelihood[0][False]))
print("P(X1=True | Spam=True ) = {:.5f}".format(likelihood[0][True]))
print("P(X1=False| Spam=True ) = {:.5f}".format(1 - likelihood[0][True]))