import os


# for subdir, dirs, files in os.walk(rootdir):
# 	if "11.0 DRAWINGS" not in subdir:
# 		continue
# 	if files == []:
# 		continue
# 	if any(".rvt" in f for f in files):
# 		index += 1
# 		print(subdir, files)
# 	else:
# 		continue
# 	if index > 10:
# 		break
# 	# for file in files:
# 		# print(os.path.join(subdir, file))

years = [
"2020",
"2019",
"2018",
"2017",
"2016",
"2015",
"2014",
]
for y in years:
	print(y)
	rootdir = os.path.join("K:",y)


	basedir = os.listdir(rootdir)
	# print(basedir)
	for bd in basedir:
		try:
			revfolder = os.path.join(rootdir,bd,"11.0 DRAWINGS","11.01 Revit Model")
			revfiles = os.listdir(revfolder)
			if any(".rvt" in f for f in revfiles):
				print(bd)
		except Exception as e:
			# print(e)
			pass