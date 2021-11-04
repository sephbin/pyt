from datetime import datetime, timedelta, date

def offsetDay(startDate, targetDay, direction = 3):
	from datetime import timedelta
	
	try: startDay = startDate.strftime("%A")
	except: startDay = startDate

	daylist = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
	index = daylist.index(targetDay)
	chopA = daylist[:index]
	chopB = daylist[index:]
	daylist = chopB+chopA
	print(daylist)
	if direction == 0:
		dayoffset = [0]+list(range(6,1,-1))
	elif direction == 1:
		dayoffset = list(range(0,-7,-1))
	elif direction == 2:
		dayoffset = list(range(0,-4,-1))+list(range(3,0,-1))
	elif direction == 3:
		dayoffset = list(range(0,-4,-1))+list(range(3,0,-1))
		if daylist.index("Monday") == 3:
			dayoffset[3]=4
		if daylist.index("Friday") == 4:
			dayoffset[4]=-4
	
	offsetIndex = dayoffset[daylist.index(startDay)]
	try:
		outDate = startDate+timedelta(days=offsetIndex)
		return outDate
	except:
		return offsetIndex


Now = date.today()
print(Now)
print(offsetDay(Now,"Monday"))