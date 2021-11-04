# -*- coding: utf-8 -*-
import os
import sys
import mutagen
import time
path = r'T:\Personal Temp\s-abutler\_MLIB2'
for path, subdirs, files in os.walk(path):
	for name in files:
		try:
			fpath=os.path.join(path, name)
			mFile = mutagen.File(fpath)
			# print(fpath)
			try:
				# print(filename)
				# print(mFile)
				try:
					artist = mFile['\xa9ART'][0]
					artist = artist.title()
					sp = artist.split(", ")
					sp = sp[::-1]
					artist = ' '.join(sp)
					print(artist)
					mFile['\xa9ART'] = artist
				except:
					pass
				try:
					aArt = mFile['aART'][0]
					aArt = aArt.title()
					sp = aArt.split(", ")
					sp = sp[::-1]
					aArt = ' '.join(sp)
					print(aArt)
					mFile['aART'] = aArt
				except:
					pass
				mFile.save()
			except Exception as e:
				print(e)
				print(mFile)
				# print(mFile)
		except:
			pass
