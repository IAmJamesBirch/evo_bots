import random
import numpy
import pyrosim.pyrosim as pyrosim
import pybullet as p
import time
import pybullet_data
import constants as c
from sensor import SENSOR
from motor import MOTOR

class ROBOT:
	def __init__(self):
		self.robotId = p.loadURDF("body.urdf")
		pyrosim.Prepare_To_Simulate(self.robotId)
		self.Prepare_To_Sense()
		self.Prepare_To_Act() 
		#self.targetAnglesFront = c.AmplitudeFront *  numpy.sin(c.FrequencyFront*(c.PhaseOffsetFront +  numpy.linspace(c.Theta_Min,c.Theta_Max,c.Sim_Steps)))
		#self.targetAnglesBack  = c.AmplitudeBack *  numpy.sin(c.FrequencyBack*(c.PhaseOffsetBack +  numpy.linspace(c.Theta_Min,c.Theta_Max,c.Sim_Steps))) 
		#numpy.save("/Users/jamesbirch/cs3060/data/targetAnglesFront.npy",self.targetAnglesFront)
		#numpy.save("/Users/jamesbirch/cs3060/data/targetAnglesBack.npy",self.targetAnglesBack)
	
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
		for key in self.motors:
			self.motors[key].Set_Value(self.robotId,t)
