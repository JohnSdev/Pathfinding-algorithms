width=6
height=5


cost = [[0, 0,  0,   0,  0,  0],
         [0, 0,  0,   0,  0,  0],
         [0, 0, "O", "O", 0,  0],
         [0, 0,  2,  "O", 0,  0],
         [0, 0,  2,  "O", 0,  1]]


all_nodes = []
for x in range(height):
    for y in range(width):
        all_nodes.append([x,y])

print (all_nodes)

def neighbors(node):
    dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    result = []
    for dir in dirs:
        neighbor = [node[0] + dir[0], node[1] + dir[1]]
        if 0 <= neighbor[0] < 20 and 0 <= neighbor[1] < 10:
            result.append(neighbor)
    return result

for nodes in all_nodes:
    print(neighbors(nodes))








