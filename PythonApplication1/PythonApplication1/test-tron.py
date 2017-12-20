import math


def minCost(cost, m, n):
    R = 10
    C = 10
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

            tc[row][col] = max(UP, LEFT) + cost[row][col] +100
            total_cost.append(tc[row][col])      
    return tc
    

#    print("rad:{}, costnad: {}".format(x, minCost(cost, 3, x)))

#Backtrack example LCS
def backtrack(tc, rows, cols):
    pathlist=[]
    debuglist=[]
    debubstorage=[]
    pathstorage=[]
    rows=4
    newdir=""

    #Start traverse bottom-up
    #for i in range(4,5):
    #    rows = i

    #if direction == "LEFT":
    while cols >0:
            
        if rows >=4:
            nextMin=max(tc[rows-1][cols], tc[rows][cols-1])
        elif rows <=0:
            nextMin=max(tc[rows][cols-1], tc[rows+1][cols])
        else:
            nextMin=max(tc[rows-1][cols], tc[rows][cols-1], tc[rows+1][cols])
                
        if  nextMin == tc[rows+1][cols]:         
            newdir = "DOWN"
            pathlist.append("DOWN")
            tc[rows+1][cols] = 0
            #debuglist.append([rows+1, cols-1])
            rows +=1          
        elif nextMin == tc[rows][cols-1]:
            newdir = "LEFT"
            pathlist.append("LEFT")
            #debuglist.append([rows, cols-1])
            cols -=1
            tc[rows][cols-1] = 0
        elif nextMin == tc[rows-1][cols]:
            #print(nextMin, rows, cols)
            newdir = "UP"
            pathlist.append("UP")
            rows -= 1
            tc[rows][cols-1] = 2
         
        print(nextMin, rows,cols)
            
    return newdir, pathlist

trow=4
tcol=4

cost2 = [[0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, "O", 0, 0],
         [0, 0, 2, "O", 0, 0],
         [0, 0, 2, "O", 0, 1]]

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

path, pathlist = backtrack(tc, trow,tcol)
print(pathlist)








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