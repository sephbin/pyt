from bs4 import BeautifulSoup
import requests
import re
import json
# from selenium import webdriver
# from time import sleep # this should go at the top of the file

headers =			{'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36', 'cookie':'_ga=GA1.2.89752886.1588115502; intercom-id-m4bn23d4=9741813d-8ce9-4e89-a2b9-d8726ca9ea29; OASSOProviderUsed=1; _BEAMER_USER_ID_zwnrZPQO21118=ac7ab72b-d65d-45b0-bdd7-ad16432a960d; _BEAMER_FIRST_VISIT_zwnrZPQO21118=2020-05-11T03:12:23.589Z; _mkto_trk=id:974-TQN-870&token:_mch-openasset.com-1592550701324-29056; _gid=GA1.2.1062936720.1592550702; OpenAsset_F22C=CD80121108176EB5D5365358F9DBCB80; _BEAMER_FILTER_BY_URL_zwnrZPQO21118=false'}
# projectNumber =	"217023.00"
projectNumber =		"213039.00"
projList =			requests.get("https://cox.openasset.com/REST/1/Projects/?code=%s"%(projectNumber), headers=headers).json()
projImages =		requests.get("https://cox.openasset.com/REST/1/Files/?project_id=%s&limit=0"%(projList[0]["id"]), headers=headers).json()

for image in projImages:
	# print(json.dumps(image))
	print(image["rank"])
	sizes = requests.get("https://cox.openasset.com/REST/1/Files/%s/Sizes"%(image["id"]), headers=headers).json()

	for r in sizes:
		# print(r["width"],r["height"], r)
		if "high" in r["http_relative_path"]:
			# print(r)
			# imgpath = "https:"+r["http_root"]+r["relative_path"]
			# print(imgpath)
			pass