import rhino3dm as rh
wZero = rh.Point3d(0,0,0)
hex = rh.Circle(wZero,1)
print(dir(hex))
hexLength = hex.Circumference
print(hexLength)

print(hex.PointAt(0.5*hexLength))

hex.ToNurbsCurve().