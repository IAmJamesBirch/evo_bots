
import random
import numpy
import pyrosim.pyrosim as pyrosim
import pybullet as p
import time
import pybullet_data

amplitudeFront = numpy.pi/4
amplitudeBack = numpy.pi/4
frequencyFront = 11
frequencyBack = 10
phaseOffsetFront = 0
phaseOffsetBack = 0
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8,physicsClient)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)
targetAnglesFront = amplitudeFront *  numpy.sin(frequencyFront*(phaseOffsetFront +  numpy.linspace(0,2*numpy.pi,1000)))
targetAnglesBack  = amplitudeBack *  numpy.sin(frequencyBack*(phaseOffsetBack +  numpy.linspace(0,2*numpy.pi,1000)))
numpy.save("/Users/jamesbirch/cs3060/data/targetAnglesFront.npy",targetAnglesFront)
numpy.save("/Users/jamesbirch/cs3060/data/targetAnglesBack.npy",targetAnglesBack)
for i in range(0,1000):
	p.stepSimulation()
	backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
	frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
	pyrosim.Set_Motor_For_Joint(
	bodyIndex = robotId,
	jointName = b'Torso_BackLeg',
	controlMode = p.POSITION_CONTROL,
	targetPosition = targetAnglesBack[i],
	maxForce = 50)
	pyrosim.Set_Motor_For_Joint(
	bodyIndex = robotId,
	jointName = b'Torso_FrontLeg',
	controlMode = p.POSITION_CONTROL,
	targetPosition = targetAnglesFront[i],
	maxForce = 50)	
	time.sleep(1/1000)
	#print(i)
p.disconnect()
#print(backLegSensorValues)
numpy.save("/Users/jamesbirch/cs3060/data/backlegsensor.npy",backLegSensorValues)
numpy.save("/Users/jamesbirch/cs3060/data/frontlegsensor.npy",frontLegSensorValues)

