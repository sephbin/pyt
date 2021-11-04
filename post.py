import requests
import json
postob = {

"data": {
	"dimensions": {
		"width" : 1.203,
		"length" : 2.344,
		"height" : 33,
		"diameter" : None,
		"dynamicVariable" : None,
		"quantity" : None,
		"unit" : "m",
	},
	"weight": {
		"value" : 1000000,
		"unit" : "kg",
	},
	"cost" : {
		"value" : 1,
		"type" : "unit",
	},
	"type":"Ceiling Tile"
	},
"name": "imaginary",
"createdBy": "Andrew B"
}
post = requests.post("http://labs.cox.com.au/muninn_dev/api/uploadBuildingComponent/",
data = json.dumps(postob)
).text
print(post)