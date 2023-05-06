from pymongo import MongoClient

# Connect to MongoDB
mongoClient = MongoClient("mongodb://localhost/pokemon")

# Access the "pokemondb" database
pokemonDB = mongoClient['pokemondb']

# Create a collection named "pokemon_data"
pokemonColl = pokemonDB['pokemon_data']

# QUERY 1: Write a query that returns all the Pokemon named "Pikachu". (1pt)
print()
print("Executing Query1... : ", end= "\n\n")

# Defining the query. Finding all pokemon with the name "Pikachu"
pickachuQuery = {
    "name": "Pikachu"
}

# Execute the query.
pickachuQueryResults = pokemonColl.find(pickachuQuery)

# Processing the query results.
for pokemons in pickachuQueryResults:
    print(pokemons)

print("\nFinished Printing Query1", end ="\n\n\n")


# Query 2: Write a query that returns all the Pokemon with an attack greater than 150. (1pt)
print()
print("Executing Query2... : ", end= "\n\n")

# Defining the query. Finding all pokemon with attack greater than 150
attackGreaterThan150 = {
    "attack": {"$gt": 150}
}

# Execute the query.
findAttackGreaterThan150 = pokemonColl.find(attackGreaterThan150)

# Processing the query results.
for pokemonsAttack in findAttackGreaterThan150:
    print(pokemonsAttack)

print("\nFinished Printing Query2", end="\n\n\n")

# Query 3: Write a query that returns all the Pokemon with an ability of "Overgrow" (1pt)

print()
print("Executing Query3... : ", end= "\n\n")

# Defining the query. Finding all pokemon with an ability of "Overgrow"
abilitiesOvergrow = {
    "abilities": {"$regex": "Overgrow"}
}

# Execute the query.
findAbilitiesOvergrow = pokemonColl.find(abilitiesOvergrow)

# Processing the query results.
for pokemonsAbilities in findAbilitiesOvergrow:
    print(pokemonsAbilities)

print("\nFinished Printing Query3", end="\n\n\n")

# Closing the client.
mongoClient.close()



