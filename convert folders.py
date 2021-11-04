lut = {
	"5.1" : "5.1 Preliminary",
	"5.2" : "5.2 Primary",
	"5.3" : "5.3 Secondary",
	"5.4" : "5.4 Specialist",
}

l = ["5.1.1 Architect (other)",
"5.1.6 Quantity Surveyor",
"5.1.7 Surveyor",
"5.2.2 Structural",
"5.2.3 Mechanical",
"5.2.4 Electrical & Comms",
"5.2.5 Hydraulics",
"5.2.6 Fire Services",
"5.2.7 Vertical Transport",
"5.2.8 Façade",
"5.2.9 Landscape",
"5.3.1 Access",
"5.3.2 Acoustic",
"5.3.3 BCA Advisor",
"5.3.5 Fire Engineer",
"5.3.6 Heritage",
"5.4.1 Creative Media & Model Maker",
"5.4.2 Kitchen (F&B)",
"5.4.3 Marketing",]


txt = ""
for i in l:
	# print(i[:3])
	for ss in ["Correspondence","Current Documents", "Milestones"]:
		subfolder = lut[i[:3]]+"\\"+i+"\\"+ss
		txt += '"'+subfolder+'" '

print(txt)