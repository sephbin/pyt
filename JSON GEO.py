import clr

import sys
sys.path.append('C:\Program Files (x86)\IronPython 2.7\Lib')
import json
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
import inspect
log = []
#The inputs to this node will be stored as a list in the IN variables.
in1 = IN[0]
in1 = [json.loads(in1)]
array = []
def featurecollection(o):
    for i in o["features"]:
        fCall = function_mappings[i['geometry']['type']]
        props = {}
        try:
            props = i['properties']
        except:
            pass
        obarray.append(fCall(i['geometry'],props))
def feature(o):
	pass
def point(array):
	log.append("pt")
	log.append(str(array))
	log.append(str(type(array)))
	if str(type(array)) == "<type 'list'>":
		pt = Point.ByCoordinates(float(array[0]),float(array[1]),float(array[2]))
	if str(type(array)) == "<type 'dict'>":
		pt = Point.ByCoordinates(float(array['coordinates'][0]),float(array['coordinates'][1]),float(array['coordinates'][2]))
	return pt
def pointcollection(o, prop = None):
	parray = []
	for p in o['coordinates']:
		pt = point(p)
		parray.append(pt)
	return parray	
def polyline(o,prop = None):
	log.append("polyline")
	log.append(str(o))
	polarray = []
	for p in o['coordinates']:
		pt = point(p)
		polarray.append(pt)
	pline = Polygon.ByPoints(polarray)
	#pline = NurbsCurve.ByControlPoints(polarray,1,o['properties']['closed'])
	return pline
def line(o,prop = None):
	log.append("line")
	log.append(str(o))
	lineconstruct = Line.ByStartPointEndPoint(point(o['coordinates'][0]),point(o['coordinates'][1]))
	return lineconstruct

def spline(o,prop = None):
	log.append("spline")
	log.append(str(o))
	polarray = []
	for p in o['coordinates']:
		pt = point(p)
		polarray.append(pt)
	try:
		cspline = NurbsCurve.ByPoints(polarray)
		#pline = NurbsCurve.ByControlPoints(polarray,1,o['properties']['closed'])
		return cspline
	except Exception as e:
		log.append(e)
		pass

def profile(o,prop = None):
	log.append("profile")
	log.append(str(o))
	profileconstruct = []
	for segment in o:
		fCall = function_mappings[segment['type']]
		profileconstruct.append(fCall(segment))
	try:
		profilecurve = PolyCurve.ByJoinedCurves(profileconstruct)
		return profilecurve
	except Exception as e:
		log.append(e)
		pass

def loft(o,prop = None):
	try:
		log.append("loft")
		log.append(str(o))
		curveArray = []	
		log.append("START LOOP")
		for curve in o['coordinates']:
			fCall = function_mappings[curve['type']]
			log.append(str(fCall))
			curveArray.append(fCall(curve['coordinates']))
		#Loft = Solid.ByLoft(curveArray)
		return curveArray
	except Exception as e:
		log.append(e)
		pass

function_mappings = {
		'FeatureCollection':featurecollection,
        'Feature': feature,
        'point': point,
        'pointcollection': pointcollection,
        'polyline': polyline,
        'line': line,
        'loft': loft,
        'profile' : profile,
        'spline' : spline
}
obarray = []
for i in in1:
    if i["type"]:
        fCall = function_mappings[i['type']]
        fCall(i)
    else:
        fCall = function_mappings[i['geometry']['type']]
        obarray.append(fCall(i['geometry']))

#OUT = log
OUT = obarray