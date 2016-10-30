"""
Project Euler Problem 15
========================

Starting in the top left corner of a 2 * 2 grid, there are 6 routes
(without backtracking) to the bottom right corner.

How many routes are there through a 20 * 20 grid?
"""

class Node(object):
    name = ""
    up = None
    right = None
    down = None
    left = None
    def __repr__(object):
        return object.name

nodes = []

def create_grid(size):
    global nodes

    for i in range(size + 1):
        nodes.insert(i, range(size+1))
    
    for (x, y) in [(i, j) for i in range(size+1) for j in range(size+1)]:
        node = Node()
        node.name = str(y + x*(size+1))
        nodes[x][y] = node

    for (x, y) in [(i, j) for i in range(size+1) for j in range(size+1)]:
        if y < size:
            nodes[x][y].right = nodes[x][y+1]
        if y > 0:
            nodes[x][y].left  = nodes[x][y-1]
        if x < size:
            nodes[x][y].down  = nodes[x+1][y]
        if x > 0:
            nodes[x][y].up    = nodes[x-1][y]
        
count_dict = {}
def count_paths(node, used = None):
    global count_dict
    if count_dict.has_key(node.name):
        return count_dict[node.name]
    
    output = 0

    if not used:
        used = []
    
    used.append(node.name)
    
    global nodes
    if node.name == '440':
        return 1
    """
    if node.up and node.up.name not in used:
        tmp_used = list(used)
        output += count_paths(node.up, tmp_used)
    """        
    if node.right and node.right.name not in used:
        tmp_used = list(used)
        output += count_paths(node.right, tmp_used)

    if node.down and node.down.name not in used:
        tmp_used = list(used)
        output += count_paths(node.down, tmp_used)
    """
    if node.left and node.left.name not in used:
        tmp_used = list(used)
        output += count_paths(node.left, tmp_used)
    """
    count_dict[node.name] = output
    return output
    
create_grid(20)
#print nodes
print count_paths(nodes[0][0])
