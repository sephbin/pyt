from laspy.file import File
import numpy as np

inFile = File(r'D:\Users\s-abutler\Downloads\512box.las', mode='r')

# print(inFile.points)
# # print(dir(inFile))
# print(inFile.points[0])
# print(inFile.points[1])

pcTup = [((0,0,0,0,0,0,0,0,0,0,0,0),),((512,512,512,0,0,0,0,0,0,65535,0,65535),)]
newPC = np.array(pcTup)
print(newPC)
outFile = File(r'D:\Users\s-abutler\Downloads\a.las', mode='w', header=inFile.header)
# outFile.points = inFile.points
outFile.points = pcTup
outFile.close()