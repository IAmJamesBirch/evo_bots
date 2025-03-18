
import random
import numpy
import pyrosim.pyrosim as pyrosim
import pybullet as p
import time
import pybullet_data
from pyrosim.neuralNetwork import NEURAL_NETWORK
import constants as c
from sensor import SENSOR
from motor import MOTOR

class ROBOT:
	def __init__(self):
		self.robotId = p.loadURDF("body.urdf")
		pyrosim.Prepare_To_Simulate(self.robotId)
		self.Prepare_To_Sense()
		self.Prepare_To_Act() 
		self.nn = NEURAL_NETWORK("brain.nndf")
	
	def Prepare_To_Sense(self):
		self.sensors = {}
		for linkName in pyrosim.linkNamesToIndices:
			self.sensors[linkName] = SENSOR(linkName)
	
	def Sense(self,t):
		for key in self.sensors:
			self.sensors[key].Get_Value(t)
	
	def Prepare_To_Act(self):
		self.motors = {}
		for jointName in pyrosim.jointNamesToIndices:
			self.motors[jointName] = MOTOR(jointName)
	
	def Act(self,t):
		for neuronName in self.nn.Get_Neuron_Names():
			if self.nn.Is_Motor_Neuron(neuronName):
				jointName = self.nn.Get_Motor_Neurons_Joint(neuronName).encode("utf-8")
				desiredAngle = self.nn.Get_Value_Of(neuronName)
				self.motors[jointName].Set_Value(self.robotId,desiredAngle)
#				#print(neuronName,jointName,desiredAngle)
#		for key in self.motors:
#			self.motors[key].Set_Value(self.robotId,t)
	
	def Think(self):
		self.nn.Update()
		#self.nn.Print()

	def Get_Fitness(self):
		stateOfLinkZero = p.getLinkState(self.robotId,0)
		positionOfLinkZero = stateOfLinkZero[0]
		xCoordinateOfLinkZero = positionOfLinkZero[0]
		#print(xCoordinateOfLinkZero)
		file = open("fitness.txt","w")
		file.write(str(xCoordinateOfLinkZero))
		file.close()
		exit()
		
