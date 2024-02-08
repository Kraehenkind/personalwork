import json
from urllib import request
import ssl

context = ssl._create_unverified_context()

url = "https://www.dnd5eapi.co/api/"

response = request.urlopen(url, context=context)

dnd_data = json.load(response)

all_keys = {}

for i in dnd_data:
    api_name = dnd_data[i]
    url = "https://www.dnd5eapi.co"+api_name
    response = request.urlopen(url, context=context)
    current_api = json.load(response)
    with open(f"/home/madhatter/Schreibtisch/MosterDB/all apis/{api_name[5:]}.json", "w", encoding="utf-8") as file:
        json.dump(current_api, file, indent=4)
