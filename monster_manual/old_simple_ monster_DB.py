import json
import sqlite3
import os

#list for opening multiple files by name:
all_file_names = []

with open("dnd_data.json", "r", encoding="utf-8") as file:
    whole_data_set = json.load(file)
    for i in whole_data_set["results"]:
        all_file_names.append(i["url"][14:])

#getting the keys to make in to column-names
with open("key_count.json", "r", encoding="utf-8") as file:
    all_keys = json.load(file)

#checking for datatypes, dropping list and dict:
key_variations = {}
    
for i in all_file_names:
    with open(f"all monsters/{i}.json") as file:
        check_value_file = json.load(file)
        for j in all_keys:
            try:
                if type(check_value_file[j]) == list:
                    continue
                elif type(check_value_file[j]) == dict:
                    continue
                else:
                    key_variations.setdefault(j, set())
                    key_variations[j].add(type(check_value_file[j]))
            except:
                continue

# changing the datatypes into SQL-conform str
values_types = []

for i in key_variations.values():
    type_str = (str(i)[9:-3])
    if type_str != "str":
        if len(type_str) > 4:
            values_types.append("FLOAT(4,3)")
        else:
            values_types.append("INTEGER")
    else:
        values_types.append("VARCHAR(50)")

#building list with all column-names and datatypes
columns = key_variations.keys()

columns_str = [i for i in map(lambda x: str(x[0])
                              +" "
                              +str(x[1]),zip(columns,values_types))][1:]

#CREATE TABLE sql-statement
table_creation_sql = f"""CREATE TABLE IF NOT EXISTS monsterlist ( 
    monster_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    {', '.join(columns_str)});"""

#create/open DB
db_path = "monster_manual.db"
with sqlite3.connect(db_path) as conn:
    cur = conn.cursor()

cur.execute(table_creation_sql)
conn.commit()

#opening Monsterfiles, getting the values
for i in all_file_names:
    with open(f"all monsters/{i}.json") as file:
        monster_stats = json.load(file)
    stat_values = []
    relevant_keys = [i for i in key_variations.keys()][1:]
    for key in relevant_keys:
        try:
            current_stat = monster_stats[key]
            stat_values.append(current_stat)
        except:
            stat_values.append("NULL")

#constructing strings for insert-sql-statement
    value_placeholder = f"{', '.join(['?']*(len(key_variations)-1))}"
    insert_sql = f"""INSERT INTO monsterlist 
        ({', '.join([*columns][1:])}) 
        Values ({value_placeholder});"""

#inserting values into db
    cur.execute(insert_sql,stat_values)
    conn.commit()