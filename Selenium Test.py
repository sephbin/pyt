from selenium import webdriver
from selenium.webdriver.common.keys import Keys
words = ""
driver = webdriver.Chrome(executable_path=r'F:\Downloads\chromedriver_win32\chromedriver.exe')
driver.get("https://www.google.com/imghp?hl=en")
driver.find_element_by_css_selector('[aria-label="Search by image"]').click()
# driver.find_element_by_css_selector('[name="image_url"]').send_keys("https://cdna.artstation.com/p/assets/images/images/043/116/792/large/alhin-row-mhw-21.jpg" + Keys.ENTER)
driver.find_element_by_css_selector('[name="image_url"]').send_keys("https://cdnb.artstation.com/p/assets/images/images/023/030/615/large/ningbo-jiang-daming.jpg" + Keys.ENTER)
driver.find_element_by_css_selector('[aria-label="Search"]').clear()
# driver.find_element_by_css_selector('[aria-label="Search"]').send_keys("site:deviantart.com/*/art/" + Keys.ENTER)
driver.find_element_by_css_selector('[aria-label="Search"]').send_keys("site:cdnb.artstation.com" + Keys.ENTER)
# driver.find_element_by_css_selector('[data-attrid="images universal"]').click()
driver.find_element_by_css_selector('h3[aria-level="2"]').click()


images = driver.find_elements_by_css_selector('[rel="noopener"]')

# print(words)
for image in images:
	try:
		title = image.get_attribute("title").lower().translate({ord(i):None for i in r'!@#?$,.-&:|0123456789(){}[]'})
		words = words + title +" "
	except Exception as e:
		print("error",e)
		pass
try:
	words = words.encode('utf-8').strip()
	wordList = words.split()
	wordSet = list(set(wordList))
	ignore = list(map(lambda x: x.encode('utf-8'), [
		"deviantart", "wallpaper", "art","fantasy","character","wallpapers", "liveaction", "wallpaperuse", "screenshot", "game", "artwork", "fictional",
		'profile', 'user', 'professional', 'artist', 'digital',
		'games', 'adventure', 'anime', 'best', 'gamecg', 'movies', 'series', 'wallpaperup', 'mythology', 'wallhere' , 'rpg',
		"vs", "you", "and", "or", "on", "by", "of", "the", "hd", "x", "in", "for", "to"]))
	wordSet = [x for x in wordSet if x not in ignore]
	count = []
	for i in wordSet:
		countNum = wordList.count(i)
		count.append(countNum)
		# print(i, countNum)
	sorted_zipped_lists = sorted(zip(count,wordSet))
	print(sorted_zipped_lists)
	sorted_wordSet = [element for _, element in sorted_zipped_lists]
	print(sorted_wordSet)
except:
	pass


# aria-label="Search by image"

# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source


# <a class="VFACy kGQAp sMi44c lNHeqe WGvvNb" data-ved="2ahUKEwjMoKSS5Y30AhUWn0sFHSQYDf8Qr4kDegQIARB-" jsname="uy6ald" style="" rel="noopener" target="_blank" href="https://www.google.com/url?sa=i&amp;url=https%3A%2F%2Fwww.deviantart.com%2Fandimayer%2Fart%2FBeowulf-against-the-Dragon-350538702&amp;psig=AOvVaw0kEDRf1Y9BG8VBSKHUsvp7&amp;ust=1636633529053000&amp;source=images&amp;cd=vfe&amp;ved=2ahUKEwjMoKSS5Y30AhUWn0sFHSQYDf8Qr4kDegQIARB-" jsaction="focus:kvVbVb;mousedown:kvVbVb;touchstart:kvVbVb;" title="Beowulf against the Dragon by Andimayer on DeviantArt" rlhc="1">Beowulf against the Dragon by Andimayer ...<div class="fxgdke">deviantart.com</div></a>
driver.close()
driver.quit()