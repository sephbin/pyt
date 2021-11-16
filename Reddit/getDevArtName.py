import os
import pyexiv2
directory = r"C:\Users\Andrew\Documents\GitHub\pyt\Reddit\cache\devart"
userList = []	
for file in os.listdir(directory):
	file = os.path.join(directory,file)
	# print(file)
	filename = os.fsdecode(file)
	# print(dir(exivimg))
	try:
		exivimg = pyexiv2.Image(file)
		xmp = exivimg.read_xmp()
		title = xmp['Xmp.dc.title']['lang="x-default"'].replace("https://www.deviantart.com/","")
		print(title)
		if r"/" in title:
			user = title.split(r"/")[0]
			userList.append(user)
			userList = list(set(userList))
	except: pass

print(userList)