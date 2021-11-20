import requests
import json

jsonFiles = [
  'https://github.com/raspberrypisig/corpora/raw/master/custom/countries.json',
  'https://github.com/raspberrypisig/corpora/raw/master/custom/animals.json',
  'https://github.com/raspberrypisig/corpora/raw/master/custom/fruits.json',
  'https://github.com/raspberrypisig/corpora/raw/master/custom/vegetables.json'
]

currentJsonFile = jsonFiles[3]

r = requests.get(currentJsonFile)
countries = r.json()
#print(countries)
restricted_countries = list(filter(lambda c: len(c) <= 10, countries))
#print(restricted_countries)
print(json.dumps(restricted_countries, indent=4))
