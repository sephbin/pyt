data = [{"id":"C2.6","name":"Security Risk Assessment","conditions":[{"id":"a","condition":"The Contractor must undertake a Security Risk Assessment (SRA), in consultation with the Principal, SCGT, Emergency Services, and other Stakeholders nominated by the Principal. The SRA must be used to inform and confirm the design of the;","subconditions":[{"id":"i","condition":"Hostile Vehicle Mitigation (HVM) as detailed in Clause D2.4.11"},{"id":"ii","condition":"Security Office as detailed in Clause D12.4.1"},{"id":"iii","condition":"Security Systems as detailed in Chapter F17 (Security Systems)"}]},{"id":"b","condition":"The SRA must be undertaken in accordance with the methodology and guidance in the international standard Risk Management – Guidelines (ISO 31000:2018) and Handbook 167:2006 Security Risk Management, and must calculate the “likelihood” (informed by an assessment of threat and vulnerability) and “consequence” of credible security risks."},{"id":"c","condition":"The SRA must employ a risk matrix that is tailored for the assessment and rating of security risks."}]}]

tabs = ""
def log(text):
	t = text
	if type(text) == type([]):
		t = "\t".join(text)
	print(tabs+str(t))

for sec in data:
	log([sec['id'],sec['name']])
	for cons in sec['conditions']:
		tabs = "\t"
		log([cons['id'], cons['condition']])
		try:
			for scons in cons['subconditions']:
				tabs = "\t\t"
				log([scons['id'], scons['condition']])
		except:
			pass
