# -*- coding: utf-8 -*-
""" 
Python Script
Created on  Tuesday November 2021 11:59:34 
@author:  andrew.butler 

[desc]
Description of the plugin Here
Write here any thing... 
[/desc]

ARGUMENTS:
----------
<inp> 
	choices :[required] - [type = list] - [default = []]]
	Descripe your input here 
		* bullet point.
		* bullet point
</inp>
<inp> 
	match :[required] - [type = list] - [default = []]]
	Descripe your input here 
		* bullet point.
		* bullet point
</inp>

RETURN:
----------
	<out>
		output_ : indicate your output description here. \n refers to a new line.
	</out>

"""

from fuzzywuzzy import fuzz
from fuzzywuzzy import process

outOb = []
for m in match:
	choice, score = process.extractOne(m, choices)
	outOb.append(choice)

output_ = outOb