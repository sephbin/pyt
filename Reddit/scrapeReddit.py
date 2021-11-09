import praw
import re
import shutil
import requests
import os
from secure import createRedditSecure


reddit = createRedditSecure()
print(reddit.read_only)
subredlist = {

# "ImaginaryArchers": {"base":"characters"},
# "ImaginaryAssassins": {"base":"characters"},
# "ImaginaryAstronauts": {"base":"characters"},
# "ImaginaryKnights": {"base":"characters"},
# "ImaginaryLovers": {"base":"characters"},
# "ImaginaryMythology": {"base":"characters"},
# "ImaginaryNobles": {"base":"characters"},
# "ImaginaryScholars": {"base":"characters"},
# "ImaginarySoldiers": {"base":"characters"},
# "ImaginaryWarriors": {"base":"characters"},
# "ImaginaryWitches": {"base":"characters"},
# "ImaginaryWizards": {"base":"characters"},


# "ImaginaryAngels":{"base":"characters"},
# "ImaginaryDwarves":{"base":"characters"},
# "ImaginaryElves":{"base":"characters"},
# "ImaginaryFaeries":{"base":"characters"},
# "ImaginaryHumans":{"base":"characters"},
# "ImaginaryImmortals":{"base":"characters"},
# "ImaginaryMerfolk":{"base":"characters"},
# "ImaginaryOrcs":{"base":"characters"},

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


# "ImaginaryBattlefields": {"base":"landscapes"},
# "ImaginaryCityscapes": {"base":"landscapes"},
# "ImaginaryHellscapes": {"base":"landscapes"},
# "ImaginaryMindscapes": {"base":"landscapes"},
# "ImaginaryPathways": {"base":"landscapes"},
# "ImaginarySeascapes": {"base":"landscapes"},
# "ImaginarySkyscapes": {"base":"landscapes"},
# "ImaginaryStarscapes": {"base":"landscapes"},
# "ImaginaryWastelands": {"base":"landscapes"},
# "ImaginaryWeather": {"base":"landscapes"},
# "ImaginaryWildlands": {"base":"landscapes"},
# "ImaginaryWorlds": {"base":"landscapes"},
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
						if not os.path.isfile("cache\\"+filename):
							
							response = requests.get(url, stream=True)
							print(subred, filename)
							with open("cache\\"+subdata["base"]+"\\"+filename, 'wb') as out_file:
								shutil.copyfileobj(response.raw, out_file)
							del response
			except:	pass
				# break
			# print(title)