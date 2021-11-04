import clr

import sys
sys.path.append('C:\Program Files (x86)\IronPython 2.7\Lib')
import json
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
log = []
#The inputs to this node will be stored as a list in the IN variables.
in1 = IN[0]
in1 = json.loads(in1)

obarray = []
for i in in1:
	obarray.append(json.dumps(i['properties']))

OUT = obarray