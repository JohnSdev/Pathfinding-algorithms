import sys, math, random
from statistics import mean, median
from bresenham import bresenham

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
        mergedpath=[]
        buffer=2 #Set Radar buffer, aka look ahead if either of next col is equal. 

        # Starting at a random position on the left:
        for i in range(5,50,1):
            
            starting_row = i
            matrix=self._map.getMatrix()
            
            # Experiment with Dynamic programming
            #( cost ) = self.minCost( starting_row )
                      
            (path, cost)  = self.rec(matrix,i, 0, emptypath, costlista, buffer)

            mergedpath=[item for sublist in path for item in sublist]
                   
            costlist.append(cost)
            #path.extend([0])
            pathlista.append(mergedpath)
                      
            #Add all paths and visualize them
            self._visualiser.addPath(mergedpath)
            
            #Reset path list for each iteration
            mergedpath=[1]
        
        print("length 1:{}  2: {}".format(len(pathlista[0]), len(pathlista[2])))  
            
        #Calculate best path to draw
        bestpath=min(costlist)
        
        for x in range(len(costlist)):
            if costlist[x] == bestpath:
                self._visualiser.setBestPath(pathlista[x])
                

        print(sorted(costlist)) #Debug list of all costs
        print("Least cost in m: ", min(costlist))
        #Visualize best path
        self._visualiser.setBestPathCost( min(costlist) )
        #path=[]
        #self.recRadar(matrix, x , 0, path, costlista, buffer)
        #print("path:", path)
        #self._visualiser.setBestPath(pathlista[1])
     
        return

    def findCheapestPathWithRadar(self):
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
        mergedpath=[]
        buffer=2 #Set Radar buffer, aka look ahead if either of next col is equal. 

        # Starting at a random position on the left:
        for i in range(5,50,1):
            
            starting_row = i
            matrix=self._map.getMatrix()
            
            # Experiment with Dynamic programming
            #( cost ) = self.minCost( starting_row )
                      
            #(path, cost)  = self.rec(matrix,i, 0, emptypath, costlista, buffer)
            (path, cost)  = self.recRadar(matrix, i , 0, emptypath, costlista, buffer)

            mergedpath=[item for sublist in path for item in sublist]
                   
            costlist.append(cost)
            #path.extend([0])
            pathlista.append(mergedpath)
                      
            #Add all paths and visualize them
            self._visualiser.addPath(mergedpath)
            
            #Reset path list for each iteration
            mergedpath=[1]
        
        print("length 1:{}  2: {}".format(len(pathlista[0]), len(pathlista[2])))  
            
        #Calculate best path to draw
        bestpath=min(costlist)
        
        for x in range(len(costlist)):
            if costlist[x] == bestpath:
                self._visualiser.setBestPath(pathlista[x])
                

        print(sorted(costlist)) #Debug list of all costs
        print("Least cost in m: ", min(costlist))
        #Visualize best path
        self._visualiser.setBestPathCost( min(costlist) )
        #path=[]
        #self.recRadar(matrix, x , 0, path, costlista, buffer)
        #print("path:", path)
        #self._visualiser.setBestPath(pathlista[1])
     
        return

    #Recursive radar draft
    def recRadar(self, grid,  row , col, path, accu, buffer):
        path=path
        cost=accu
        print(col)
        buffer=buffer
        maxrow=2
        if col == 843:
            buffer=1       
        if row == 479-buffer:
            maxrow=maxrow-1
        if col >= 838:
            return (path, cost)
        lista0=[]
        lista1=[]
        lista2=[]
        lista3=[]
        lista4=[]
        lista5=[]
        lista6=[]
        lista7=[]
        lista8=[]
        lista9=[]
        
        nylista0=[]
        nylista1=[]
        nylista2=[]
        nylista3=[]
        nylista4=[]
        nylista5=[]
        nylista6=[]
        nylista7=[]
        nylista8=[]
        nylista9=[]

        #Generate generic radar rays 
        degupp=[]
        deg90=[]
        degdwn=[]
        fwdUpp=list(bresenham(row, col, row-maxrow, col+buffer))
        degupp_path=[]
        fwd=list(bresenham(row, col, row, col+buffer))

        for x in range(-5,5):
            
            lista0=list(bresenham(row, col, row+x, col+buffer))
        
        deg90_path=[]
        fwdDwn=list(bresenham(row, col, row+maxrow, col+buffer))
        degdwn_path=[]
        
        bestup=0
        bestfwd=0
        bestdwn=0
        radarcost=0

        for x in fwdUpp:
            degupp.append(x)
        for x in fwd:
            deg90.append(x)
        for x in fwdDwn:
            degdwn.append(x)
        
        for lists in range(0,9):
            for steps in range(len(lista0)):
                (rows,cols) = lista
                (rows2,cols2) = lista[lists][steps+1]
                nylista[x].append(row)
            #print(row, col, row2, col2)

            radarcost+=abs(grid[rows][cols] - grid[rows2][cols2])

        for steps in range(len(degupp,)-1):
            (rows,cols) = degupp[steps]
            (rows2,cols2) = degupp[steps+1]
            degupp_path.append(row)
            #print(row, col, row2, col2)
            radarcost+=abs(grid[rows][cols] - grid[rows2][cols2])
            
        bestup=radarcost
        radarcost=0

        for steps in range(len(deg90,)-1):
            (rows,cols) = deg90[steps]
            (rows2,cols2) = deg90[steps+1]
            deg90_path.append(row)
 
            radarcost+=abs(grid[rows][cols] - grid[rows2][cols2])
        bestfwd=radarcost
        radarcost=0


        for steps in range(len(degdwn,)-1):
            (rows,cols) = degdwn[steps]
            (rows2,cols2) = degdwn[steps+1]
            degdwn_path.append(row)
            radarcost+=abs(grid[rows][cols] - grid[rows2][cols2])
        bestdwn=radarcost
        radarcost=0

        #Sets which radar ray got the least cost. 
        best_choice=min(bestup, bestfwd, bestdwn)

        #Ray Up
        if best_choice == bestup:
            cost+=best_choice
            #path.append(degupp_path)

            return self.recRadar(grid,  row-maxrow , col+buffer, path+[degupp_path], cost, buffer)
        #Ray Fwd
        elif best_choice == bestfwd:
            cost+=best_choice
            #path.append(deg90_path)

            return self.recRadar(grid,  row , col+buffer, path+[deg90_path], cost, buffer)        
        #Ray Dwn
        elif best_choice == bestdwn:
            cost+=best_choice
            #path.append(degdwn_path)

            return self.recRadar( grid,  row+maxrow , col+buffer, path+[degdwn_path], cost, buffer)
        
        return path





    ##Recursive func
    def rec(self, start,row,col, path, accu, buffer):
        
        costa=accu
        path=path
        maxrow=5
        #buffer=buffer
        
        """
        if col == 834:
            return (path, costa)
        if col >= 840:
            #if ngativa
            if row == 0:
        
                minim=min(FwdU, FwdS )
       
            elif row == 400: #min storlek på rows -1

                minim=min(FwdS, FwdD )
            else:
                minim=min(FwdU, FwdS, FwdD )

            #DownFwd
            if FwdU == minim:
            
                if row >400:
                    costa+=abs(start[row][col] - FwdS)
                    return self.rec(start, row, col+1, path+[row],costa)
           
                elif row+1 <=0:
                    costa+=abs(start[row][col] - FwdS)
                    return self.rec(start, row, col+1, path+[row], costa )
            
                else:
                    costa+=abs(start[row][col] - FwdU)
                    return self.rec(start, row+1, col+1, path+[row], costa )
           
            #Fwd
            if FwdS == minim:
                #path.append(FwdS)
                costa+=abs(start[row][col] - FwdS)
                return self.rec(start, row, col+1, path+[row], costa)
                #print(path)

            #UppFwd
            if FwdD == minim:
                if row <=0:
                    costa+=abs(start[row][col] - FwdS)
                    print(costlist)
                    return self.rec(start, row, col+1, path+[row], costa )
           
                else:
                    costa+=abs(start[row][col] - FwdD)
                
                    return self.rec(start, row-1, col+1, path+[row+1], costa )
            

        
        buffermin_dwn=abs(FwdU - start[row][col])
        buffermin_up=abs(FwdD - start[row][col])
        buffermin_fwd=abs(FwdS - start[row][col])
        buffermin=min(buffermin_fwd, buffermin_up, buffermin_dwn)

            
        #dwnfwd
        if buffermin == buffermin_dwn:
            if row >478:
                costa+=abs(start[row][col] - FwdS)
                return self.rec(start, row, col+1, path+[row],costa)
           
            elif row+1 <=0:
                costa+=abs(start[row][col] - FwdS)
                return self.rec(start, row, col+1, path+[row], costa )
            
            else:
                costa+=abs(start[row][col] - FwdU)
                return self.rec(start, row+1, col+1, path+[row], costa )

        #Fwd
        if buffermin == buffermin_fwd:
            costa+=abs(start[row][col] - FwdS)
            return self.rec(start, row, col+1, path+[row], costa)
               

        #UppFwd
        if buffermin == buffermin_up:
            if row <=0:
                costa+=abs(start[row][col] - FwdS)
                return self.rec(start, row, col+1, path+[row], costa )
           
            else:
                costa+=abs(start[row][col] - FwdD)      
                return self.rec(start, row-1, col+1, path+[row+1], costa )
        return (path, costa)    
        ####
        """
 #######################################################################################          
        if col == 843-buffer:
            buffer=buffer-1
        if row == 479-buffer:
            maxrow=maxrow-1
        if col == 843:
            return (path, costa)
        #print(FwdU,FwdS,FwdD)
        print("Row:{} Col: {}, cost: {}".format(row, col, costa))

        #If position is att top most 
        FwdU=start[row-1][col+1]
        FwdS=start[row][col+1]
        FwdD=start[row+1][col+1]

        #Set how far the Radar will look
        
        FwdUBuffer=start[row-3][col+buffer]
        FwdSBuffer=start[row][col+buffer]
        FwdDBuffer=start[row+3][col+buffer]

        buffermin_upp=abs(FwdUBuffer - start[row][col])
        buffermin_dwn=abs(FwdDBuffer - start[row][col])
        buffermin_fwd=abs(FwdSBuffer - start[row][col])
        buffermin=min(buffermin_fwd, buffermin_upp, buffermin_dwn)        
        
        
        radarchoice=None #What the radar has selected -1, 0, 1

        #If position is at top dont look above matix
        if row == 0:
            if FwdU == FwdS: #Id next are equal, Use radar buffer
                radarchoice=min(buffermin_fwd, buffermin_dwn) #
                if radarchoice==buffermin_fwd:
                    minim=FwdS
                else:
                    minim=FwdD

            else:
                minim=min(FwdD, FwdS )

        #If postiton is at bottom, dont look past max limit.
        elif row == 478: 
            if FwdU == FwdS: 
                radarchoice=min(buffermin_upp, buffermin_fwd )
                if radarchoice==buffermin_upp:
                    minim=FwdU
                else:
                    minim==FwdS
           
  
            
        #If position is not top/bottom, aka normal run
        #Check for equals and activate radar if nedded
        else:
            if FwdU == FwdS: 
                radarchoice=min(buffermin_upp, buffermin_fwd )
                if radarchoice==buffermin_upp:
                    minim=FwdU
                else:
                    minim=min(FwdS, FwdD)

            if FwdU == FwdD:
                radarchoice=min(buffermin_upp, buffermin_dwn )
                if radarchoice==buffermin_upp:
                    minim=FwdU
                else:
                    minim=min(FwdD, FwdS)

            if FwdD == FwdS:

                radarchoice=min(buffermin_dwn, buffermin_fwd )
                if radarchoice==buffermin_dwn:
                    minim=FwdD
                else:
                    minim=min(FwdS, FwdU)
            else:
                minim=min(FwdD, FwdS, FwdU)
                #temp=[FwdS, FwdD, FwdU]
                #minim=median(temp)
                
                ################


        #FwdUpp
        if FwdU == minim:
            if row <=0:
                costa+=abs(start[row][col] - FwdS)
                #print(costlist)
                return self.rec(start, row, col+1, path+[row], costa, buffer )
           
            else:
                costa+=abs(start[row][col] - FwdU)
                
                return self.rec(start, row-1, col+1, path+[row], costa, buffer )


        #DownFwd
        #Test maxdrop check

        if FwdD == minim:


                if row >474:
                    costa+=abs(start[row][col] - FwdS)
                    return self.rec(start, row, col+1, path+[row],costa, buffer)
           
                elif row+1 <=0:
                    costa+=abs(start[row][col] - FwdS)
                    return self.rec(start, row, col+1, path+[row], costa, buffer )
            
                else:
                    costa+=abs(start[row][col] - FwdD)
                    return self.rec(start, row+1, col+1, path+[row], costa, buffer )
           


        #Fwd
        if FwdS == minim:
            #path.append(FwdS)
            costa+=abs(start[row][col] - FwdS)
            return self.rec(start, row, col+1, path+[row], costa, buffer)
            #print(path)                
        
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

