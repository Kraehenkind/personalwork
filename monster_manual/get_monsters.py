"""
Getting the list of all monsters, then getting all 
stats of those and turning them into jsons
"""

import json
from urllib import request
import ssl

context = ssl._create_unverified_context()

url = "https://www.dnd5eapi.co/api/monsters/"

response = request.urlopen(url, context=context)

dnd_data = json.load(response)

with open("all_monsters.json", "w", encoding="utf-8") as file:
    json.dump(dnd_data, file, indent=4)

all_keys = {}

for i in dnd_data["results"]:
    monster_name = i["url"]
    url = "https://www.dnd5eapi.co"+monster_name
    response = request.urlopen(url, context=context)
    current_monster = json.load(response)
    for j in current_monster:
        all_keys.setdefault(j,0)
        if type(current_monster[j]) is not str and type(current_monster[j]) is not int:
            all_keys[j] +=1
        with open(f"{monster_name[14:]}.json", "w", encoding="utf-8") as file:
            json.dump(current_monster, file, indent=4)
with open("key_count.json", "w", encoding="utf-8") as file:
    json.dump(all_keys, file, indent=4)