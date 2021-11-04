import pprint
import random
pp = pprint.PrettyPrinter(indent=3, width=10, depth=10)

blank = {"name":"","race":"","occupation":"","status":"","id":"","connection":[], "attributes":{"stOffValue":0, "dxOffValue":0, "iqOffValue":0, "htOffValue":0, "hpOffValue":0, "willOffValue":0, "perOffValue":0, "fpOffValue":0, "bsOffValue":0}, "dr":{"headDR":"2", "groinDR":"0", "faceDR":"0", "eyeDR":"0", "neckDR":"0", "torsoDR":"0", "lArmDR":"0", "rArmDR":"0", "lHandDR":"0", "rHandDR":"0", "lLegDR":"0", "rLegDR":"0", "lFootDR":"0", "rFootDR":"0"}, "advantages":[], "disadvantages":[], "skills":[], "languages":[], "cultures":[], "reactions":{"appearance":"Standard", "status":"0", "reputations":[] }, "possessions":[], }
ob = {
  "scout": {
    "occupation": "Scout",
    "attributes": {
      "dxOffValue": 1,
      "htOffValue": 1
    },
    "advantages": [
      {"name": "Outdoorsman", "value": 1, "cost":10,"stack": 1 },
    ],
    "skills": [
      {"name": "Bow", "rank": "2"},
      {"name": "Camouflage", "rank": "2"},
      {"name": "Fast-Draw (Arrow)", "rank": "2"},
      {"name": "Observation", "rank": "2"},
      {"name": "Tracking", "rank": "4"}
    ],
    "choice": [{'type':'advantages','poolType':'cost','poolMax':15,'pool':[{"name": "Absolute Direction", "cost": 5, "stack": 0 },{"name": "Acute Vision", "value":1, "cost": 2, "stack": 1 },{"name": "Combat Reflexes", "cost": 15, "stack": 0 },{"name": "Danger Sense", "cost": 15, "stack": 0 },{"name": "Fit", "cost": 5, "stack": 0 },{"name": "Very Fit", "cost": 15, "stack": 0 },{"name": "High Pain Threshold", "cost": 10, "stack": 0 }, {"name": "Luck", 'value':1,"cost": 15, "stack": 0 },{"name": "Night Vision", "value":1, "cost": 1, "stack": 1 },{"name": "Outdoorsman", "value":1, "cost": 10, "stack": 1 },{"name": "Peripheral Vision", "cost": 15, "stack": 0 },{"name": "Signature Gear", "value":1,"cost": 1, "stack": 1 },{"name": "Weapon Bond", "cost": 1, "stack": 0 }
    	]}
    ]
  }
}
select = ob['scout']
operations = {'occupation':'conc','attributes':'nestAdd','advantages':'addisAdd','disadvantages':'addisAdd','skills':'skillAdd','choice':'chooseSomething'}
# Definitions
def conc(base,mod,key):
	base[key]=base[key]+mod[key]
def nestAdd(base,mod,key):
	for kM in mod[key]:
		base[key][kM] = base[key][kM]+mod[key][kM]
def addisAdd(base,mod,key):
	for kM in mod[key]:
		notfound = True
		if (kM['stack']):
			for kB in base[key]:
				if(kM['name']==kB['name']):
					kB['value']+=kM['value']
					kB['cost']+=kM['cost']
					notfound = False
		if(notfound):
			base[key].append(kM)
def skillAdd(base,mod,key):
	for kM in mod[key]:
			notfound = True
			for kB in base[key]:
				if(kM['name']==kB['name']):
					kB['rank']+=kM['rank']
					notfound = False
			if(notfound):
				base[key].append(kM)
def chooseSomething(base,mod,key):
	for choose in mod[key]:
		poolMax = choose['poolMax']
		pool = choose['pool']
		poolType = choose['poolType']
		defType = choose['type']
		choices = {defType:[]}
		# pp.pprint(pool)
		# print ('Starting to choose something...')
		while (poolMax>0):
			pool = removeTooMuch(pool,poolMax,poolType)
			selected = (random.sample(pool, 1)[0])
			if(selected['stack']==0):
				pool.remove(selected)
			choices[defType].append(selected)
			poolMax += (selected[poolType]*-1)
			# print selected
			# print poolMax
		# print choices
		for kC in choices:
			exec(operations[kC]+"(blank,choices,kC)")

#
def removeTooMuch(pool, poolMax, poolType):
	cleanArray = []
	for item in pool:
		# print ('\titem: '+ str(item))
		if (item[poolType]<=poolMax):
			# print ('\t\tadding: '+ str(item))
			cleanArray.append(item)
	return cleanArray


# 
for k in select:
	exec(operations[k]+"(blank,select,k)")
# 
pp.pprint(blank)

cost = 0
for adv in blank['advantages']:
	cost += adv['cost']
print cost
