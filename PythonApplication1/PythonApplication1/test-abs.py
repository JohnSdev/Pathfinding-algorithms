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
    R = 4
    C = 4

    total_cost=[]
    tc = [[0 for x in range(C)] for x in range(R)]

    step=0
    #tc[0][0] = cost[0][step]#col 3
    
    
    #for i in range(1, m+1):
    #    tc[i][0] = abs(cost[i-1][0] - cost[i][step])
    #    #tc[i][0] = tc[i-1][0] + cost[i][step]
 
  
    #for j in range(1, n+1):
    #    tc[0][j] = abs(cost[0][j-1] - cost[0][j+step])
 
    print("DP Matrix")
    #for i in range(0, m):
    #    for j in range(0, n):
    #        next_min=min(cost[i-1][j-1]+tc[i-1][j-1], cost[i][j-1]+tc[i][j-1], cost[i+1][j-1]+tc[i+1][j-1])
    #        tc[i][j] = abs(next_min - cost[i][j+step])
    #        #add append of abs to list
    #        total_cost.append(tc[i][j])

    for i in range(1, n+1):
        for j in range(0, m):
            print(cost[j][i])
            print(cost[j-1][i-1])
            print(cost[j][i-1])
            print(cost[j+1][i-1])
            print(abs(cost[j][i+step] - cost[j-1][i-1])+tc[j-1][i-1])
            print(abs(cost[j][i+step] - cost[j][i-1]) +tc[j][i-1])
            print(abs(cost[j][i+step] - cost[j+1][i-1])+tc[j+1][i-1])

            next_min=min(abs(cost[j][i+step] - cost[j-1][i-1]) + tc[j-1][i-1], 
                         abs(cost[j][i+step] - cost[j][i-1]) + tc[j][i-1],
                         abs(cost[j][i+step] - cost[j+1][i-1]) + tc[j+1][i-1])
            print("NM",next_min)
            tc[j][i] = next_min
            #add append of abs to list
            total_cost.append(tc[j][i])

    for x in tc:
        print(x)

    print("")
    print("Original Matrix {}, {}".format(m,n))
    for x in cost:
        print(x)
    print("Total Cost :",tc[m][n])
    #print (*tc)

    #Construct path
        
    return tc

# Driver program to test above functions

#for x in range(0,4):
#    print("rad:{}, costnad: {}".format(x, minCost(cost, 3, x)))


def backtrack( a, b, LCS ):
    s = ""
    # read the substring out from the matrix
    i = a
    j = b
    while i>0 and j > 0:
        if LCS[i][j] == LCS[i-1][j]:
            i -= 1
        elif LCS[i][j] == LCS[i][j-1]:
            j -= 1
        else:
            # must have been a match
            s = a[i-1] + s
            i -= 1
            j -= 1
    return s

trow=2
tcol=2

cost2 = [[1, 1, 2, 1],
        [2, 3, 2, 2],
        [2, 3, 2, 1],
        [2, 3, 2, 1],
        [2, 3, 2, 1]]

cost = [[2000, 2500, 1500, 1500],
        [1800, 1900, 4500, 4500],
        [1500, 3000, 2000, 2000],
        [0, 0, 0, 0],
        [2, 3, 2, 1],
        [2, 3, 2, 1]]

tc=minCost(cost, trow, tcol)
path = backtrack( trow,tcol, tc )









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