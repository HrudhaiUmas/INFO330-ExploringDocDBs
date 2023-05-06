# EXTRA CREDIT Improve the Battle.py script. (2 pts)
# The algorithm in the Battle.py script is pretty lame.
# (Team Rocket is NOT known for its skills in evaluating Pokemon.)
# Improve it and commit the changes to this repository.
# Make sure to point out to your TA that you have improved it, so they can
# verify it and give you the extra point.

import random
from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']


def fetch(pokemonid):
    return pokemonColl.find_one({"pokedex_number": pokemonid})


print()


def battle(pokemon1, pokemon2):
    print("Let the Pokemon battle begin! ================")
    print("It's " + pokemon1['name'] + " vs " + pokemon2['name'])
    print()

    p1_advantage_counter = 0  # Counter for pokemon 1's advantages
    p2_advantage_counter = 0  # Counter for pokemon 2's advantages

    for stat in ['hp', 'attack', 'defense', 'speed', 'sp_attack', 'sp_defense']:
        if pokemon1[stat] > pokemon2[stat]:
            print(pokemon1['name'] + " has the advantage in " + stat)
            p1_advantage_counter += 1
        elif pokemon2[stat] > pokemon1[stat]:
            print(pokemon2['name'] + "'s " + stat + " is superior")
            p2_advantage_counter += 1
        else:
            print("Both Pokémon have equal " + stat)

    print()

    if p1_advantage_counter > p2_advantage_counter:
        print("Battle results: " + pokemon1['name'] + " wins!")
        print("Final score:\n" + pokemon1['name'] + ": " + str(p1_advantage_counter) + "\n" + pokemon2['name'] + ": "
              + str(p2_advantage_counter))
    elif p2_advantage_counter > p1_advantage_counter:
        print("Battle results: " + pokemon2['name'] + " wins!")
        print("Final score:\n" + pokemon2['name'] + ": " + str(p2_advantage_counter) + "\n" + pokemon1[
            'name'] + ":" + str(p1_advantage_counter) )
    else:
        print("It's a tie!")

    print()


def main():
    # Fetch two pokemon from the MongoDB database
    pokemon1 = fetch(random.randrange(801))
    pokemon2 = fetch(random.randrange(801))

    # Pit them against one another
    battle(pokemon1, pokemon2)


main()
