

cost = [[2000, 2500, 1500, 1500],
        [1800, 1900, 4500, 4500],
        [1500, 3000, 2000, 2000]]

all_nodes = []
for row in range(2):
    for col in range(2):
        all_nodes.append([row,col])

print(all_nodes)




def neighbors(node):
    neighbor=[]
    dirs = [[-1, 1], [0, 1], [1, 1]]
    result = []
    for dir in dirs:
        neighbor= [node[0] + dir[0], node[1] + dir[1]]
        if neighbor in all_nodes:
            result.append(neighbor)
    return result

def neighbors2(node):
    dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    result = []
    for dir in dirs:
        neighbor = [node[0] + dir[0], node[1] + dir[1]]
        if 0 <= neighbor[0] < 2 and 0 <= neighbor[1] < 2:
            result.append(neighbor)
    return result

for node in all_nodes:
   print( neighbors2(node))



print()

