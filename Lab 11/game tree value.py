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
        



game_tree = [1, 2, 3]

print("Root utility for minimiser:", min_value(game_tree))
print("Root utility for maximiser:", max_value(game_tree))


game_tree = [1, 2, [3]]

print(min_value(game_tree))
print(max_value(game_tree))