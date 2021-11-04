import clr

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
import sys
sys.path.append('C:\Program Files (x86)\IronPython 2.7\Lib')
import json
import os
import urllib
import urllib2
import httplib

in0 = IN[0]
in1 = IN[1]
in2 = IN[2]
in3 = IN[3]
in4 = IN[4]
delununsed = IN[5]
log = []
send = IN[6]
OUTOB = []

try:
	url = 'http://labs.cox.com.au/bd/rooms.json/?search=218142.00'
	posturl = 'http://labs.cox.com.au/bd/capi/rooms/'
	#url = 'http://jsonplaceholder.typicode.com/posts'
	#log.append(url)

	test = in0
	testid = in1
	rlist = []
	for r,eid, lcb, coords in zip(test,testid, in3, in4):
		room  = {
		"project_number":in2[0],
		"element_id":eid,
		"room_name": r.GetParameterValueByName("Name"),
		"room_type_text": r.GetParameterValueByName("Name")
		}
		params = r.Parameters
		data = {}
		data["LastChangedBy"] = lcb 
		data["Coordinates"] = coords
		for p in params:
			t = type(p.Value)
			log.append(p.Name.ToString())
			if t == type("") or t == type(1) or t == type(1.1) or t == type(True):
				if p.Name.ToString() in send:
					data[p.Name.ToString()] = p.Value
		room["data"] = data
		rlist.append(room)


	###POST
	try:
		postdata = {
		'data' : json.dumps(rlist)
		}
		if delununsed:
			postdata['bulktype'] = 'deleteunused'
			
		data = urllib.urlencode(postdata)
		req = urllib2.Request(posturl, data)
		response = urllib2.urlopen(req)
		jresponse = json.loads(response.read())
		log.append(jresponse)
	except Exception as e:
		log.append(str(e))



	###GET
	#try:
	#	req = urllib2.Request(url)
	#	response = urllib2.urlopen(req)
	#	the_page = response.read()
	#	log.append(the_page)
	#
	#except Exception as e:
	#	log.append(str(e))




#OUT = OUTOB
except Exception as e:
	exc_type, exc_obj, exc_tb = sys.exc_info()
	other = sys.exc_info()[0].__name__
	fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
	errorType = str(exc_type)
	log.append({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno})

file = open("C:\\Temp\\dynamo_log.log","w")
file.write(json.dumps(log, indent=4, sort_keys=True))
file.close()
OUT = True