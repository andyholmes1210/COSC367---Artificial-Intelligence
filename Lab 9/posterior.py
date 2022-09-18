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
        


prior = 0.05
likelihood = ((0.001, 0.3),(0.05,0.9),(0.7,0.99))

observation = (True, True, True)

class_posterior_true = posterior(prior, likelihood, observation)
print("P(C=False|observation) is approximately {:.5f}"
      .format(1 - class_posterior_true))
print("P(C=True |observation) is approximately {:.5f}"
      .format(class_posterior_true))

