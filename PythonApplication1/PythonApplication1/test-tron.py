import math


def minCost(cost, m, n):
    R = 5
    C = 5
    total_cost=[]
    tc = [[0 for x in range(C)] for x in range(R)]


    for col in range(1, n+1):
        for row in range(0, m+1):
            if cost[row][col] == "O":
                cost[row][col] = -1000
            if row <1:
                UP=-10000
            else:
                UP=tc[row-1][col]
             
            LEFT=tc[row][col-1]

            tc[row][col] = max(UP, LEFT) + cost[row][col] * 10 -4
            total_cost.append(tc[row][col])      
    return tc
    

#    print("rad:{}, costnad: {}".format(x, minCost(cost, 3, x)))

#Backtrack example LCS

trow=4
tcol=4

cost2 = [[0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, "O", 0, 0],
         [0, 2, "O", 0, 0],
         [0, 2, "O", 0, 1]]

cost = [[2000, 2500, 1500, 1500],
        [1800, 1900, 4500, 4500],
        [1500, 3000, 2000, 2000],
        [0, 0, 0, 0],
        [2, 3, 2, 1],
        [2, 3, 2, 1]]

#To test the algorithm
tc=minCost(cost2, trow, tcol)
for x in tc:
    print(x)

#path = backtrack( trow,tcol, tc )









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