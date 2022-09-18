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



network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.2
            }},
}

p = joint_prob(network, {'A': True})
print("{:.5f}".format(p))



network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.1
            }},

    'B': {
        'Parents': ['A'],
        'CPT': {
            (True,): 0.8,
            (False,): 0.7,
            }},
    }

p = joint_prob(network, {'A': False, 'B':True})
print("{:.5f}".format(p))