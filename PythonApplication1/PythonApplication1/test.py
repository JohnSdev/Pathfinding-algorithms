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
    path=[]
    setpath=0


    tc = [[0 for x in range(C)] for x in range(R)]
 
    tc[0][0] = cost[0][0]
 
    # Initialize first column of total cost(tc) array
    for i in range(1, m+1):
        tc[i][0] = tc[i-1][0] + cost[i][0]
 
    # Initialize first row of tc array
    for j in range(1, n+1):
        tc[0][j] = tc[0][j-1] + cost[0][j]
 
    # Construct rest of the tc array
    for i in range(1, m+1):
        for j in range(1, n+1):
            minim=min(tc[i-1][j-1], tc[i-1][j], tc[i][j-1])
            tc[i][j] = minim + cost[i][j]
            if minim== tc[i-1][j-1]:
                setpath=cost[i-1][j-1]
            elif minim== tc[i-1][j]:
                setpath=cost[i-1][j]
            elif minim== tc[i][j-1]:
                setpath=cost[i][j-1]
            path.append(setpath)

 
   
    for x in tc:
        print(x)
   #print (*tc)
    print(path)
    return tc[m][n]



def rec(start,row,col, map):
    map=map

    
    if col == 7:
        #print(path)
        return map
    
    print(start[row+1][col+1],start[row][col+1],start[row-1][col+1])
    print("Row:{} Col: {}".format(row, col))

    #if ngativa
    if row == 0:
        
        minim=min(start[row+1][col+1], start[row][col+1] )
       
    elif row == 7: #Max storlek på rows -1

        minim=min(start[row][col+1], start[row-1][col+1] )
    else:
        minim=min(start[row+1][col+1], start[row][col+1], start[row-1][col+1] )

    
    if start[row+1][col+1] == minim:
        if row >=5:
            
            return rec(start, row, col+1, map+[row])
           
        elif row+1 <=0:
            
            return rec(start, row, col+1, map+[row] )
            
        else:
            
            return rec(start, row+1, col+1, map+[row] )
           
    
    if start[row][col+1] == minim:
        #path.append(start[row][col+1])
        return rec(start, row, col+1, map+[row])
        #print(path)

    if start[row-1][col+1] == minim:
        if row <=0:
            return rec(start, row, col+1, map+[row] )
           
        else:           
            return rec(start, row-1, col+1, map+[row+1] )
    return map

# Driver program to test above functions
cost = [[1, 2, 3, 4, 5, 62, 72, 1],
        [5, 6, 7, 8, 9, 10, 11, 12],
        [7, 8, 9, 13, 1, 1, 6, 17],
        [10, 11, 12, 12, 1, 2, 14, 13],
        [13, 14, 15, 1, 1, 1, 1, 1],
        [16, 17, 18, 1, 1, 1, 1, 1],
        [16, 17, 18, 55, 166, 661, 66, 1]]

#print(cost[3][0])
#map=[]
#for x in range(0,4):
#    print("rad:{}, costnad: {}".format(x, minCost(cost, 3, x)))
#print(minCost(cost, 5, 2), "Target is 4")
#print(rec(cost, 3,0, map))
buffer=1
col=0
print(cost[col+buffer])

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