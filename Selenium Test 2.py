from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import shutil
import requests
import pyexiv2
import time
import os
import glob
words = ""
other = ['jess-madhouse', 'typhonart', 'tsvetka', 'istrandar', 'willwarburton']
goodUsers = ["donatoarts", "markelli",'mhandt', 'r-tan', 'raysheaf', 'mishelangello', 'takmaj', 'anatofinnstark', 'hbajramovic', 'irenhorrors', 
'just-rascal', 'luka-basyrov-art', 'katarzyna-kmiecik', 'astoralexander', 'w-e-z', 'kylewright', 'merl1ncz', 'igorlevchenko', 'deharme', 'yoann-lossel', 'era7', 'donatoarts', 'jozefbalaz', 'carlos-quevedo', 'florentllamas',
]
# goodUsers = ['zsoltkosa', 'sirtiefling', 'eduardo-pena', 'algenpfleger', 'rittik-designs', 'wraithdt', 'lpsdc', 'darekzabrocki', 'scottpurdy', 'dangercook', 'njoo', 'greg-opalinski', 'boc0', 'orekigenya', 'devburmak', 'candra', 'manzanedo', 'telthona', 'natalyalex', 'adiillu', 'edcid', 'getsugadante', 'benoit-godde', 'chateaugrief', 'endemilk', 'baklaher', 'dongjunlu', 'arvalis', 'zoonoid', 'elenadudina', 'zeilyan', 'jemajema', 'jonasdero', 'yngvarasplund', 'delowar', 'carmensinek', 'justynagil', 'aaronmiller', 'jeleynai', 'cynic-pavel', 'xpendable', 'willobrien']
# goodUsers = ['hanh-chu', 'millikodea', 'antoinettestoll', 'matija5850', 'vitogh', 'icezimy', 'ferdinandladera', 'jpryno', 'whendell', 'kunsword', 'emanuelmardsjo', 'bryansyme', 'eliottsontot', 'elemont', 'moonsongwolf', 'vexim', '1ver4ik1', 'majesticchicken', 'era-7', 'guweiz', 'kolokas', 'adelasu1', 'ivantao', 'sarcone', 'goatlord51', 'cendence1', 'warp-zero', 'kimsuyeong81', 'yurishwedoff', '2wenty', 'tsabo6', 'haikai13', 'shootingstarlogbook', 'woutart', 'gantzu', 'johnsilva', 'tsundere-power', 'iromonik', 'seraph777', 'quackermelonn', 'anatofinnstark', 'jonik9i', 'kloir', 'liiga', 'wskalska99', 'joelchaimholtzman', 'thomas-elliott-art', 'blazbaros', 'remarin', 'ashpwright', 'sarty96', 'wood-illustration', 'oiu4ever', 'artofryanyee', 'irontree', 'vanharmontt', 'abyss1956', 'tyzranan', 'edufrancisco', 'flaviobolla', 'smekalov', 'alradeck', 'clockbirds', 'r00kie-n', 'jason-felix', 'eddy-shinjuku', 'tiagoaleixo', 'igorivart', 'grimdreamart', 'ketka', 'gornik6', 'damntorren', 'negg4dia', 'brittmartin', 'asahisuperdry', 'fooyee', 'chinnkun', 'booublik', 'artofty', 'shadypotatodragon', 'eksrey', 'lauragalliart', 'amenlona', 'mattdemino', 'ronindude', 'phaserunner', 'seansamson', 'tattiart', 'ullathynell', 'lightanri', 'sagasketchbook', 'piotrdura', 'elias-chatzoudis', 'paveltomashevskiy', 'ethicallychallenged', 'elsevilla', 'showmeyourmoves', 'azazel1944', 'irenbee', 'giz-art', 'robotdelespacio', 'pin100', 'mobiusu14', 'rayseb', 'mehrdadnikshomar', 'kastep', 'breath-art', 'michaeladamidisart', 'diegogisbertllorens', 'akreon', 'rainieshun', 'jameszapata', 'deathstars69', 'targete', 'zhangqipeng', 'reraartist', 'lasahido', 'd1sk1ss', 'ianllanas', 'sylverryn', 'gabriellebrickey', 'tohad', 'sadantelope', 'lord-of-the-guns', 'daverapoza', 'carlos-quevedo', 'richardlayart', 'nihmei', 'lolloboloz', 'infesth6', 'procsan', 'dopaprime', 'clintcearley', 'amisgaudi', 'dar-devil', 'muhut', 'chriscold', 'prywinko', 'czepeku', 'g-hamm', 'zolaida', 'alexboca', 'vladmrk', 'kerembeyit', 'wav3vil', 'philbyers', 'hamsterfly', 'era7', 'jasonchanart', 'patvit', 'elgrimlock', '88grzes', 'velinov', 'dmitrys', 'lealebourgeois', 'skavenzverov', 'pindurski', 'kilirai', 'kelvvv', 'caiomm', 'tr0tzki', 'aerroscape', 'mjesther13', 'crutz', 'almanegra', 'jybe44', 'dron111', 'kamikaye', 'sandara', 'futurodox', 'amysticpizza', 'eriktaberman', 'raidesart', 'jademerien', 'fainernil', 'jjcanvas', 'chris-karbach', 'marcellyne', 'jasonengle', 'teranen', 'jamesryman', 'reicheran', 'gladly', 'panjoool', 'drachenmagier', 'asur-misoa', '7a12deviant', 'deligaris', 'genzoman', 'vezoniaartz', 'nattyna', 'tamikaproud', 'beastysakura', 'maxgrecke', 'lozanox', 'arvl', 'depingo', 'nenadnacevic', 'milicraft', 'susanopower', 'mlenart', 'daarken', 'limboartwork', 'abigbat', 'klegs', 'rodrigo-vega', 'kilartdev', 'astri-lohne', 'arukanoda', 'caraidart', 'therafaarts', 'isbjorg', 'aleksi--briclot', 'jeanne24', 'earl-graey', 'tomtc', 'armandeo64', 'avereechaloupka']
# goodUsers = ['zsoltkosa']
driver = webdriver.Chrome(executable_path=r'F:\Downloads\chromedriver_win32\chromedriver.exe',service_log_path=None)
bases = [
# "https://www.deviantart.com/topic/fantasy",
# "https://www.deviantart.com/tag/conceptart",
# "https://www.deviantart.com/tag/mtg",
"https://www.deviantart.com/tag/landscapefantasy",
"https://www.deviantart.com/tag/landscapepainting",
# "https://www.deviantart.com/search?q=wyrm",
# "https://www.deviantart.com/88grzes/gallery",
# "https://www.deviantart.com/hamsterfly/gallery",
# "https://www.deviantart.com/clintcearley/gallery",
# "https://www.deviantart.com/targete/gallery",
# "https://www.deviantart.com/devburmak/gallery",
# "https://www.deviantart.com/darekzabrocki/gallery",
]
bases = list(map(lambda x: "https://www.deviantart.com/%s/gallery"%(x), goodUsers))
imageUrls = []
for base in bases:
	numberSearch = 5
	if "search?" in base:
		numberSearch = 1
	base = base.replace("#",r"%23")
	driver.get(base)
	driver.execute_script("window.scrollTo(0,64000)")

	# driver.find_element(By.CSS_SELECTOR, '[aria-label="Search by image"]').click()

	i = 0


	oldCount = -1
	for i in range(numberSearch):
		try:
			driver.execute_script("window.scrollTo(0,64000)")
			# images_selenium = driver.find_elements(By.CSS_SELECTOR, '[data-hook="deviation_link"]')
			images_selenium = driver.find_elements(By.CSS_SELECTOR, '[data-hook="deviation_link"]')
			# print(images_selenium)
			for image in images_selenium:
				try:
					# print(image)
					apUrl = str(image.get_attribute("href"))
					# print(apUrl)
					imageUrls.append(apUrl)
					imageUrls = list(set(imageUrls))
				except Exception as e:
					print(e,image)
			# imageUrls = list(set(imageUrls + list(map(lambda x: x.get_attribute("href"), images_selenium))))
			print("urlList", len(imageUrls))
			if len(imageUrls) == oldCount:
				break
			oldCount = len(imageUrls)
			try:
				# print(i,"nextButtons vvvvvvv")
				nextButtons = driver.find_elements(By.CSS_SELECTOR, 'a')
				# print("nextButtons", nextButtons)
				for nextButton in nextButtons:
					try:
						if "Next" in nextButton.get_attribute("innerText"):
							try:
								print(nextButton.get_attribute("innerText"))
								nextUrl = nextButton.get_attribute("href")
								print(nextUrl)
								driver.get(nextUrl)
							except Exception as e:
								print(e)
					except Exception as e:
						print(e)
			except Exception as e:
				print(e)

			# print(nextButton)
			# nextUrl = nextButton.get_attribute("href")
			# print(nextUrl)
		except Exception as e:
			print(e)
		# time.sleep(5)
driver.close()
driver.quit()
	# print(imageUrls)
fullLen = len(imageUrls)
# print(fullLen,imageUrls)
def downloadImage(image, driver=None):
	
	try:
		imageId = image.split("-")[-1]
		imageId = imageId.replace("\n","")
		globs = glob.glob(os.path.join("Reddit","cache","devart","*%s.*"%(imageId)))
		print(globs)
		if len(globs) == 0:
			print("DOWN",image)
			time.sleep(2)
			driver.get(image)
			tags = driver.find_elements(By.CSS_SELECTOR, '[href*="tag"]')
			tags = list(map(lambda x: x.get_attribute("innerText").encode('utf-8').decode('ascii', 'ignore').lower(), tags))
			# print(fullLen,tags)
			imageDL = driver.find_element(By.CSS_SELECTOR, '[draggable="true"]').find_element(By.CSS_SELECTOR, 'img')
			imageUrl = imageDL.get_attribute("src")
			imageAlt = imageDL.get_attribute("alt").translate({ord(i):None for i in r'''!@#?$,.-&:|0123456789(){}[]'\/'''})
			# print(fullLen,imageUrl)
			filetype = ".jpg"
			if ".png?" in imageUrl:
				filetype = ".png"
			if ".gif?" in imageUrl:
				filetype = ".gif"
			img_response = requests.get(imageUrl, stream=True)
			# print(fullLen,imageAlt+"-"+imageId+filetype)
			filepath = os.path.join("Reddit","cache","devart",imageAlt+"-"+imageId+filetype)
			filepath = filepath.replace("\n","")
			# for f in filepath:
			# 	print(f.encode('utf-8'))
			print(filepath)
			with open(filepath, 'wb') as out_file:
				shutil.copyfileobj(img_response.raw, out_file)
			try:
				exivimg = pyexiv2.Image(filepath)
				exivimg.modify_xmp({'Xmp.dc.subject': tags, 'Xmp.dc.title': image})
			except Exception as e:
				print(image,"error",e)
				pass
		else:
			print("SKIP",image)
	except Exception as e:
		# print(fullLen,"error",e)
		pass

	return image

# with open('devartcache.txt', 'w', newline='') as f:
# 	for item in imageUrls:
# 		f.write("%s\n" % item)
 
with open('devartcache.txt', 'r') as f:
	for item in f.readlines():
		imageUrls.append(item)


from multiprocessing.pool import ThreadPool as Pool
# from multiprocessing import Pool

iDr0 = webdriver.Chrome(executable_path=r'F:\Downloads\chromedriver_win32\chromedriver.exe',service_log_path=None)
iDr1 = webdriver.Chrome(executable_path=r'F:\Downloads\chromedriver_win32\chromedriver.exe',service_log_path=None)
iDr2 = webdriver.Chrome(executable_path=r'F:\Downloads\chromedriver_win32\chromedriver.exe',service_log_path=None)
iDr3 = webdriver.Chrome(executable_path=r'F:\Downloads\chromedriver_win32\chromedriver.exe',service_log_path=None)
# iDr4 = webdriver.Chrome(executable_path=r'F:\Downloads\chromedriver_win32\chromedriver.exe',service_log_path=None)
# iDr5 = webdriver.Chrome(executable_path=r'F:\Downloads\chromedriver_win32\chromedriver.exe',service_log_path=None)

pool_size = 2  # your "parallelness"
pool = Pool(pool_size)
# print("pool", pool)
for index, image in enumerate(imageUrls):
	try:
		driverIndex = index % 4
		# print(driverIndex, image)
		whichDriver = globals()["iDr"+str(driverIndex)]
		# print(whichDriver)
		a = pool.apply_async(downloadImage, (image, whichDriver))
	except: pass

pool.close()
pool.join()

iDr0.close()
iDr0.quit()
iDr1.close()
iDr1.quit()
iDr2.close()
iDr2.quit()
iDr3.close()
iDr3.quit()
# iDr4.close()
# iDr4.quit()
# iDr5.close()
# iDr5.quit()