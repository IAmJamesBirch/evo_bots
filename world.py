
import random
import numpy
import pyrosim.pyrosim as pyrosim
import pybullet as p
import time
import pybullet_data
import constants as c

class WORLD:
	def __init__(self):
		p.loadSDF("/Users/jamesbirch/cs3060/world.sdf")
		self.planeId = p.loadURDF("plane.urdf") 

