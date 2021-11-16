from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import shutil
import requests
import pyexiv2
import time
words = ""

driver = webdriver.Chrome(executable_path=r'F:\Downloads\chromedriver_win32\chromedriver.exe',service_log_path=None)
bases = [
# "https://www.artstation.com/channels/concept_art?sort_by=trending&dimension=2d"
"https://www.artstation.com/channels/matte_painting?sort_by=trending&dimension=2d"
]
imageUrls = []
for base in bases:
	base = base.replace("#",r"%23")
	driver.get(base)

	# driver.find_element_by_css_selector('[aria-label="Search by image"]').click()

	i = 0


	for i in range(20):
		try:
			driver.execute_script("window.scrollTo(0,64000)")
			images_selenium = driver.find_elements_by_css_selector('.gallery-grid-link')
			imageUrls = list(set(imageUrls + list(map(lambda x: x.get_attribute("href"), images_selenium))))
			print(len(imageUrls))
	# 		imageScores = driver.find_elements_by_css_selector('[aria-label="Favourite"]')
	# 		imageUrls = list(set(imageUrls + list(map(lambda x: x.get_attribute("href"), images_selenium))))
	# 		print(i,"nextButtons vvvvvvv")
	# 		nextButtons = driver.find_elements_by_css_selector('a')
	# 		print("nextButtons", nextButtons)
	# 		for nextButton in nextButtons:
	# 			try:
	# 				if "Next" in nextButton.get_attribute("innerText"):
	# 					try:
	# 						print(nextButton.get_attribute("innerText"))
	# 						nextUrl = nextButton.get_attribute("href")
	# 						print(nextUrl)
	# 						driver.get(nextUrl)
	# 					except Exception as e:
	# 						print(e)
	# 			except Exception as e:
	# 				print(e)

	# 		# print(nextButton)
	# 		# nextUrl = nextButton.get_attribute("href")
	# 		# print(nextUrl)
		except: pass
		time.sleep(1)
driver.close()
driver.quit()
	# print(imageUrls)
print(len(imageUrls),imageUrls)
imageDriver = webdriver.Chrome(executable_path=r'F:\Downloads\chromedriver_win32\chromedriver.exe',service_log_path=None)
for image in imageUrls:
	try:
		imageId = image.split("/")[-1] 
		imageDriver.get(image)
		tags = imageDriver.find_elements_by_css_selector('.label-tag')
		tags = list(map(lambda x: x.get_attribute("innerText").encode('utf-8').decode('ascii', 'ignore').lower(), tags))
		print(tags)
		imageDL = imageDriver.find_elements_by_css_selector('.img')
		for resIndex, resImage in enumerate(imageDL):
			try:
				imageUrl = resImage.get_attribute("src")
				imageAlt = resImage.get_attribute("alt")
				print(imageUrl, imageAlt)
				img_response = requests.get(imageUrl, stream=True)
				fileName = "Reddit\\cache\\"+"ArtStation"+"\\"+imageAlt+"-"+imageId+"_"+str(resIndex)+".jpg"
				with open(fileName, 'wb') as out_file:
					shutil.copyfileobj(img_response.raw, out_file)
				exivimg = pyexiv2.Image(fileName)
				exivimg.modify_xmp({'Xmp.dc.subject': tags, 'Xmp.dc.title': image})
			except:
				pass
	except Exception as e:
		print("error",e)
		pass
imageDriver.close()
imageDriver.quit()

