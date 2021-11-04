import os, sys, subprocess, ctypes, platform, getpass, requests, time, json
user32 = ctypes.windll.User32

def isLocked():
	return user32.GetForegroundWindow() == 0


error = 0
running = True
while running:
	exec(open("T:\\Software Temp\\CheckIn\\coxcheckin\\runcode.py").read())