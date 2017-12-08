import sys, math, random

class Pathfinder:
    def __init__(self, visualiser, map):
        self._visualiser = visualiser
        self._map = map

    def findCheapestPath(self):
        cost=0
        # Mark's silly algorithm for finding the cheapest path:
        #   Use random logic - virtually gauranteed to give the correct answer
        #   eventually if we just run it enough times.
        #   NOTE: Since problem is NP-hard - we won't know for sure that it is
        #         the correct answer when we get it which is a bummer.
        path=[]
        # Starting at a random position on the left:
        for x in range(0,1):
            starting_row = x

            # Search for one random path:
            ( cost ) = self.minCost( starting_row )
            print(cost)
        # It is the only path we have found, visualise it:
       # self._visualiser.addPath(path)

        # The only path so it must also be the best path, visualise that:
            self._visualiser.setBestPath(path)

        # And the cost of this so called "best" path:
            self._visualiser.setBestPathCost( cost )

        # What next?  Can you do better than random?
        # TODO:  Step 1 - a greeedy algorithm from a random starting position
        # TODO:  Step 2 - best greedy of all possible starting positions
        # TODO:  Step 3 - improve even more!
        return


    def minCost(self, start):
        cost=0
        totalsum=[]
    #    # for q in range(0,5):
        
	   # # Instead of following line, we can use int tc[m+1][n+1] or
	   # # dynamically allocate memoery to save space. The following
	   # # line is used to keep te program simple and make it working
	   # # on all compilers
        rows = self._map.getHeight()
        cols = self._map.getWidth()
        row = start
        costn = []
        col=0
        path=[ row ]
        path.append( row )
        #Rotate matrix 90deg
        matrix=self._map.getMatrix()
        new=list(zip(*matrix))[::-1]
        newmatrix = list(map(list, new))
        #Temporary array size
        R = 900
        C = 600
        #Point to find min cost path in array
        m=839
        n=300

        total_cost=[]
        tc = [[0 for x in range(C)] for x in range(R)]
        step=0
        tc[0][0] = newmatrix[0][step]#col 3
    
    
        for i in range(1, m+1):
            tc[i][0] = abs(newmatrix[i-1][0] - newmatrix[i][step])
            #tc[i][0] = tc[i-1][0] + cost[i][step]
 
  
        for j in range(1, n+1):
            tc[0][j] = abs(newmatrix[0][j-1] - newmatrix[0][j+step])
 
    
        for i in range(1, m+1):
            for j in range(1, n+1):
                next_min=min(newmatrix[i-1][j-1], newmatrix[i-1][j], newmatrix[i][j-1])
                tc[i][j] = abs(next_min - newmatrix[i][j+step])
                #add append of abs to list
                total_cost.append(tc[i][j])
                #print(total_cost)
            r=
        totalsum.append(sum(total_cost))
        total_cost=[]
        for x in tc:
            print(x)
        return totalsum

        ##return (best, path)
      

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

