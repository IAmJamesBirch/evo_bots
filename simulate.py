import random
import numpy
import pyrosim.pyrosim as pyrosim
import pybullet as p
import time
import pybullet_data
import constants as c
from simulation import SIMULATION

simulation = SIMULATION()
SIMULATION.Run(simulation)

#for i in range(0,c.Sim_Steps):
#	p.stepSimulation()
#	backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
#	frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
#	pyrosim.Set_Motor_For_Joint(
#	bodyIndex = robotId,
#	jointName = b'Torso_BackLeg',
#	controlMode = p.POSITION_CONTROL,
#	targetPosition = targetAnglesBack[i],
#	maxForce = c.Max_Force)
#	pyrosim.Set_Motor_For_Joint(
#	bodyIndex = robotId,
#	jointName = b'Torso_FrontLeg',
#	controlMode = p.POSITION_CONTROL,
#	targetPosition = targetAnglesFront[i],
#	maxForce = c.Max_Force)	
#	time.sleep(c.Step_Pause)
#	#print(i)
#p.disconnect()
###print(backLegSensorValues)
#numpy.save("/Users/jamesbirch/cs3060/data/backlegsensor.npy",backLegSensorValues)
#numpy.save("/Users/jamesbirch/cs3060/data/frontlegsensor.npy",frontLegSensorValues)

