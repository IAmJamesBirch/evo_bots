import os
import numpy
from parallelHillClimber import PARALLEL_HILL_CLIMBER

phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.Show_Best()
print(phc.data)
filename = "/Users/jamesbirch/cs3060/fitnessvalsB.npy"
numpy.save(filename,phc.data)