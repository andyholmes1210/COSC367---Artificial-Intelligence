import csv

def learn_prior(file_name, pseudo_count=0):
    result = 0
    with open(file_name) as in_file:
        training_examples = [tuple(row) for row in csv.reader(in_file)] 
        
        rows = len(training_examples)
        for i in range(1, rows):
            if int(training_examples[i][-1]) == 1:
                result += 1 
        
        
    return (result + pseudo_count) / ((rows - 1) + (pseudo_count * 2))




prior = learn_prior("spam-labelled.csv", pseudo_count = 10)
print(format(prior, ".5f"))