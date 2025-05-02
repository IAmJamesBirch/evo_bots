import os
import random
import pyrosim.pyrosim as pyrosim
import time
import numpy
import constants as c

class SOLUTION:

	def __init__(self,nextAvailableID):
		self.weights0 = numpy.random.rand(c.numSensorNeurons,c.numHiddenNeurons)
		self.weights0 = self.weights0 * 2 - 1
		
		self.weights1 = numpy.random.rand(c.numHiddenNeurons,c.numMotorNeurons)
		self.weights1= self.weights1 * 2 - 1
		
		self.weightsS = numpy.random.rand(c.numHiddenNeurons,c.numHiddenNeurons)
		self.weightsS = self.weightsS * 2 - 1

		self.myID = nextAvailableID

	def Evaluate(self,directOrGUI):
		pass

	def Start_Simulation(self,directOrGUI):
		self.Create_World()
		self.Create_Body()
		self.Create_Brain()
		os.system("python3 simulate.py " + directOrGUI + " " +  str(self.myID) + " 2&>1 &")

	def Wait_For_Simulation_To_End(self):
		filename = "fitness" + str(self.myID) + ".txt"
		while not os.path.exists(filename):
			time.sleep(0.01)
		file = open(filename, "r")
		self.fitness = float(file.readline())
		#print(self.fitness)
		file.close()
		os.system("rm " + filename)

	def Create_World(self):
			pyrosim.Start_SDF("world.sdf")
			#pyrosim.Send_Cube(name="Box", pos=[3,3,0.5] , size=[1,1,1])
			pyrosim.End()

	def Create_Body(self):
			pyrosim.Start_URDF("body.urdf")
			pyrosim.Send_Cube(name="Torso", pos=[0,0,1] , size=[1,1,1])
			pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [0,-0.5,1], jointAxis = "1 0 0")
			pyrosim.Send_Cube(name="BackLeg", pos=[0,-0.5,0] , size=[0.2,1,0.2])
			pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0,0.5,1], jointAxis = "1 0 0")
			pyrosim.Send_Cube(name="FrontLeg", pos=[0,0.5,0] , size=[0.2,1,0.2])
			pyrosim.Send_Joint( name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" , type = "revolute", position = [-0.5,0,1], jointAxis = "0 1 0")
			pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5,0,0] , size=[1,0.2,0.2])
			pyrosim.Send_Joint( name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" , type = "revolute", position = [0.5,0,1], jointAxis = "0 1 0")
			pyrosim.Send_Cube(name="RightLeg", pos=[0.5,0,0] , size=[1,0.2,0.2])
			pyrosim.Send_Joint( name = "BackLeg_LowerBackLeg" , parent= "BackLeg" , child = "LowerBackLeg" , type = "revolute", position = [0,-1,0], jointAxis = "1 0 0")
			pyrosim.Send_Cube(name="LowerBackLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])
			pyrosim.Send_Joint( name = "FrontLeg_LowerFrontLeg" , parent= "FrontLeg" , child = "LowerFrontLeg" , type = "revolute", position = [0,1,0], jointAxis = "1 0 0")
			pyrosim.Send_Cube(name="LowerFrontLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])
			pyrosim.Send_Joint( name = "LeftLeg_LowerLeftLeg" , parent= "LeftLeg" , child = "LowerLeftLeg" , type = "revolute", position = [-1,0,0], jointAxis = "0 1 0")
			pyrosim.Send_Cube(name="LowerLeftLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])
			pyrosim.Send_Joint( name = "RightLeg_LowerRightLeg" , parent= "RightLeg" , child = "LowerRightLeg" , type = "revolute", position = [1,0,0], jointAxis = "0 1 0")
			pyrosim.Send_Cube(name="LowerRightLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])
			pyrosim.End()	
			#exit()

	def Create_Brain(self):##edited to be og version right now ## make recurrent/self synapses be first?
			pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
			links = []
			for linkName in pyrosim.linkNamesToIndices:
					links.append(linkName)
			joints = {}
			for x in range(c.numMotorNeurons//2):
					joints[x] = links[0] + "_" + links[x+1]

			for x in range(c.numMotorNeurons//2):
					joints[x + c.numMotorNeurons//2] = links[x+ 1] + "_" + links[x+c.numMotorNeurons//2+1]

			#print(joints)
			#exit()
			#will need to use pyrosim.jointNamesToIndices and pyrosim.linkNamesToIndices, they are ordered by creation in above function^^, loops may be in robot.py

			for x in range(0,c.numSensorNeurons):
				pyrosim.Send_Sensor_Neuron(name = x , linkName = links[x + 1 + c.numSensorNeurons])
			##simple version code##
			#for x in range(0,c.numSensorNeurons):
			# 	pyrosim.Send_Sensor_Neuron(name = x , linkName = links[x + 1 + c.numSensorNeurons])

			for x in range(c.numSensorNeurons,c.numSensorNeurons + c.numHiddenNeurons):
				pyrosim.Send_Hidden_Neuron( name = x )

			for x in range(0,c.numMotorNeurons):
 			 	pyrosim.Send_Motor_Neuron( name = x + c.numSensorNeurons + c.numHiddenNeurons , jointName = joints[x])
			##simple version code##
			#for x in range(0,c.numMotorNeurons):
 			# 	pyrosim.Send_Motor_Neuron( name = x + c.numSensorNeurons, jointName = joints[x])

			#self and reccurent connections for Hidden layer only
			for currentRow in range(c.numSensorNeurons,c.numSensorNeurons + c.numHiddenNeurons):
				for currentColumn in range(c.numSensorNeurons,c.numSensorNeurons + c.numHiddenNeurons):
			 		pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn, weight = self.weightsS[currentRow - c.numSensorNeurons][currentColumn - c.numSensorNeurons ])

			for currentRow in range(0,c.numSensorNeurons):
			 		for currentColumn in range(0,c.numHiddenNeurons):
			 				pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn + c.numSensorNeurons , weight = self.weights0[currentRow][currentColumn])
			##simple version code##
			#for currentRow in range(0,c.numSensorNeurons):
			#	for currentColumn in range(c.numMotorNeurons):
			#		pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn + c.numSensorNeurons, weight = self.weights1[currentRow][currentColumn])

			for currentRow in range(0,c.numHiddenNeurons):
				for currentColumn in range(0,c.numMotorNeurons):
			 			pyrosim.Send_Synapse( sourceNeuronName = currentRow + c.numSensorNeurons , targetNeuronName = currentColumn + c.numSensorNeurons + c.numHiddenNeurons , weight = self.weights1[currentRow][currentColumn])
			
			


			pyrosim.End()
			#exit()


	def Mutate(self):
		randomRow0 = random.randint(0,c.numSensorNeurons - 1)
		randomColumn0 = random.randint(0,c.numHiddenNeurons - 1)
		self.weights0[randomRow0,randomColumn0] = random.random() * 2 - 1

		randomRow1 = random.randint(0,c.numHiddenNeurons - 1)
		randomColumn1 = random.randint(0,c.numMotorNeurons - 1)
		self.weights1[randomRow1,randomColumn1] = random.random() * 2 - 1

		randomRowR = random.randint(0,c.numHiddenNeurons - 1)
		randomColumnR = random.randint(0,c.numHiddenNeurons - 1)
		self.weightsS[randomRowR][randomColumnR] = random.random() * 2 -1
		
	def Set_ID(self,num):
		self.myID = num
