
import pygame
from pygame.base import*
import sys
import random
import time


from map import Map
from visualiser import Visualiser
from pathfinder import Pathfinder


map = Map()
map.loadData()

visualiser = Visualiser( "Inlupp 2 - Visualiser", map.getWidth(), map.getHeight() )
visualiser.setMap( map )

pathfinder = Pathfinder( visualiser, map )
tstart = time.time()
pathfinder.findCheapestPath()
tstop=time.time()
print("Pathfinder took {:.3f}s".format( tstop-tstart ) )
#pathfinder.minCost()
visualiser.runLoop()


