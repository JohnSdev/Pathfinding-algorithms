
import pygame
from pygame.base import*
import sys
import random
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

from map import Map
from visualiser import Visualiser
from pathfinder import Pathfinder


map = Map()
map.loadData()

visualiser = Visualiser( "Inlupp 2 - Visualiser", map.getWidth(), map.getHeight() )
visualiser.setMap( map )

pathfinder = Pathfinder( visualiser, map )
pathfinder.findCheapestPath()
#pathfinder.minCost()
visualiser.runLoop()




