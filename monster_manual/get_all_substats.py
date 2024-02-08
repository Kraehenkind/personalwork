'''
Script to get all types of stats, like speed types or armor types.
Multidatastats will be converted into sets, for planning the DB.
'''

import json
import pprint

#print-command
pp = pprint.PrettyPrinter(indent=4)

#list for opening multiple files by name:
all_file_names = []

with open("all_monsters.json", "r", encoding="utf-8") as file:
    whole_data_set = json.load(file)
    for i in whole_data_set["results"]:
        all_file_names.append(i["url"][14:])

#sets for found values

armor_types = set()
armors = set()
movement_types = set()
skills = set()
dmg_types = set()
conditions = set()
languages = set()
special_abilities = []
basic_actions_content = set()
usage_types = set()
usage_details = set()
usage_roll_values = set()
legendary_substats = set()
reactions = set()
forms = set()


# loop for opening all files one-by-one

for i in all_file_names:
    with open(f"all monsters/{i}.json") as file:
        monster_stats = json.load(file)

        # get all armor types and names

        for armorstat in monster_stats["armor_class"]:
            armor_types.add(armorstat["type"])
            if armorstat["type"] == "spell":
                armors.add(armorstat["spell"]["name"])
            try:
                for specific_armor in armorstat["armor"]:
                    armors.add(specific_armor["name"])
            except:
                pass

        #get all movement_types

        for type in monster_stats["speed"]:
            movement_types.add(type)

        #get all skills/proficiencies

        for skill in monster_stats["proficiencies"]:
            # get rid of "Skill: " start
            if skill["proficiency"]["name"].startswith("Skill: "):
                shortskill = skill["proficiency"]["name"][7:]
                skills.add(shortskill)
                continue
            skills.add(skill["proficiency"]["name"])

        # get all languages

        for language in monster_stats["languages"].split(", "):
            if language == "":
                continue
            elif language.startswith("and "):
                language = language[4:]
            elif " plus " in language:
                all_languages = language.split(" plus ")
                languages.add(all_languages[0])
                languages.add(all_languages[1])
                continue
            languages.add(language)

        # get all dmg_types for vulnerabilities,immunities, etc.

        for dmg_type in monster_stats["damage_vulnerabilities"]:
            dmg_types.add(fr"{dmg_type}")
        for dmg_type in monster_stats["damage_resistances"]:
            dmg_types.add(fr"{dmg_type}")
        for dmg_type in monster_stats["damage_immunities"]:
            dmg_types.add(fr"{dmg_type}")

        # get all conditions for condition immunitites

        for condition in monster_stats["condition_immunities"]:
            conditions.add(condition["name"])

        # get all special abilities
            
        for special in monster_stats["special_abilities"]:
            special_abilities.append({special["name"]:special["desc"]})
            ohne_dopplungen_values = set()
            ohne_dopplungen_keys = set()
            for x in special_abilities:
                for key,value in x.items():
                    ohne_dopplungen_keys.add(key)
                    ohne_dopplungen_values.add(value)
            
            # print("Alle Abilities:",len(special_abilities))
            # print("Ohne Dopplungen:", len(ohne_dopplungen))

        # get all actions
                    
        basic_actions_content= {"name","desc","attack_bonus","dc","usage"}
        
        for kind in monster_stats["actions"]:
            if "usage" in kind.keys():
                usage_types.add(kind["usage"]["type"])
                for i in kind["usage"]:
                    usage_details.add(i)
                if "min_value" in kind["usage"]:
                    usage_roll_values.add(kind["usage"]["dice"])

        if "legendary_actions" in monster_stats:
            for legendary in monster_stats["legendary_actions"]:
                for substat in legendary:
                    legendary_substats.add(substat)
            
        if "reactions" in monster_stats:
            for reaction_type in monster_stats["reactions"]:
                #print(reaction_type)
                pass
        
        if "forms" in monster_stats:
            print(monster_stats["index"])
            for form in monster_stats["forms"]:
                print(form)

"""
still to-do:

    "forms": []
    "senses": {}

"""


# print(armors)
# print(armor_types)
# print(movement_types)
# print(skills)
# pp.pprint(dmg_types)
# print(conditions)
# print(languages)
# pp.pprint(special_abilities)
# pp.pprint(ohne_dopplungen_keys)
# print("Ohne Dopplungen:", len(ohne_dopplungen_keys),":",len(ohne_dopplungen_values))
# pp.pprint(basic_actions_content)
# pp.pprint(usage_types)
# pp.pprint(usage_details)
# pp.pprint(usage_roll_values)
# pp.pprint(legendary_substats)
