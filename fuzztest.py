from fuzzywuzzy import process


choices = ["Toilet", "Bathroom", "WC", "Water Closet", "Library", "Green Room", "Store"]

choice = process.extract("stor", choices, limit=3)

import requests
import json
app_id = "65785464"
app_key = "6908068c1a9947e37795818c32519712"
language = "en-gb"
word_id = choice[0][0]
url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
# data = {"id": "water_closet", "metadata": {"operation": "retrieve", "provider": "Oxford University Press", "schema": "RetrieveEntry"}, "results": [{"id": "water_closet", "language": "en-gb", "lexicalEntries": [{"entries": [{"pronunciations": [{"audioFile": "https://audio.oxforddictionaries.com/en/mp3/water_closet_1_gb_1.mp3", "dialects": ["British English"], "phoneticNotation": "IPA"}], "senses": [{"definitions": ["a flush toilet."], "domainClasses": [{"id": "plumbing", "text": "Plumbing"}], "id": "m_en_gbus1143280.005", "registers": [{"id": "dated", "text": "Dated"}], "semanticClasses": [{"id": "lavatory", "text": "Lavatory"}], "shortDefinitions": ["flush toilet"], "subsenses": [{"definitions": ["a room containing a flush toilet."], "id": "m_en_gbus1143280.008", "semanticClasses": [{"id": "lavatory", "text": "Lavatory"}], "shortDefinitions": ["room containing flush toilet"]}], "synonyms": [{"language": "en", "text": "lavatory"}, {"language": "en", "text": "bathroom"}, {"language": "en", "text": "facilities"}, {"language": "en", "text": "urinal"}, {"language": "en", "text": "privy"}, {"language": "en", "text": "latrine"}, {"language": "en", "text": "outhouse"}], "thesaurusLinks": [{"entry_id": "toilet", "sense_id": "t_en_gb0014957.001"}]}]}], "language": "en-gb", "lexicalCategory": {"id": "noun", "text": "Noun"}, "text": "water closet"}], "type": "headword", "word": "water closet"}], "word": "water closet"}
data = r.json()
# print(json.dumps(r.json()))
# print(json.dumps(r.json()["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["synonyms"]))
# print(json.dumps(data))
for result in data["results"]:
	for lexicalEntry in result["lexicalEntries"]:
		if lexicalEntry["lexicalCategory"]["id"] == "noun":
			for entry in lexicalEntry["entries"]:
				for sense in entry["senses"]:
					# for definition in sense["definitions"]:
						# print(definition)
					domains = ""
					for domainClass in 
					if "synonyms" in sense:
						for synonym in sense["synonyms"]:
							print(synonym["text"])
					if "subsenses" in sense:
						for subsense in sense["subsenses"]:
							if "synonyms" in subsense:
								for synonym in subsense["synonyms"]:
									print(synonym["text"])
					else:
						print(sense)
						for k in sense: print(k)