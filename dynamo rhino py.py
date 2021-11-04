import clr
import json

# Import ToDSType(bool) extension method
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

# Import geometry conversion extension methods
clr.ImportExtensions(Revit.GeometryConversion)

# Import DocumentManager and TransactionManager
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
from System.Collections.Generic import *

# Import RevitAPI
clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *

import sys
import os

def errorLog(e, log=[]):
	exc_type, exc_obj, exc_tb = sys.exc_info()
	other = sys.exc_info()[0].__name__
	fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
	errorType = str(exc_type)
	try:
		errob = {"isError":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log}
	except:
		errob = {"isError":str(e)}
	return errob



try:

	roamingFolder = os.getenv('APPDATA')

	rhinoInsidePath = roamingFolder + r'\Autodesk\Revit\Addins\2020\RhinoInside.Revit'

	rhinoCommonPath = r'C:\Program Files\Rhino 7 WIP\System'

	sys.path.append(rhinoInsidePath)
	sys.path.append(rhinoCommonPath)

	clr.AddReference("RhinoInside.Revit")
	import RhinoInside
	from RhinoInside.Revit.Convert.Geometry import *

	clr.AddReference("RhinoCommon")
	import Rhino as rh
	doc = DocumentManager.Instance.CurrentDBDocument
	def coerceguid(id, raise_exception=False):
		if type(id) is System.Guid: return id
		if type(id) is str and len(id)>30:
			try:
				id = System.Guid(id)
				return id
			except:
				pass
		if (type(id) is list or type(id) is tuple) and len(id)==1:
			return coerceguid(id[0], raise_exception)
		if type(id) is Rhino.DocObjects.ObjRef: return id.ObjectId
		if isinstance(id,Rhino.DocObjects.RhinoObject): return id.Id
		if raise_exception: raise TypeError("Parameter must be a Guid or string representing a Guid")
	def __getlayer(name_or_id, raise_if_missing):
		if not name_or_id: raise TypeError("Parameter must be a string or Guid")
		id = coerceguid(name_or_id)
		if id:
			layer = scriptcontext.doc.Layers.FindId(id)
		else:
			name = name_or_id
			layer_index = scriptcontext.doc.Layers.FindByFullPath(name, UnsetIntIndex)
			if layer_index != UnsetIntIndex: return scriptcontext.doc.Layers[layer_index]
			layer = scriptcontext.doc.Layers.FindName(name)
		if layer: return layer
		if raise_if_missing: raise ValueError("%s does not exist in LayerTable" % name_or_id)
	def ObjectsByLayer(layer_name, select=False):
		"""Returns identifiers of all objects based on the objects' layer name
		Parameters:
			layer_name (str): name of the layer
			select (bool, optional): select the objects
		Returns:
			list(guid, ...): identifiers for objects in the specified layer
		Example:
			import rhinoscriptsyntax as rs
			obj = rs.GetObject("Pick any object")
			if obj:
				layer = rs.ObjectLayer(obj)
				rs.ObjectsByLayer(layer, True)
		See Also:
			
		"""
		layer = __getlayer(layer_name, True)
		rhino_objects = scriptcontext.doc.Objects.FindByLayer(layer)
		if not rhino_objects: return []
		if select:
			for rhobj in rhino_objects: rhobj.Select(True)
			scriptcontext.doc.Views.Redraw()
		return [rhobj.Id for rhobj in rhino_objects]
	def coercegeometry(id, raise_if_missing=False):
		"""attempt to get GeometryBase class from given input
		Parameters:
			id = geometry identifier
			raise_if_missing [opt] = True or False
		Example:
		See Also:
		"""
		if isinstance(id, Rhino.Geometry.GeometryBase): return id
		if type(id) is Rhino.DocObjects.ObjRef: return id.Geometry()
		if isinstance(id, Rhino.DocObjects.RhinoObject): return id.Geometry
		id = coerceguid(id, raise_if_missing)
		if id:
			rhobj = scriptcontext.doc.Objects.Find(id)
			if rhobj: return rhobj.Geometry
		if raise_if_missing: raise ValueError("unable to convert %s into geometry"%id)

	
	# import rhinoscriptsyntax as rs
	# import scriptcontext as sc

	a = None

	sc.doc = rh.RhinoDoc.ActiveDoc
	
	all_objs = []
	Ls = ["Default"]
	for layer in Ls:
		
		objs = rs.ObjectsByLayer(layer)
		if objs:
			#you need to get the geometry from IDs
			objs = [rs.coercegeometry(x) for x in objs]
			#if you want to use rs, then add to the current doc
			objs = [ghdoc.Objects.Add(x) for x in objs]
			all_objs.extend(objs)
			
	a = all_objs
	
	#sc.doc = ghdoc

	#Uncomment the line below to enable the first input
	#t = UnwrapElement(IN[0])

	# "Start" the transaction
	#TransactionManager.Instance.EnsureInTransaction(doc)

	# "End" the transaction
	#TransactionManager.Instance.TransactionTaskDone()

	#Uncomment the line below to output an object
	#OUT = t
	with open("D:\\Dropbox (COX Architecture)\\LOCAL TEMP\\errorlog.json","w") as f:
		json.dump(outob, f, sort_keys=True, indent=4)
except Exception as e:
	with open("D:\\Dropbox (COX Architecture)\\LOCAL TEMP\\errorlog.json","w") as f:
		json.dump(errorLog(e), f, sort_keys=True, indent=4)
	OUT = json.dumps(errorLog(e), sort_keys=True, indent=4