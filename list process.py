lookup = {"J01":"Reception Desk", "J02A":"Trophy Cabinet with Bench", "J02B":"Trophy Cabinet", "J03":"First Aid / Physio Treatment Joinery Unit", "J04":"Supervisor's Desk", "J05":"Strength & Conditioning Teapoint / Utilities", "J06A":"Cardio Room Joinery", "J06B":"Rowing / ERG Room Joinery", "J07":"Locker Shroud", "J09":"Basketball Locker Room Locker", "J10":"Window Bench Seating", "J11":"Credenza Joinery", "J12":"PDHPE Teapoint / Utilities", "J13":"Christian Studies Teapoint / Utilities", "J14":"Office Teapoint", "J15":"Wall Mounted Laptop Shelf", "J16":"Wet Area Bench - Double-Sided", "J17":"Wet Area Bench - Singled-Sided"}

clist = ["N/A", "1no J02B", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "4no J07; 2no J16; 7no J17", "4no J07; 2no J16; 7no J17", "N/A", "1no J03", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "4no J07; 2no J16; 6no J17", "4no J07; 2no J16; 6no J17", "N/A", "1no J17", "20no J09; 1no J15", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "1no J11", "N/A", "2no J10", "2no J10", "2no J10", "1no J10", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "1no J10; 1no J13", "N/A", "1no J01", "1no J14", "1no J03", "1no J05", "1no J04", "1no J06A", "1no J06B", "1no J02A ", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "5no J07; 2no J16; 9no J17", "5no J07; 2no J16; 7no J17", "N/A", "N/A", "N/A", "N/A", "1no J16; 1no J17", "1no J16; 1no J17", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "1no J12; 2no J10; 1no J11", "N/A", "2no J10", "2no J10", "2no J10", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A"]

NONE = []

for c in clist:
	text = c.split("; ")
	outob = []
	for f in text:
		try:
			text = f
			lu = f.split(" ")
			text = f.replace(f, f+": "+lookup[lu[-1]])
			outob.append(text)
			# outob.append(f+": "+lookup[f])
		except:
			outob.append("!!!"+f)
			NONE.append(f)

	print("  ".join(outob))

print(NONE)