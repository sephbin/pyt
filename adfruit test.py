import serial
baud_rate = 9600
s = serial.Serial('COM3',baudrate=baud_rate)
try:
	try: s.open()
	except: pass
	print(dir(s))
	s.write(b"Hello")
	s.close()
	# res = s.read()
	print(s)
except Exception as e:
	print(e)
	try: s.close()
	except: pass