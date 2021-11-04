from wikitools import wiki
from wikitools import api

# create a Wiki object
site = wiki.Wiki("http://wiki.coxarchitecture-workshop.com/wiki/api.php") 
# login - required for read-restricted wikis
site.login("s-abutler", "maneshisan6248")
# define the params for the query
params = {'action':'query', 'titles':'Json'}
# create the request object
request = api.APIRequest(site, params)
# query the API
result = request.query()