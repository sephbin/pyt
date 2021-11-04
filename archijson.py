import rhinoscriptsyntax as rs
import Rhino as r
import Grasshopper as g
import json
log = []
def Point(geom,prop=None):
    pt = rs.coerce3dpoint(geom)
    pt = [pt[0],pt[1],pt[2]]
    if prop:
        pt = {"geometry":{'coordinates':pt, 'type': 'point'}}
        pt['properties'] = json.loads(prop)
        return pt
    else:
        return pt
def convertToRPT (geom):
    pt = r.Geometry.Point3d(geom[0],geom[1],geom[2])
    return pt
def PointCollection(geom,prop=None):
    t = geom
    pts = map(lambda g: Point(g), t)
    crv = {"geometry":{'coordinates':pts, 'type': 'pointcollection'}}
    if prop:
        crv['properties'] = json.loads(prop)
    print(crv)
    return crv
def Plane(geom,prop=None):
    pln = {"geometry":{'coordinates':[geom.XAxis.X,geom.YAxis.X,geom.ZAxis.X,geom.OriginX,geom.XAxis.Y,geom.YAxis.Y,geom.ZAxis.Y,geom.OriginY,geom.XAxis.Z,geom.YAxis.Z,geom.ZAxis.Z,geom.OriginZ,0,0,0,1], 'type': 'xform'}}
    if prop:
        pln['properties'] = json.loads(prop)
    return pln
def Curve(geom,prop=None):
    t = rs.CurvePoints(geom)
    tc = rs.ClosedCurveOrientation(geom)
    if tc == 0: tc = False
    else: tc = True
    tdeg = rs.CurveDegree(geom)
    tcPo = len(t)
    print("tdeg: "+str(tdeg))
    print("tcPo: "+str(tcPo))
    pts = map(lambda g: Point(g), t)
    crv = {"geometry":{'coordinates':pts, 'type': 'polyline','closed':tc}}
    if tdeg == 1 and tc  : del crv['geometry']['coordinates'][-1]
    if tdeg == 1 and tcPo == 2  : crv['geometry']['type']='line'
    if tdeg >= 2                : crv['geometry']['type']='spline'
    if tdeg == 2 and tcPo == 5  :
        arc = rs.AddArc3Pt(pts[0],pts[4],pts[2])
        pt0 = convertToRPT(pts[0])
        pt2 = convertToRPT(pts[2])
        pt4 = convertToRPT(pts[4])
        arc = r.Geometry.Arc(startPoint = pt0, pointOnInterior = pt2, endPoint = pt4)
        crv['geometry']['type']='arc'
        print(crv['geometry']['coordinates'])
        del crv['geometry']['coordinates'][3]
        del crv['geometry']['coordinates'][1]
    if prop:
        crv['properties'] = json.loads(prop)
    print(crv)
    return crv
otype = {"0": "Unknown object", "1": Point, "2": "PointCloud", "3":PointCollection, "4": Curve, "5":Plane, "8": "Surface", "16": "Polysurface", "32": "Mesh", "256": "Light", "512": "Annotation", "4096": "Instance reference", "8192": "Text dot", "16384": "Grip", "32768": "Detail", "65536": "Hatch", "131072": "Morph control", "134217728": "Cage", "268435456": "Phantom", "536870912": "Clipping plane", "1073741824": "Extrusion"}
def Convert(geom,prop):
    print("START CONVERT")
    print(geom)
    ot = otype["1"]
    try:
        ot = otype[str(rs.ObjectType(geom))]
    except:
        #ot = otype[type(geom)]
        othertype = str(type(geom))
        print(othertype)
        if othertype == "<type 'List[object]'>":
            ot = otype["3"]
        if othertype == "<type 'Plane'>":
            ot = otype["5"]
    if T == 0:
        return(ot(geom,prop))
    if T == 1:
        return(json.dumps((ot(geom,prop))))
O = map(lambda g,p: Convert(g,p), G,P)
L = log