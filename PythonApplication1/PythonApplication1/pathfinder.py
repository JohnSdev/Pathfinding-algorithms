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
        pathlista=[]
        costlista=0
        costlist=[]
        emptypath=[]
        # Starting at a random position on the left:
        for i in range(5,9):

            starting_row = i
            matrix=self._map.getMatrix()
            
            # Search for one random path:
            #( cost ) = self.minCost( starting_row )
            

            (path, cost)  = self.rec(matrix,i, 0, emptypath, costlista)
            costlist.append(cost)
            path.extend([0])
            pathlista.append(path)
           
            #print(sum(costa))
            self._visualiser.addPath(path)
            # It is the only path we have found, visualise it:
        
        
        print("length 1:{}  2: {}".format(len(pathlista[0]), len(pathlista[1])))  
        
        for x in range(len(pathlista[0])):

            print(pathlista[0][x], pathlista[1][x],"\n")
        print(pathlista[1])
        #Draw other paths

        
            
        
        #Calculate best path to draw
        bestpath=min(costlist)
        
        for x in range(len(costlist)):
            if costlist[x] == bestpath:
                self._visualiser.setBestPath(pathlista[1])
                
        
        
        #And the cost of this so called "best" path:
        print("Least cost in m: ", min(costlist))
        self._visualiser.setBestPathCost( min(costlist) )
     

        # What next?  Can you do better than random?
        # TODO:  Step 1 - a greeedy algorithm from a random starting position
        # TODO:  Step 2 - best greedy of all possible starting positions
        # TODO:  Step 3 - improve even more!
        return

    ##Recursive func
    def rec(self, start,row,col, path, accu):
        
        costa=accu
        path=path
        #print(costa)
        """
        if col == 834:
            return (path, costa)
        if col >= 840:
            #if ngativa
            if row == 0:
        
                minim=min(start[row+1][col+1], start[row][col+1] )
       
            elif row == 400: #Max storlek på rows -1

                minim=min(start[row][col+1], start[row-1][col+1] )
            else:
                minim=min(start[row+1][col+1], start[row][col+1], start[row-1][col+1] )

            #DownFwd
            if start[row+1][col+1] == minim:
            
                if row >400:
                    costa+=abs(start[row][col] - start[row][col+1])
                    return self.rec(start, row, col+1, path+[row],costa)
           
                elif row+1 <=0:
                    costa+=abs(start[row][col] - start[row][col+1])
                    return self.rec(start, row, col+1, path+[row], costa )
            
                else:
                    costa+=abs(start[row][col] - start[row+1][col+1])
                    return self.rec(start, row+1, col+1, path+[row], costa )
           
            #Fwd
            if start[row][col+1] == minim:
                #path.append(start[row][col+1])
                costa+=abs(start[row][col] - start[row][col+1])
                return self.rec(start, row, col+1, path+[row], costa)
                #print(path)

            #UppFwd
            if start[row-1][col+1] == minim:
                if row <=0:
                    costa+=abs(start[row][col] - start[row][col+1])
                    print(costlist)
                    return self.rec(start, row, col+1, path+[row], costa )
           
                else:
                    costa+=abs(start[row][col] - start[row-1][col+1])
                
                    return self.rec(start, row-1, col+1, path+[row+1], costa )
            

        
        buffermin_dwn=abs(start[row+1][col+1] - start[row][col])
        buffermin_up=abs(start[row-1][col+1] - start[row][col])
        buffermin_fwd=abs(start[row][col+1] - start[row][col])
        buffermin=min(buffermin_fwd, buffermin_up, buffermin_dwn)

            
        #dwnfwd
        if buffermin == buffermin_dwn:
            if row >478:
                costa+=abs(start[row][col] - start[row][col+1])
                return self.rec(start, row, col+1, path+[row],costa)
           
            elif row+1 <=0:
                costa+=abs(start[row][col] - start[row][col+1])
                return self.rec(start, row, col+1, path+[row], costa )
            
            else:
                costa+=abs(start[row][col] - start[row+1][col+1])
                return self.rec(start, row+1, col+1, path+[row], costa )

        #Fwd
        if buffermin == buffermin_fwd:
            costa+=abs(start[row][col] - start[row][col+1])
            return self.rec(start, row, col+1, path+[row], costa)
               

        #UppFwd
        if buffermin == buffermin_up:
            if row <=0:
                costa+=abs(start[row][col] - start[row][col+1])
                return self.rec(start, row, col+1, path+[row], costa )
           
            else:
                costa+=abs(start[row][col] - start[row-1][col+1])      
                return self.rec(start, row-1, col+1, path+[row+1], costa )
        return (path, costa)    
        ####
        """
 #######################################################################################          
        if col == 843:
            return (path, costa)
        #print(start[row+1][col+1],start[row][col+1],start[row-1][col+1])
        #print("Row:{} Col: {}".format(row, col))

        #If position is att top most 
        radarchoice=0
        if row == 0:
            if start[row+1][col+1] == start[row][col+1]: #Id next are equal, check 5 seps ahead
                radarchoice=min(start[row+2][col+5], start[row][col+5] #Check 5 step ahead and set next row to it.
                if radarchoice==start[row+2][col+5]:
                    minim=start[row+1][col+1]
                else:
                    minim==start[row][col+1]

            else:
            minim=min(start[row+1][col+1], start[row][col+1] )

        #If postiton is at bottom
        elif row == 478: 
            #if start[row+1][col+1] == (start[row][col+1]): #Id next are equal, randomize
            #    minim=min(start[row][col+2], start[row-2][col+2] )
            #else:

            minim=min(start[row][col+1], start[row-1][col+1] )

        
        
            
        #If position is not top/bottom
        else:
            minim=min(start[row+1][col+1], start[row][col+1], start[row-1][col+1] )
        

        #Fwd
        if start[row][col+1] == minim:
            #path.append(start[row][col+1])
            costa+=abs(start[row][col] - start[row][col+1])
            return self.rec(start, row, col+1, path+[row], costa)
            #print(path)

        #DownFwd
        if start[row+1][col+1] == minim:
            
            if row >470:
                costa+=abs(start[row][col] - start[row][col+1])
                return self.rec(start, row, col+1, path+[row],costa)
           
            elif row+1 <=0:
                costa+=abs(start[row][col] - start[row][col+1])
                return self.rec(start, row, col+1, path+[row], costa )
            
            else:
                costa+=abs(start[row][col] - start[row+1][col+1])
                return self.rec(start, row+1, col+1, path+[row], costa )
           


        #UppFwd
        if start[row-1][col+1] == minim:
            if row <=0:
                costa+=abs(start[row][col] - start[row][col+1])
                print(costlist)
                return self.rec(start, row, col+1, path+[row], costa )
           
            else:
                costa+=abs(start[row][col] - start[row-1][col+1])
                
                return self.rec(start, row-1, col+1, path+[row+1], costa )
                
        
        return  path
        


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
        n=1

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
                next_min=min(newmatrix[i-1][j-1], newmatrix[i-1][j], newmatrix[i-1][j+1])
                tc[i][j] = abs(next_min - newmatrix[i][j+step]) + tc[i-1][j-1]
                #add append of abs to list
                #total_cost.append(tc[i][j])
                #print(total_cost)
            
        #totalsum.append(sum(total_cost))
        #total_cost=[]
        #for x in tc:
        #    print(x)
        return tc[i][j]

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

