import math
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

 

    tc = [[0 for x in range(C)] for x in range(R)]
    step=2
    tc[0][0] = cost[0][step]#col 3
    
    # Initialize first column of total cost(tc) array
    for i in range(1, m+1):
        tc[i][0] = tc[i-1][0] + cost[i][step]
 
    # Initialize first row of tc array
    for j in range(1, n+1):
        tc[0][j] = tc[0][j-1] + cost[0][j+step]
 
    # Construct rest of the tc array
    for i in range(1, m+1):
        for j in range(1, n+1):
            tc[i][j] = min(tc[i-1][j-1], tc[i-1][j], tc[i-1][j+1]) + cost[i][j+step]
    for x in tc:
        print(x)
   #print (*tc)
    return tc[m][n]

# Driver program to test above functions
cost = [[2, 1, 1, 1, 1, 1, 1, 1],
        [2, 31, 1, 1, 1, 1, 1, 1],
        [2, 31, 1, 1, 1, 1, 1, 1],
        [2, 31, 1, 1, 1, 1, 1, 1],
        [2, 31, 1, 1, 1, 1, 1, 1],
        [2, 31, 1, 1, 1, 1, 1, 1]]
#for x in range(0,4):
#    print("rad:{}, costnad: {}".format(x, minCost(cost, 3, x)))
#print(minCost(cost, 5, 5), "Target is 4")

lista=[1,2,3,4,5]
lista.reverse()
print(lista)
# This code is contributed by Bhavya Jain
 
#print(cost)
#new=list(zip(*cost))[::-1]
#new = list(map(list, new))
#print(new)
