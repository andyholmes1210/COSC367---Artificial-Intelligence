import math

def max_value(tree):
    result = -math.inf
    if isinstance(tree, int):
        return tree
    else:
        for i in tree:
            result = max(result, min_value(i))
    return result
    
    
def min_value(tree):
    result = math.inf
    if isinstance(tree, int):
        return tree
    else:
        for i in tree:
            result = min(result, max_value(i))
    return result
        

def max_action_value(game_tree):
    result = []
    if isinstance(game_tree, int):
        return(None, game_tree)
    else:
        for i, j in enumerate(game_tree):
            result.append((i, min_value(j)))
            
    return max(result, key=lambda x: x[1])
        
            
    
def min_action_value(game_tree):
    result = []
    if isinstance(game_tree, int):
        return(None, game_tree)
    else:
        for i, j in enumerate(game_tree):
            result.append((i, max_value(j)))
    return min(result, key=lambda x: x[1])
            


game_tree = [2, [-3, 1], 4, 1]

action, value = min_action_value(game_tree)
print("Best action if playing min:", action)
print("Best guaranteed utility:", value)
print()
action, value = max_action_value(game_tree)
print("Best action if playing max:", action)
print("Best guaranteed utility:", value)