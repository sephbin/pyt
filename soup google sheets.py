from bs4 import BeautifulSoup
import requests
import re
import json
# print("tempFFESchedule")
#### Standard Request
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQDy9AQEnd97e-lK_jXEuZ94CQv1oBR2dUvzcZvr6Jx3quUAXayhm_kHDeG-xnRhurOMGsbA4DFD8Kv/pubhtml?gid=1458703766&single=true'
# html = requests.get(url, headers=headers ).text


soup = BeautifulSoup(html, 'html.parser')
# regex = re.compile(r'^/.')
# rows = soup.find_all('a', attrs={'href': regex})
table = soup.find('tbody')
rows = table.find_all('tr')
# print(rows)
# del rows[0]
headers = {}
data= []
ignore = ["Image",]
for row_index, r in enumerate(rows):
	# print(r)
	cells = r.find_all('th')
	cells += r.find_all('td')
	apdata = {}
	for col_index, c in enumerate(cells):
		# print(c)
		append = False
		if "freezebar-cell" not in c.attrs["class"] and "row-header-shim" not in c.attrs["class"]:
			contents = c
			if "<div" in str(contents.encode_contents()):
				contents = c.find("div")
			if row_index == 0:
				cellcont = str(contents.contents[0])
				if cellcont not in ignore:
					headers[str(col_index)] = str(contents.contents[0])
			else:
				if str(col_index) in headers:
					key = headers[str(col_index)]
					cellcont = list(map(lambda x: str(x), contents.contents))
					cellcont = "<br/>".join(cellcont)
					if "<a" in cellcont:
						# cellcont = BeautifulSoup(cellcont, 'html.parser').find('a').attrs["href"]
						cellcont = BeautifulSoup(cellcont, 'html.parser').find('a').text
						print("<a>", cellcont)
					apdata[key] = cellcont
					append = True
					# print(contents.contents[0])
				# print(dir(contents))
	if append:
		data.append(apdata)