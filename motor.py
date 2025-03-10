import constants as c
import numpy
import pyrosim.pyrosim as pyrosim
import pybullet as p
import time
import pybullet_data


class MOTOR:
	def __init__(self,jointName):
		self.jointName = jointName
		#print(self.jointName)
		self.Prepare_To_Act()
	
	def Prepare_To_Act(self):
		self.amplitude = c.AmplitudeFront
		if(self.jointName == b'Torso_BackLeg'):
			self.frequency = c.FrequencyFront
		else:
			self.frequency = 0.5 * c.FrequencyFront
		#print(self.frequency)
		self.offset = c.PhaseOffsetFront
		self.motorValues = self.amplitude * numpy.sin(self.frequency * (self.offset + numpy.linspace(c.Theta_Min,c.Theta_Max,c.Sim_Steps)))
	
	def Set_Value(self,robotId,desiredAngle):
		pyrosim.Set_Motor_For_Joint(bodyIndex = robotId,
			jointName = self.jointName,
			controlMode = p.POSITION_CONTROL,
			targetPosition = desiredAngle,
			maxForce = c.Max_Force)
	
	def Save_Values(self):
		filename = "/Users/jamesbirch/cs3060/data/" + self.jointName + "motor.npy"
		numpy.save(filename,self.motorValues)
