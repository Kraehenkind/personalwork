'''
Program to get all values for the 1:n tables, which is the basic
data for the monster manual. Those values will than be written to 
the DB on the server. (DB allready exists)
allready done parts commented out
'''

import json
import paramiko
import pymysql
from sshtunnel import SSHTunnelForwarder

#list for opening multiple files by name:
all_file_names = []

with open("all_monsters.json", "r", encoding="utf-8") as file:
    whole_data_set = json.load(file)
    for i in whole_data_set["results"]:
        all_file_names.append(i["url"][14:])

#sets for found values

#armor_types = set()
#armors = set()
movement_types = set()
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
skills = set()

for i in all_file_names:
    with open(f"all monsters/{i}.json") as file:
        monster_stats = json.load(file)

        # get all armor types and names

        # for armorstat in monster_stats["armor_class"]:
        #     armor_types.add(armorstat["type"])
        #     if armorstat["type"] == "spell":
        #         armors.add(armorstat["spell"]["name"])
        #     try:
        #         for specific_armor in armorstat["armor"]:
        #             armors.add(specific_armor["name"])
        #     except:
        #         pass

        #get all movement_types

        for type in monster_stats["speed"]:
            movement_types.add(type)

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

        # get all special abilities
            
        for special in monster_stats["special_abilities"]:
            special_abilities.append({special["name"]:special["desc"]})
            ohne_dopplungen_values = set()
            ohne_dopplungen_keys = set()
            for x in special_abilities:
                for key,value in x.items():
                    ohne_dopplungen_keys.add(key)
                    ohne_dopplungen_values.add(value)

# SSH Connection Details
ssh_host = '192.168.0.105'
ssh_port = 22
ssh_user = 'kraehenkind'
ssh_key_path = '/home/madhatter/.ssh/home_server.key'

# DB Connection Details
db_host = '192.168.0.105'
db_user = 'kraehenkind'
db_password = 'trem667re'
db_name = 'monster_manual'

# SSH connection with private key
private_key = paramiko.RSAKey(filename=ssh_key_path)
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(ssh_host, ssh_port, ssh_user, pkey=private_key)

# Create an SSH tunnel to the MariaDB server

ssh_tunnel = SSHTunnelForwarder(
    "192.168.0.105",
    ssh_username= "kraehenkind",
    ssh_password= "trem667re",
    remote_bind_address= ("127.0.0.1", 3306)
)

ssh_tunnel.start()

# Connect to DB via SSH tunnel

db_connection = pymysql.connect(
    host='localhost',
    port=ssh_tunnel.local_bind_port,
    user=db_user,
    password=db_password,
    database=db_name,
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

# SQL-Statement for armor_types and data:
# armor_types_sql = "INSERT INTO armor_types (type_name) VALUES (%s)"
# armor_types_data = [(i,) for i in armor_types]

# SQL-Statement for Armors:
# armors_sql = "INSERT INTO armors (armor) VALUES (%s)"
# armors_data = [(i,) for i in armors]

#SQL-Statement for movement types
movement_types_sql = "INSERT INTO movement_types (movement_type) VALUES (%s)"
movement_types_data = [(i,) for i in movement_types]

#SQL-Statement for damage types
damage_types_sql = "INSERT INTO damage_types (damage_type) VALUES (%s)"
damage_types_data = [(i,) for i in dmg_types]

#SQL-Statement for conditions
conditions_types_sql = "INSERT INTO conditions (condition) VALUES (%s)"
conditions_types_data = [(i,) for i in conditions]

with db_connection.cursor() as cursor:
    pass
    # Parts that are done:
    # cursor.executemany(armor_types_sql, armor_types_data)
    # cursor.executemany(armors_sql, armors_data)

db_connection.commit()
db_connection.close()
ssh_tunnel.stop()
ssh_client.close()

