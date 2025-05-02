import numpy
import matplotlib.pyplot
import constants as c

fitnessvalsA = numpy.load('fitnessvalsA.npy')
fitnessvalsB = numpy.load('fitnessvalsB.npy')


avgfitnessvalsA = fitnessvalsA.mean(axis=0)
avgfitnessvalsB = fitnessvalsB.mean(axis=0)
#print(avgfitnessvalsA)
stdfitnessvalsA = fitnessvalsA.std(axis=0)
stdfitnessvalsB = fitnessvalsB.std(axis=0)
print(stdfitnessvalsA)
#for x in range(c.populationSize):
#    matplotlib.pyplot.plot(fitnessvalsA[x,:], linewidth=1,label=f"{x}")
matplotlib.pyplot.plot(avgfitnessvalsA, linewidth=4,label="Aavg")
matplotlib.pyplot.plot(avgfitnessvalsA + stdfitnessvalsA, linewidth=4,label="Aavg+std")
matplotlib.pyplot.plot(avgfitnessvalsA - stdfitnessvalsA, linewidth=4,label="Aavg-std")
matplotlib.pyplot.plot(avgfitnessvalsB, linewidth=2,label="Bavg")
matplotlib.pyplot.plot(avgfitnessvalsB + stdfitnessvalsB, linewidth=2,label="Bavg+std")
matplotlib.pyplot.plot(avgfitnessvalsB - stdfitnessvalsB, linewidth=2,label="Bavg-std")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()