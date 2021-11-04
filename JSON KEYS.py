import clr

import sys
sys.path.append('C:\Program Files (x86)\IronPython 2.7\Lib')
import json
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
log = []
#The inputs to this node will be stored as a list in the IN variables.
in1 = IN[0]
in2 = []
for item in in1:
	item = json.loads(item)
	in2.append(item)
#in1 = json.loads(in1)
obarray = []
for a in in2:
	aarray=[]
	for i in a:
		aarray.append(str(i))
	obarray.append(aarray)

OUT = obarray