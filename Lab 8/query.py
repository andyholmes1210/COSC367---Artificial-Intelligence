from itertools import *

def joint_prob(network, assignment):
    
    p = 1 
    for i, j in assignment.items():
        if len(network[i]['Parents']) == 0:
            if j:
                p *= network[i]['CPT'][()]
            else:
                p *= 1 - network[i]['CPT'][()]
        else:
            parent = network[i]['Parents']
            node_list = []
            for k in range(len(parent)):
                node_list.append(assignment[parent[k]])
            if j:
                p *= network[i]['CPT'][tuple(node_list)]
            else:
                p *= 1 - network[i]['CPT'][tuple(node_list)]
    return p



def query(network, query_var, evidence):
    
    # If you wish you can follow this template
    
    # Find the hidden variables
    hidden_vars = network.keys() - evidence.keys() - {query_var}
    result = 0
    # Initialise a raw distribution to [0, 0]
    assignment = dict(evidence) # create a partial assignment
    for query_value in {True, False}:
        i = 0
        for values in product((True, False), repeat=len(hidden_vars)):
            hidden_assignments = {var:val for var,val in zip(hidden_vars, values)}
            hidden_assignments.update({query_var: query_value})
            hidden_assignments.update(evidence)
            i += joint_prob(network, hidden_assignments)
        assignment[query_value] = i

    for j, k in enumerate(assignment.values()):
        if k == True:
            continue
        else:
            result += k

    for a, b in assignment.items():
        assignment[a] = b/result
    return assignment



network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.2
            }},
}

answer = query(network, 'A', {})
print("P(A=true) = {:.5f}".format(answer[True]))
print("P(A=false) = {:.5f}".format(answer[False]))


network = {
    'Burglary': {
        'Parents': [],
        'CPT': {
            (): 0.001
            }},

    'Earthquake': {
        'Parents': [],
        'CPT': {
            (): 0.002,
            }},
    'Alarm': {
        'Parents': ['Burglary','Earthquake'],
        'CPT': {
            (True,True): 0.95,
            (True,False): 0.94,
            (False,True): 0.29,
            (False,False): 0.001,
            }},

    'John': {
        'Parents': ['Alarm'],
        'CPT': {
            (True,): 0.9,
            (False,): 0.05,
            }},

    'Mary': {
        'Parents': ['Alarm'],
        'CPT': {
            (True,): 0.7,
            (False,): 0.01,
            }},
    }

answer = query(network, 'Burglary', {'John': True, 'Mary': True})
print("Probability of a burglary when both\n"
      "John and Mary have called: {:.3f}".format(answer[True]))