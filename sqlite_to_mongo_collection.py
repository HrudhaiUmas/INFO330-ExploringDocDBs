import sqlite3
from pymongo import MongoClient

import secrets
import string

id_length = 10

# Establish a connection to the SQLite database
conn = sqlite3.connect("pokemon.sqlite")
# Create a cursor object
cursor = conn.cursor()

# Execute the SQL query to retrieve the desired information for all rows
cursor.execute("SELECT name, pokedex_number, type1, type2, hp, attack, defense, speed, sp_attack, sp_defense, abilities FROM imported_pokemon_data")

# Fetch all the results
pokemon_rows = cursor.fetchall()

# Close the cursor and the database connection
cursor.close()
conn.close()

# Create a list to store the JSON structures for all Pokémon
pokemon_list = []

# Iterate over the rows and create JSON structures for each Pokémon
for row in pokemon_rows:
    alphanumeric = string.ascii_letters + string.digits
    random_id = ''.join(secrets.choice(alphanumeric) for _ in range(id_length))

    pokemon_json = {
        "_id": random_id,
        "name": row[0],
        "pokedex_number": int(row[1]),
        "types": [row[2], row[3]],
        "hp": int(row[4]),
        "attack": int(row[5]),
        "defense": int(row[6]),
        "speed": int(row[7]),
        "sp_attack": int(row[8]),
        "sp_defense": int(row[9]),
        "abilities": row[10]
    }
    pokemon_list.append(pokemon_json)

# Print the list of Pokémon JSON structures
print(pokemon_list)

# Establish a connection to MongoDB
mongoClient = MongoClient("mongodb://localhost/pokemon")

# Access the "pokemondb" database
pokemonDB = mongoClient['pokemondb']

# Create a collection named "pokemon_data"
pokemonColl = pokemonDB['pokemon_data']

# Insert the Pokemon JSON data into the collection
pokemonColl.insert_many(pokemon_list)  # Assuming "pokemon_list" contains the JSON data

# Confirm the data has been inserted successfully
print("Data inserted into the 'pokemon_data' collection.")

