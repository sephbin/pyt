from fuzzywuzzy import fuzz
from fuzzywuzzy import process


choices = ["Premium", "Toilet", "Study", "General", "Stair", "Plant"]
fuzzresults = process.extract("Generl Plnt", choices, limit=5)

print(fuzzresults)
for f in fuzzresults:
	if f[1] > 50:
		print(f[0])

from word_forms.word_forms import get_word_forms

		print(get_word_forms("premium"))