from bs4 import BeautifulSoup
import requests
import re
import json
from selenium import webdriver
from time import sleep # this should go at the top of the file

# url = "https://www.bunnings.com.au/johnson-tiles-97-x-97mm-concrete-gloss-spectrum-wall-tile_p0012026"
root = "https://www.bunnings.com.au"
url = root+"/search/products?page=1&q=plasterboard&sort=BoostOrder&pageSize=60"
# url = "https://www.bunnings.com.au/hyne-165-x-65mm-h2-treated-pine-glulam-structural-beam-17-per-linear-metre_p8461033"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}



PATH = r"C:\Temp\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get(url)
try:
	sleep(5)
	html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
except Exception as e:
	print(e)
	pass
driver.quit()

soup = BeautifulSoup(html, 'html.parser')

regex = re.compile(r'^/.')
# ^= Start of text
# /= /
# . = any character
content_lis = soup.find_all('a', attrs={'href': regex})

links = list(map(lambda x: x['href'], content_lis))

index = 0
# print(links)
for link in links:
	killLink = ["bbundle","/maps.google.com.au","/our-range", "/stores","/our-services", "/jobs", "/contact-us", "/login", "/wish-lists", "/cart","/bunnings-marketlink", "/redemption-offers", "/bunnings-magazine", "/gift-cards", "/gift-ideas", "/diy-advice","/workshop-online-community", "/trade", "/about-us", "/search","/price-policy", "/about-us", "/media-centre", "/catalogue", "/installation-licensing", "/returns", "/shop-online", "/exclusive-to-powerpass", "/product-recalls", "/product-reviews", "/terms-of-use", "/online-shopping-terms-conditions", "/special-orders-terms-conditions", "/online-gift-cards-terms", "/hire-shop-terms-conditions", "/privacy-policy", "/privacy-statement", "/privacy-policy-credit", "/store-entry-information", "/scam-warning", "/superannuation-payment-information", "/sitemap",]
	killLoop = False
	for k in killLink:
		if k in link:
			killLoop=True
	if killLoop:
		continue
	
	index += 1
	if index > 1:
		break
	#### Standard Request
	# r = requests.get(root+link,
	# 	headers=headers
	# 	).text
	r = ""
	try:
		driver = webdriver.Chrome(PATH)
		driver.get(root+link)
		sleep(1)
		r = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
	except Exception as e:
		print(e)
	driver.quit()


	lines = r.split("\n")
	nodata = True
	for l in lines:
		if "productDetailsData" in l:
			nodata = False
			l = l.replace("var productDetailsData =","").replace("};","}")
			# l = r'  {"allowEnquiryLabel":"Add To Enquiry"}'
			datadict = json.loads(l)
			postob = {
					"createdBy": "Example",
					"name": "Example",
					"data": {
						# "url": root+link,
						"url": "",
						"type":"Example",
						"dimensions": {
						# "width" : datadict["productDimensions"]["width"],
						# "length" : datadict["productDimensions"]["height"],
						# "height" : datadict["productDimensions"]["depth"],
						"width" : None,
						"length" : None,
						"height" : None,
						"unit" : None,
						"diameter" : None,
						"dynamicVariable" : None,
						"quantity" : None,
						},
						"weight": {
							"value" : None,
							"unit" : None
						},
						"material":{
							"name":None
						},
						"cost" : {
							"value" : None,
							"type" : None
						},
						},
				}
			print(postob)
			post = requests.post("http://labs.cox.com.au/muninn_dev/api/uploadBuildingComponent/",
				data = json.dumps(postob)
				).text
			print(post)
			print(datadict["displayName"])
	if nodata:
		print(link, "NO PRODUCT DETAILS DATA")
		# print(lines)
		# error = True
		# break
