# Save as client.py 
# Message Sender
import os
from socket import *
# host = input("Enter ip address of host: ")
# host = "127.0.0.1" # set to IP address of target computer
host = "127.0.0.1"
port = 13001
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
# while True:
    # data = input("Enter message to send or type 'exit': ")
# data = "import requests"
data = [
# "r = requests.post(url = 'https://www.google.com/')",
# "print(r)",
# "print(r.text)",
"exit",
'toaster = ToastNotifier()',
# 'toaster.show_toast("Possible file conflict","With Andrew Butler", icon_path ="custom.ico", duration=100)',
'toaster.show_toast("Possible file conflict","With Andrew Butler", duration=100)',
]
for d in data:
	d = d.encode()
	UDPSock.sendto(d, addr)
# if data == "exit":
#     break
UDPSock.close()
os._exit(0)