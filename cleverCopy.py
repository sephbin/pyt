def serverToDropbox():
	from iptcinfo3 import IPTCInfo
	import os
	import shutil
	import datetime
	# rootdir =r'C:\Temp\Dropbox (COX Archit/ecture)\DC6\COX_CSIRO_ACT Framework Plan Folder'
	# rootdir =r'K:\2018\218999.99'
	proj = input("Project Number to migrate to Dropbox\n")
	# proj = "218999.99"
	rootdir = 'K:\\20%s%s\\%s'%(proj[1],proj[2],proj)
	print(rootdir)
	out = []
	parse = []

	for subdir, dirs, files in os.walk(rootdir):
		for file in files:
			try:
				f = os.path.join(subdir, file)
				if f.endswith(".dropbox"):
					out.append(f)
				# parse.append(f)
			except:
				pass
	# parse.reverse()
	# index = len(parse)
	# for f in parse:
	# 	try:
	# 		if index % 50 == 0:
	# 			print(str(index)+" "*10, end="\r")
	# 		index += -1
	# 		info = IPTCInfo(f)
	# 		kw = info["keywords"]
	# 		if b'used' in kw or f.endswith(".indd"):
	# 			# print(f)
	# 			out.append(f)
	# 		# if index <= 710:
	# 			# break
	# 	except:
	# 		pass

	print(out)


	for src in out:
		dst = src.replace("K:\\","Z:\\")
		file = dst
		dst = os.path.dirname(dst)
		try:	os.makedirs(dst)
		except:	pass
		# print(dst)
		try:
			arch = os.path.join(dst,"archive")
			try:	os.makedirs(arch)
			except Exception as e:
				# print(e)
				pass
			try:
				nfn = file.replace(".dropbox","")
				ofn = "."+datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
				shutil.move(nfn, arch)
				print(nfn,"  ->  ", arch)
				archfile = os.path.join(arch,os.path.basename(nfn))
				archfilespn = archfile+ofn
				print("..",archfile,"  ->  ", archfilespn)
				os.rename(archfile, archfilespn)
			except Exception as e:
				# print(e)
				pass


			shutil.copy(src, dst)
			os.rename(file, nfn)
			print("-",nfn)
		except Exception as e:
			print(e)
			pass
	print("Done migrating %s to Dropbox"%(proj))

serverToDropbox()
# import win32com.client
# app = win32com.client.Dispatch('InDesign.Application.CC.2019')
# print(dir(app.Documents))
# myDocument = app.Documents.Add()
# myDocument = app.Open("C:\\Temp\\Dropbox\\DC6\\COX_CSIRO_ACT Framework Plan Folder\\COX_CSIRO_ACT Framework Plan.indd");
# print(myDocument)
# myPage = myDocument.Pages.Item(1)
# myTextFrame = myPage.TextFrames.Add()
# myTextFrame.GeometricBounds = ["6p0", "6p0", "18p0", "18p0"]
# myTextFrame.Contents = "Hello World!"

