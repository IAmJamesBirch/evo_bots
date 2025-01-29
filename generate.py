import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("box.sdf")
for row in range(5):
	for col in range(5):
		x=row
		y=col
		z=0.5
		length=1
		width=1
		height=1
		for i in range(10):
			pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
			z+=height
			length *= 0.9
			width *= 0.9
			height *= 0.9
pyrosim.End()


