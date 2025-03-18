
import random
import numpy
import pyrosim.pyrosim as pyrosim
import pybullet as p
import time
import pybullet_data

#world setup
Sim_Steps = 1000
Gravity = -9.8
Step_Pause = 1/1000

#target angle stuff
AmplitudeFront = numpy.pi/4
AmplitudeBack = numpy.pi/4
FrequencyFront = 11
FrequencyBack = 10
PhaseOffsetFront = 0
PhaseOffsetBack = 0
Theta_Min= 0
Theta_Max= 2*numpy.pi

#motor
Max_Force = 50

#evolution
numberOfGenerations = 10
