import numpy
import pyrosim.pyrosim as pyrosim
import constants as c

class SENSOR:
	def __init__(self,linkName):
		self.linkName = linkName
		self.values = numpy.zeros(c.Sim_Steps)
		#print(self.values)			
	
	def Get_Value(self,t):
		self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
		if(t == c.Sim_Steps - 1):
			print(self.values)
	
	def Save_Values(self):
		filename = "/Users/jamesbirch/cs3060/data/" + self.linkName + "sensor.npy"
		numpy.save(filename,self.values)
