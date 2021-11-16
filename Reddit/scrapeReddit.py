import praw
import re
import shutil
import requests
import os
from secure import createRedditSecure
from google.cloud import vision
import pyexiv2

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="cache/pyvision-331611-767b74d9e10c.json"
reddit = createRedditSecure()
print(reddit.read_only)
subredlist = {

"ImaginaryArchers": {"base":"characters"},
"ImaginaryAssassins": {"base":"characters"},
"ImaginaryAstronauts": {"base":"characters"},
"ImaginaryKnights": {"base":"characters"},
"ImaginaryLovers": {"base":"characters"},
"ImaginaryMythology": {"base":"characters"},
"ImaginaryNobles": {"base":"characters"},
"ImaginaryScholars": {"base":"characters"},
"ImaginarySoldiers": {"base":"characters"},
"ImaginaryWarriors": {"base":"characters"},
"ImaginaryWitches": {"base":"characters"},
"ImaginaryWizards": {"base":"characters"},


"ImaginaryAngels":{"base":"characters"},
"ImaginaryDwarves":{"base":"characters"},
"ImaginaryElves":{"base":"characters"},
"ImaginaryFaeries":{"base":"characters"},
"ImaginaryHumans":{"base":"characters"},
"ImaginaryImmortals":{"base":"characters"},
"ImaginaryMerfolk":{"base":"characters"},
"ImaginaryOrcs":{"base":"characters"},

"ImaginaryArchitecture":{"base":"architecture"},
"ImaginaryCastles":{"base":"architecture"},
"ImaginaryDwellings":{"base":"architecture"},
"ImaginaryInteriors":{"base":"architecture"},


"ImaginaryBeasts":{"base":"monsters"},
"ImaginaryBehemoths":{"base":"monsters"},
"ImaginaryCarnage":{"base":"monsters"},
"ImaginaryDemons":{"base":"monsters"},
"ImaginaryDragons":{"base":"monsters"},
"ImaginaryElementals":{"base":"monsters"},
"ImaginaryHorrors":{"base":"monsters"},
"ImaginaryHybrids":{"base":"monsters"},
"ImaginaryLeviathans":{"base":"monsters"},
"ImaginaryMonsterGirls":{"base":"monsters"},
"ImaginaryUndead":{"base":"monsters"},
"ImaginaryWorldEaters":{"base":"monsters"},


"ImaginaryArmor":{"base":"technology"},
"ImaginaryCybernetics":{"base":"technology"},
"ImaginaryCyberpunk":{"base":"technology"},
"ImaginaryFutureWar":{"base":"technology"},
"ImaginaryFuturism":{"base":"technology"},
"ImaginaryMechs":{"base":"technology"},
"ImaginaryPortals":{"base":"technology"},
"ImaginaryRobotics":{"base":"technology"},
"ImaginaryStarships":{"base":"technology"},
"ImaginarySteampunk":{"base":"technology"},
"ImaginaryVehicles":{"base":"technology"},
"ImaginaryWeaponry":{"base":"technology"},


"ImaginaryBattlefields": {"base":"landscapes"},
"ImaginaryCityscapes": {"base":"landscapes"},
"ImaginaryHellscapes": {"base":"landscapes"},
"ImaginaryMindscapes": {"base":"landscapes"},
"ImaginaryPathways": {"base":"landscapes"},
"ImaginarySeascapes": {"base":"landscapes"},
"ImaginarySkyscapes": {"base":"landscapes"},
"ImaginaryStarscapes": {"base":"landscapes"},
"ImaginaryWastelands": {"base":"landscapes"},
"ImaginaryWeather": {"base":"landscapes"},
"ImaginaryWildlands": {"base":"landscapes"},
"ImaginaryWorlds": {"base":"landscapes"},
}
for subred, subdata in subredlist.items():
	
	groups = [
	reddit.subreddit(subred).top("all"),
	reddit.subreddit(subred).top("year"),
	reddit.subreddit(subred).top("month"),
	reddit.subreddit(subred).top("week"),
	reddit.subreddit(subred).top("day"),
	reddit.subreddit(subred).hot(limit=100),
	]

	for group in groups:
		for submission in group:
			try:
				title = submission.title.encode('utf-8')
				data = vars(submission)
				if data["post_hint"] == "image":
					# print(vars(submission))
					url = data["url_overridden_by_dest"]
					filetype = url.split(".")[-1]
					filetype = filetype.split("?")[0]
					if filetype in ["jpg","png","gif"]:
						filename = "".join([data["author"].name,"_",data["name"],".",filetype])
						# print(data)
						# if not os.path.isfile("cache\\"+subdata["base"]+"\\"+filename):
						if os.path.isfile("cache\\"+subdata["base"]+"\\"+filename):
							
							img_response = requests.get(url, stream=True)
							print(subred, filename)
							keywords = [subred]

							# client = vision.ImageAnnotatorClient()
							# image = vision.Image()
							# image.source.image_uri = url
							# response = client.label_detection(image=image, max_results=40)
							# ignore = ["art", "font", "illustration", "handwriting", "painting",
							# 'drawing', 'fictional character', 'visual arts', 'supernatural creature', 'graphics', 'graphic design', 'fiction',
							#  'hero',
							# ]
							# for label in response.label_annotations:
							# 	# print(label.description, '(%.2f%%)' % (label.score*100.))
							# 	desc = label.description.lower()
							# 	if desc not in ignore:
							# 		keywords.append(desc)
							print(keywords)

							with open("cache\\"+subdata["base"]+"\\"+filename, 'wb') as out_file:
								shutil.copyfileobj(img_response.raw, out_file)
							del img_response
							# keywords = ["Building","Water","Skyscraper","Atmospheric phenomenon","Rectangle","Cloud","Glass","Sky","Tints and shades","City","Tower block","Facade","Transparent material","Urban area","Metropolis","Urban design","Reflection","Darkness","Condominium","Tower",]
							img = pyexiv2.Image("cache\\"+subdata["base"]+"\\"+filename)
							# print(dir(img))
							# print(img.read_xmp())
							img.modify_xmp({'Xmp.dc.subject': keywords, 'Xmp.dc.title': url, 'Xmp.iptc.CreatorContactInfo/Iptc4xmpCore:CiUrlWork': "https://www.reddit.com"+submission.permalink})
			except Exception as e:
				print(e)
				# break
			# print(title)
			# break
		# break
	# break





# print(help(client.label_detection))


# print('Labels (and confidence score):')
# print('=' * 30)
# for label in response.label_annotations:
#     print(label.description, '(%.2f%%)' % (label.score*100.))