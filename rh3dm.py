from rhino3dm import *
import requests 

#Rhino file
file = "T:\\Personal Temp\\s-whamilton\\test.3dm"

#The file as a parameter
model = File3dm.Read(file)
#All of the objects in the file, this can be used later to write to the file or to querey
modelObs = model.Objects

#Example of Quereying the file
for obj in modelObs:
	geometry = obj.Geometry
	bbox = geometry.GetBoundingBox()
	# print("{​​​​​​​}​​​​​​​, {​​​​​​​}​​​​​​​".format(bbox.Min, bbox.Max))
#Example of writing an object to the file
#Creating a geometry
ball = Sphere(Point3d(0,0,0),1000)
#Adding the geometry to the list of model objects
modelObs.AddSphere(ball)
f = Font("hello")
# f.IsEngravingFont = True

# modelObs.Add(f)
modelObs.AddCurve(f)

#Saving the file
model.Write(file,0)


