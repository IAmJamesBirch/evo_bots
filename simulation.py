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
	def __init__(self,directOrGUI,solutionID):
		self.directOrGUI = directOrGUI
		self.solutionID = solutionID
		if(directOrGUI == "DIRECT"):
			self.physicsClient = p.connect(p.DIRECT)
		else:
			self.physicsClient = p.connect(p.GUI)

		p.setAdditionalSearchPath(pybullet_data.getDataPath())
		p.setGravity(0,0,c.Gravity,self.physicsClient)
		self.world = WORLD()
		self.robot = ROBOT(self.solutionID)

	def Run(self):
		for i in range(0,c.Sim_Steps):
			p.stepSimulation()
			self.robot.Sense(i)
			self.robot.Think()
			self.robot.Act(i)
			if(self.directOrGUI == "GUI"):
				time.sleep(c.Step_Pause)
		#	print(i)

	def __del__(self):
		p.disconnect()

	def Get_Fitness(self):
		self.robot.Get_Fitness()
