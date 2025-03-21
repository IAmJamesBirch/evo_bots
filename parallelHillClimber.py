from solution import SOLUTION
import constants as c
import copy
import os

class PARALLEL_HILL_CLIMBER:

	def __init__(self):
		os.system("rm brain*.nndf")
		os.system("rm fitness*.txt")
		self.nextAvailableID = 0
		self.parents = {}
		for x in range(0,c.populationSize):
			self.parents[x] = SOLUTION(self.nextAvailableID)
			self.nextAvailableID += 1

	def Evolve(self):
		self.Evaluate(self.parents)
		for currentGeneration in range(0,c.numberOfGenerations):
			self.Evolve_For_One_Generation()

	def Evolve_For_One_Generation(self):
		self.Spawn()
		self.Mutate()
		self.Evaluate(self.children)
		self.Print()
		self.Select()
		
	def Spawn(self):
		self.children = {}
		for x in self.parents:
			self.children[x] = copy.deepcopy(self.parents[x])
			self.children[x].Set_ID(self.nextAvailableID)
			self.nextAvailableID += 1
		
	def Mutate(self):
		for x in self.children:
			self.children[x].Mutate()

	def Evaluate(self,solutions):
		for x in solutions:
			solutions[x].Start_Simulation("DIRECT")
		
		for x in solutions:
			solutions[x].Wait_For_Simulation_To_End()

	def Select(self):
		for x in self.parents:
			if(self.parents[x].fitness > self.children[x].fitness):
				self.parents[x] = self.children[x]

	def Print(self):
		print()
		print()
		for x in self.parents:
			print()
			print(f"Parent Fitness: {self.parents[x].fitness}, Child Fitness: {self.children[x].fitness}")
			print()
		print()
		
	def Show_Best(self):
		bestF = 100
		bestP = self.parents[0]
		for x in self.parents:
			if(self.parents[x].fitness < bestF):
				bestF = self.parents[x].fitness
				bestP = self.parents[x]
		bestP.Start_Simulation("GUI")
		print(f"Best Parent Fitness: {bestF}")
