import sys, math, random

class Pathfinder:
    def __init__(self, visualiser, map):
        self._visualiser = visualiser
        self._map = map

    def findCheapestPath(self):
        matrix=self._map.getMatrix()
        cost=0
        # Mark's silly algorithm for finding the cheapest path:
        #   Use random logic - virtually gauranteed to give the correct answer
        #   eventually if we just run it enough times.
        #   NOTE: Since problem is NP-hard - we won't know for sure that it is
        #         the correct answer when we get it which is a bummer.

        # Starting at a random position on the left:
        for x in range(0,1):
            m=479
            n=843
            starting_row = x

            # Search for one random path:

            #self.minCost( starting_row )
            (dMatrix) = self.dynamicP(matrix, m, n)
            self.dynamicPaths(dMatrix)


            #print(path)
        # It is the only path we have found, visualise it:
       # self._visualiser.addPath(path)

        # The only path so it must also be the best path, visualise that:
            #self._visualiser.setBestPath(path)

        # And the cost of this so called "best" path:
            #self._visualiser.setBestPathCost( cost )
            
        # What next?  Can you do better than random?
        # TODO:  Step 1 - a greeedy algorithm from a random starting position
        # TODO:  Step 2 - best greedy of all possible starting positions
        # TODO:  Step 3 - improve even more!
        return

    def dynamicP(self, grid, m, n):
        cost=grid
        R = 900
        C = 900

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
            for j in range(1, m+1):
                if j <=1:
                    BU=1000000000
                else:
                    BU=abs(cost[j][i] - cost[j-1][i-1]) + tc[j-1][i-1]
                if j >=477:
                    BD=1000000000
                else:
                
                    BD=abs(cost[j][i] - cost[j+1][i-1]) + tc[j+1][i-1]
                B=abs(cost[j][i] - cost[j][i-1]) + tc[j][i-1]
                next_min=min(BU, B, BD)
                
                print("NM {} on col:{}, pos {}".format(next_min, i, cost[j][i]))
                tc[j][i] = next_min
                
                #add append of abs to list
                total_cost.append(tc[j][i])

        #for x in tc:
        #    print(x)

        print("")
        print("Original Matrix {}, {}".format(m,n))
        costrow=[]
        for x in range(0,478):
            costrow.append(tc[x][843])
        
        print("Total Cost :",tc[m][n])
        
        
        return tc

    def dynamicPaths(self, grid):
        pathlist=[]

        for cols in range (0, 843, -1):
            for rows in range(1, 479):
             pathlist.append(min(grid[rows-1][cols+1], grid[rows][cols+1], grid[rows+1][cols+1] ))
        
        cols=848
        rows=1
        while cols>0:
            nextMin=min(grid[rows-1][cols-1], grid[rows][cols-1], grid[rows+1][cols-1])
            if nextMin == grid[rows-1][cols-1]:
                pathlist.append(rows-1)
            elif nextMin == grid[rows][cols-1]:
                pathlist.append(rows)
            elif nextMin == grid[rows+1][cols-1]:
                pathlist.append(rows+1)
            cols-= 1
        print(pathlist)
        return



            
    def minCost(self, start):
        cost=0
   
    #    # for q in range(0,5):
        
	   # # Instead of following line, we can use int tc[m+1][n+1] or
	   # # dynamically allocate memoery to save space. The following
	   # # line is used to keep te program simple and make it working
	   # # on all compilers.

        rows = self._map.getHeight()
        cols = self._map.getWidth()

        row = start

        costn = []
        col=0
        path=[ row ]
        path.append( row )
        matrix=self._map.getMatrix()
        new=list(zip(*matrix))[::-1]
        rotatedmap = list(map(list, new))
        R = 900
        C = 600
        m=840
        n=5
        #col=0
        
        #path=[col]
        
        step=0

        tc = [[0 for x in range(C)] for x in range(R)]
        
        tc[0][0] = rotatedmap[0][step]#col 3
    
        # Initialize first column of total cost(tc) array
        for i in range(1, m+1):
            tc[i][0] = tc[i-1][0] + rotatedmap[i][step]
        
        # Initialize first row of tc array
        for j in range(1, n+1):
            tc[0][j] = tc[0][j-1] + rotatedmap[0][j+step]
        
        # Construct rest of the tc array
        for i in range(1, m+1):
            for j in range(1, n+1):
                next_min=min(tc[i-1][j-1], tc[i-1][j], tc[i][j-1])
                tc[i][j] = abs(next_min - rotatedmap[i][j+step])     
                       

        #Construct path
       


        costn.append(int(tc[m][n]))        
        #path.append(col)
        #print (costn)
        total=(sorted(costn))
       
        print(tc[m][n])
        r=0
        path=[ row ]
        row = row + r
        if row < 0:
            row = 0
        if row > rows-1:
        
            row = rows-1
        
        path.append(row)

        return 
      

    #        total.append(sum(costn))

    #    print(sorted(total))
        
    #def findPath(self, starting_row):
    #    # Code to find one path from left to right through the map
    #    # And return the total "cost" and path
    #    # Current finds only a random path - can you make it better?

    #    matrix = self._map.getMatrix()
    #    rows = self._map.getHeight()
    #    cols = self._map.getWidth()

    #    row = starting_row

    #    cost = 0
    #    col=0
    #    path=[ row ]

    #    while col+1 < cols:
    #        # how high are we right now?
    #        current_altitude = matrix[row][col]

    #        # Pick a random direction - up/right,  right,  down/right
    #        r = random.randint(-1,1)
    #        row = row + r
    #        if row < 0:
    #            row = 0
    #        if row > rows-1:
    #            row = rows-1
    #        col += 1

    #        # how high are we now?
    #        new_altitude = matrix[row][col]

    #        # change in height:
    #        delta = int( math.fabs( new_altitude - current_altitude ) )

    #        # cost is the absolute change in height per step
    #        cost += delta

    #        # add this step to the path we are following
    #        path.append( row )
    #        print(path)


    #    return ( cost, path )

