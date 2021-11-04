#Set array to append data generated in the loop
collectArray = []
#Set a variable that will help determine a condition
condition = 0

#Star the loop, condition statement written in brackets
while(condition<=10):
	collectArray.append(condition)
	condition += 1
	#You can add more complex conditions for the loop to end with an "IF and BREAK"
	#Remove the next two "#" characters to break the loop using an IF. 
	# if (len(collectArray)>=3):
	# 	break

import json

#Print result
print(collectArray)