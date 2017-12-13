import sys, math, random

class Pathfinder:
    def __init__(self, visualiser, map):
        self._visualiser = visualiser
        self._map = map

    def findCheapestPath(self):
        matrix=self._map.getMatrix()
        cost=0
        pathstorage=[]
        bestpath=0
        path=[]
        #Sets bottom/down point at the far end of the matrix in order to test all the possible routes
        m=479
        n=843

        
        (dMatrix, costrow) = self.dynamicP(matrix, m, n)
        #Dynamic algo to find all the end points with leas cost
        pathstorage, debugstorage = self.dynamicPaths(dMatrix)


        
        for j in range(0,479):       
            print(dMatrix[j][836],dMatrix[j][837],dMatrix[j][838],dMatrix[j][839],dMatrix[j][840],dMatrix[j][841],dMatrix[j][842],dMatrix[j][843] )
        for i in debugstorage[1]:
            print(i)
     
         
        #Visualize paths
        
        for paths in pathstorage:
            paths.reverse()
            self._visualiser.addPath(paths)
            
        #Find and show best path
        costrow.sort()
        bestpath=min(costrow)
        for best in range(len(costrow)):
            if costrow[best] == bestpath:
                self._visualiser.setBestPath(pathstorage[best])
                self._visualiser.setBestPathCost( bestpath )


    #Dynamic programming algorithm
    def dynamicP(self, grid, m, n):
        cost=grid
        R = 480
        C = 844
        total_cost=[]
        #Create mirror array
        tc = [[0 for x in range(C)] for x in range(R)]

        #Top down cost traverser
        for i in range(1, n+1):
            for j in range(0, m):
                #BackUp, Back, and BackDown checks
                if j <=1:
                    BU=1000000000
                else:
                    BU=abs(cost[j][i] - cost[j-1][i-1]) + tc[j-1][i-1]
                if j >=478:
                    BD=1000000000
                else:
                
                    BD=abs(cost[j][i] - cost[j+1][i-1]) + tc[j+1][i-1]
                B=abs(cost[j][i] - cost[j][i-1]) + tc[j][i-1]
                next_min=min(BU, B, BD)
                
                print("NM {} on col:{}, pos {}".format(next_min, i, cost[j][i]))
                tc[j][i] = next_min
                
                #Adds total cost to list
                total_cost.append(tc[j][i])



        #Creates a list with all the total cost/row
        costrow=[]
        #Debug chow last col, aka total cost 
        for x in range(0,478):
            costrow.append(tc[x][843])
        #Debug show list with all rows costs
        print(costrow)
         
        return (tc, costrow)

    #Build paths after dynamic arrays it created
    def dynamicPaths(self, grid):
        pathlist=[]
        debuglist=[]
        debubstorage=[]
        pathstorage=[]
        #Start traverse bottom-up
        for i in range(0,477):
            cols=844
            rows=i
            while cols>0:
                if rows >=478:
                    nextMin=min(grid[rows-1][cols-1], grid[rows][cols-1])
                elif rows <=0:
                    nextMin=min(grid[rows][cols-1], grid[rows+1][cols-1])

                else:

                    nextMin=min(grid[rows-1][cols-1], grid[rows][cols-1], grid[rows+1][cols-1])

                if  nextMin == grid[rows+1][cols-1]:
                    pathlist.append(rows+1)
                    debuglist.append([rows+1, cols-1])
                    rows +=1
            
                elif nextMin == grid[rows][cols-1]:
                    pathlist.append(rows)
                    debuglist.append([rows, cols-1])
                    rows = rows
                elif nextMin == grid[rows-1][cols-1]:
                    pathlist.append(rows-1)
                    debuglist.append([rows-1, cols-1])
                    rows -= 1
                #print(nextMin, rows,cols)
                cols-= 1
            
            #Gathers each rows path and appends to pathlist
            pathstorage.append(pathlist)  
            debubstorage.append(debuglist)
            
            debuglist=[]

            pathlist=[]
        return pathstorage, debubstorage

    #Dynamic programming draft     
    def minCost(self, start):
        cost=0


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

