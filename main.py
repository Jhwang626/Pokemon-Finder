import urllib.request
import json
import requests
url = "https://pokeapi.co/api/v2/"

trace ("Calling", URL)
response = requests.get(URL) # Get data from the URL
response.raise_for_status()

data = response.json()
trace ("\nText returned:", response.text)

trace ("\nHere are all the kay/value pairs in the JSON response:")
for key, value in data.items():
  trace (key, ": ", value)

print(f"Here's a couple choices:{data['activity']}")




