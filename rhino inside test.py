import rhinoinside
rhinoinside.load()
import System
import Rhino as rh

# for now, you need to explicitly use floating point
# numbers in Point3d constructor
pts = System.Collections.Generic.List[rh.Geometry.Point3d]()
pts.Add(rh.Geometry.Point3d(0.0,0.0,0.0))
pts.Add(rh.Geometry.Point3d(1.0,0.0,0.0))
pts.Add(rh.Geometry.Point3d(1.5,2.0,0.0))

crv = rh.Geometry.Curve.CreateInterpolatedCurve(pts,3)
print (crv.GetLength())

print(dir(rh.Geometry))