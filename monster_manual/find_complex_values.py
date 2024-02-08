"""
finding all Stats, that are not str/int/float and that 
therefore need "special attention"
"""

import json

#list for opening multiple files by name:
all_file_names = []

with open("dnd_data.json", "r", encoding="utf-8") as file:
    whole_data_set = json.load(file)
    for i in whole_data_set["results"]:
        all_file_names.append(i["url"][14:])

#getting the keys to make in to check datatypes
with open("key_count.json", "r", encoding="utf-8") as file:
    all_keys = json.load(file)

#gathering the values of non str/int/float:
key_variations = {}
    
for i in all_file_names:
    with open(f"all monsters/{i}.json") as file:
        check_value_file = json.load(file)
        for j in all_keys:
            try:
                if type(check_value_file[j]) == list:
                    key_variations.setdefault(j,[])
                elif type(check_value_file[j]) == dict:
                    key_variations.setdefault(j,{})
            except:
                continue

with open("complex_values_list.json", "w", encoding="utf-8") as file:
    json.dump(key_variations, file, indent=4)