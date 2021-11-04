import json
text ='''PM02	Broadcast Operations	4.1
PM03	Broadcast Operations	4.11
PM04	Broadcast Operations	4.12
PM05	Broadcast Operations	4.13
PM06	Broadcast Operations	4.14
PM07	Broadcast Operations	4.15
PM08	Broadcast Operations	4.16
PM09	Broadcast Operations	4.17
BM01	Broadcast Operations	4
BM02	Broadcast Operations	4.01
BM03	Broadcast Operations	4.02
BM04	Broadcast Operations	4.02.2
BM05	Broadcast Operations	4.03
BM06	Broadcast Operations	4.03
BM07	Broadcast Operations	4.03
BM08	Broadcast Operations	4.03
BM09	Broadcast Operations	4.04
BM10	Broadcast Operations	4.06
BM11	Broadcast Operations	4.07
BM99	Broadcast Operations	4.02
PM01	Broadcast Operations	4.09
MA13	Rugby Operations	1.02.8
RU24	Rugby Operations	2.06
CM01	Commercial Hospitality	6.01.3
CM02	Commercial Hospitality	6.01.3
CM03	Commercial Hospitality	6.02.1
HS01	Commercial Hospitality	6.03
HS02	Commercial Hospitality	6.03.1
HS03	Commercial Hospitality	6.03.2
HS04	Commercial Hospitality	6.03.3
HS06	Corporate Hospitality	
MA01	Competition Areas	1.01
MA02	Competition Areas	1.01.2
MA03	Competition Areas	1.01.2
MA04	Competition Areas	1.01.3
MA05	Competition Areas	1.02.1
MA06	Competition Areas	1.02.2
MA07	Competition Areas	1.02.3
MA08	Competition Areas	1.02.4
MA09	Competition Areas	1.02.5
MA10	Competition Areas	1.02.6
MA13	Competition Areas	
MA11	Competition Areas	1.02.6.1
MA12	Competition Areas	1.02.7
MA17	Competition Areas	2.02
HS05	Corporate Hospitality	6.03.4
HS21	Corporate Hospitality	
CS02	Match Management	5.01.2
CS03	Match Management	5.01.3
CS04	Match Management	5.01
CS05	Match Management	5.02.1
CS06	Match Management	5.02.2
CS07	Match Management	5.02.4
CS08	Match Management	5.03
CS09	Match Management	5.04
CS10	Match Management	5.04
EM02	Match Management	3.01.1
EM03	Match Management	3.01.2
EM04	Match Management	3.02
EM05	Match Management	3.03
EM06	Match Management	3.04
EM07	Match Management	3.04.1
EM08	Match Management	3.05
EM09	Match Management	3.06
EM10	Match Management	3.07
EM11	Match Management	3.08
EM12	Match Management	3.09
EM13	Match Management	3.1
EM14	Match Management	3.11
EM15	Match Management	3.12
CM04	Merchandise & Program	6.02.2
RU01	Rugby Operations	2.01
RU02	Rugby Operations	2.01.1
RU03	Rugby Operations	2.02
RU04	Rugby Operations	2.02
RU05	Rugby Operations	2.02
RU06	Rugby Operations	2.02
RU07	Rugby Operations	
RU08	Rugby Operations	2.02
RU09	Rugby Operations	2.02
RU10	Rugby Operations	2.02
RU11	Rugby Operations	2.03
RU12	Rugby Operations	2.04
RU13	Rugby Operations	2.04
RU14	Rugby Operations	2.04
RU15	Rugby Operations	2.04
RU16	Rugby Operations	2.04
RU17	Rugby Operations	2.04
RU18	Rugby Operations	2.04
RU19	Rugby Operations	2.05
RU20	Rugby Operations	2.05
RU21	Rugby Operations	2.05.1
RU22	Rugby Operations	2.05.2
RU23	Rugby Operations	2.05.3
RU25	Rugby Operations	2.06
RU26	Rugby Operations	2.06
RU28	Rugby Operations	2.07
RU29	Rugby Operations	2.08
RU30	Rugby Operations	2.02
SP01	Spectators	7.01
SP02	Spectators	7.01
SP03	Spectators	7.02
SP04	Spectators	7.03
SP05	Spectators	7.3
SP06	Spectators	7.04
SP07	Spectators	7.05
SP08	Spectators	7.06
CS01	Sports Presentation	5.01.1
TE01	Transport	8
CA01	Competition Areas	
CA02	Competition Areas	
MM01	Match Management	'''

with open(r"\\sydsrv01\projects\2019\219180.00\11.0 DRAWINGS\11.04 Rhino\Rhino.Inside\data.json", "r") as file:
	data = json.load(file)
	conv = text.split("\t")
	# print(data)
	for d in data:
		for c in conv:
			try:
				if c[0] == d["mark"]:
					d["department"] = c[1]
			except: pass
	# print(data)
	print(json.dumps(data))