
import random
import numpy
import pyrosim.pyrosim as pyrosim
import pybullet as p
import time
import pybullet_data
import constants as c
from world import WORLD
from robot import ROBOT

class SIMULATION:
	def __init__(self):
		self.physicsClient = p.connect(p.GUI)
		p.setAdditionalSearchPath(pybullet_data.getDataPath())
		p.setGravity(0,0,c.Gravity,self.physicsClient)
		self.world = WORLD()
		self.robot = ROBOT()

	def Run(self):
		for i in range(0,c.Sim_Steps):
			p.stepSimulation()
			ROBOT.Sense(self.robot,i)
			ROBOT.Think(self.robot)
			ROBOT.Act(self.robot,i)
		#	time.sleep(c.Step_Pause)
		#	print(i)

	def __del__(self):
		p.disconnect()
