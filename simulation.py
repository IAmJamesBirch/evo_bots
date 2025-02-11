import numpy
import pyrosim.pyrosim as pyrosim
import pybullet as p
import time
import pybullet_data

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8,physicsClient)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(100)
frontLegSensorValues = numpy.zeros(100)
for i in range(0,100):
	p.stepSimulation()
	backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
	frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
	time.sleep(1/60)
	#print(i)
p.disconnect()
#print(backLegSensorValues)
numpy.save("/Users/jamesbirch/cs3060/data/backlegsensor.npy",backLegSensorValues)
numpy.save("/Users/jamesbirch/cs3060/data/frontlegsensor.npy",frontLegSensorValues)

