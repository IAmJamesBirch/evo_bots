
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
		#pyrosim.Prepare_To_Simulate(self.robot.robotId)
		#ROBOT.Prepare_To_Sense()
	def Run(self):
		for i in range(0,c.Sim_Steps):
			p.stepSimulation()
			ROBOT.Sense(self.robot,i)
			ROBOT.Act(self.robot,i)
		#       backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
		#       frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
		#       
		#	pyrosim.Set_Motor_For_Joint(
		#       bodyIndex = robotId,
		#       jointName = b'Torso_BackLeg',
		#       controlMode = p.POSITION_CONTROL,
		#       targetPosition = targetAnglesBack[i],
		#       maxForce = c.Max_Force)
		#       pyrosim.Set_Motor_For_Joint(
		#       bodyIndex = robotId,
		#       jointName = b'Torso_FrontLeg',
		#       controlMode = p.POSITION_CONTROL,
		#       targetPosition = targetAnglesFront[i],
		#       maxForce = c.Max_Force)
			time.sleep(c.Step_Pause)
		#	print(i)
	def __del__(self):
		p.disconnect()
