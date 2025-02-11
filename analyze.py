import matplotlib.pyplot
import numpy

backLegSensorValues = numpy.load("data/backlegsensor.npy")
frontLegSensorValues = numpy.load("data/frontlegsensor.npy")
#print(backLegSensorValues)
matplotlib.pyplot.plot(backLegSensorValues,linewidth=4,label="back")
matplotlib.pyplot.plot(frontLegSensorValues,label="front")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
