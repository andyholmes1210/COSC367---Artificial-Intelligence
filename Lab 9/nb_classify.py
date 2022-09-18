import csv

def nb_classify(prior, likelihood, input_vector):
    compare = posterior(prior, likelihood, input_vector)
    if compare > 0.5:
        return ("Spam", compare)
    else:
        return ("Not Spam", 1 - compare)
        
    



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


def learn_prior(file_name, pseudo_count=0):
    result = 0
    with open(file_name) as in_file:
        training_examples = [tuple(row) for row in csv.reader(in_file)] 
        
        rows = len(training_examples)
        for i in range(1, rows):
            if int(training_examples[i][-1]) == 1:
                result += 1 
        
        
    return (result + pseudo_count) / ((rows - 1) + (pseudo_count * 2))



def posterior(prior, likelihood, observation):
    pTrue = prior
    pFalse = 1 - prior
    for i, result in enumerate(observation):
        if result == True:
            pTrue *= likelihood[i][1]
            pFalse *= likelihood[i][0]
        else:
            pTrue *= (1 - likelihood[i][1])
            pFalse *= (1 - likelihood[i][0])
            
    return pTrue / (pTrue + pFalse)


prior = learn_prior("spam-labelled.csv")
likelihood = learn_likelihood("spam-labelled.csv")

input_vectors = [
    (1,1,0,0,1,1,0,0,0,0,0,0),
    (0,0,1,1,0,0,1,1,1,0,0,1),
    (1,1,1,1,1,0,1,0,0,0,1,1),
    (1,1,1,1,1,0,1,0,0,1,0,1),
    (0,1,0,0,0,0,1,0,1,0,0,0),
    ]

predictions = [nb_classify(prior, likelihood, vector)
               for vector in input_vectors]

for label, certainty in predictions:
    print("Prediction: {}, Certainty: {:.5f}"
          .format(label, certainty))