
import matplotlib.pyplot
import numpy

backLegSensorValues = numpy.load("data/backlegsensor.npy")
frontLegSensorValues = numpy.load("data/frontlegsensor.npy")
targetAnglesFront = numpy.load("data/targetAnglesFront.npy")
targetAnglesBack = numpy.load("data/targetAnglesBack.npy")

#print(backLegSensorValues)
#matplotlib.pyplot.plot(backLegSensorValues,linewidth=4,label="back")
#matplotlib.pyplot.plot(frontLegSensorValues,label="front")
matplotlib.pyplot.plot(targetAnglesFront, linewidth=4,label="front")
matplotlib.pyplot.plot(targetAnglesBack,label="back")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
