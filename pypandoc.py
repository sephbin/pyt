import pypandoc
pageT = open('text.htm','r')
page = pageT.read()
pageT.close()
output = pypandoc.convert_text(page, 'mediawiki', format='html')
print output