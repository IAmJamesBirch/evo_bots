import sys
import random
import numpy
import pyrosim.pyrosim as pyrosim
import pybullet as p
import time
import pybullet_data
import constants as c
from simulation import SIMULATION

directOrGUI = sys.argv[1]
simulation = SIMULATION(directOrGUI)
simulation.Run()
simulation.Get_Fitness()

