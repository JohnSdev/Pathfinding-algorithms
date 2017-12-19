import math
"""from map import *

map=[[1,13,1,1],
     [22,32,2,2],
     [3,4,5,6]]

for i in range(0,2):
    a1=map[-1]
    a2=map[-2]
    for x in range(len(map)):
        a2[x] += min(a1[x], a1[x+1])
        print(a2)
    map.pop(-1)
    map[-1] = a2
print(map[0][0])


# Dynamic Programming Python implementation of Min Cost Path
# problem

import fileinput
from itertools import accumulate


    if not matrix:
        return 0                                # 0 rows

    rows = iter(matrix)
    best = list(accumulate(next(rows)))
    print(best)
    if not best:
        return 0                                # 0 columns

    for row in rows:
        best[0] += row[0]
        for j in range(1, len(row)):
            best[j] = row[j] + min(best[j-1],   # approaching from the left
                                   best[j])     # approaching from above
    return best[-1]
"""
 
def minCost(cost, m, n):
    R = 10
    C = 10

 
    total_cost=[]
    tc = [[0 for x in range(C)] for x in range(R)]
    step=3
    tc[0][0] = cost[0][step]#col 3
    
    
    #for i in range(1, m+1):
    #    tc[i][0] = abs(cost[i-1][0] - cost[i][step])
    #    #tc[i][0] = tc[i-1][0] + cost[i][step]
 
  
    #for j in range(1, n+1):
    #    tc[0][j] = abs(cost[0][j-1] - cost[0][j+step])
 
    
    for i in range(1, m+1):
        for j in range(0, n+1):
            next_min=min(cost[i-1][j-1], cost[i-1][j], cost[i-1][j+1])
            print(next_min)
            tc[i][j] = abs(next_min - cost[i][j+step])
            print(cost[i][j+step])
            #add append of abs to list
            total_cost.append(tc[i][j])
    for x in tc:
        print(x)
   #print (*tc)
    print(sum(total_cost))
    return tc[m][n]

# Driver program to test above functions
cost = [[0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0],
        [0, 2, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]]
#for x in range(0,4):
#    print("rad:{}, costnad: {}".format(x, minCost(cost, 3, x)))
print(minCost(cost, 3,5), "Target is 4")


# This code is contributed by Bhavya Jain
 
#print(cost)
#new=list(zip(*cost))[::-1]
#new = list(map(list, new))
#print(new)

[[1, 1, 5], 
 [7, 7, 0], 
 [2, 7, 1]]

"""
[[1104, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
 [2, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
 [5, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
 [15, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
 [17, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

# This code is contributed by Bhavya Jain
"""