
import os, subprocess, ctypes, platform, getpass, requests
user32 = ctypes.windll.User32

def isLocked():
	return user32.GetForegroundWindow() == 0

if not isLocked():
	compNumber = platform.node()
	userName = getpass.getuser()
	stream = subprocess.check_output(["qwinsta"]).decode("utf-8")
	stream = stream.split("\r\n")
	if "-VD-" not in compNumber:
		for s in stream:
			if "Active" in s and "rdp-tcp" not in s :
				try:
					print("in office:",compNumber, userName)
					data = {"computer":compNumber, "user":userName}
					r = requests.post(url = "workshop.cox.com.au/oj/autocheckin/", data = data)
				except:
					pass
