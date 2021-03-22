'''
    6. Pokemon Battle
You are tasked to create two classes: a Pokemon class and a Trainer class.
The Pokemon class should receive a name (string) and health (int) upon initialization.
It should also have a method called pokemon_details that returns the information of the pokemon:
"{pokemon_name} with health {pokemon_health}"
The Trainer class should receive a name (string).
The Trainer should also have an attribute pokemon (list, empty by default). The Trainer has three methods:
    • add_pokemon(pokemon: Pokemon)
        ◦ Add the pokemon to the collection. After adding the pokemon, it should return "Caught {pokemon_name}
        with health {pokemon_health}". Note: use the pokemon's details method.
        ◦ If the pokemon is already in the collection, it should return "This pokemon is already caught"
    • release_pokemon(pokemon_name: String)
        ◦ Check if you have a pokemon with the name and remove it from the collection.
        It should return "You have released {pokemon_name}"
        ◦ If there isn't a pokemon with that name in the collection, return "Pokemon is not caught"
    • trainer_data()
        ◦ The method returns the information of the trainer with his pokemon in this format:
"Pokemon Trainer {trainer_name}
 Pokemon count {the amount of pokemon caught}
 - {pokemon_details}
 ...
 - {pokemon_details}
"
'''
class Pokemon:

    def __init__(self, name, health):

        self.name = name
        self.health = health

    def pokemon_details(self):

        return f"{self.name} with health {self.health}"

class Trainer:

    def __init__(self, name):

        self.name = name
        self.pokemon_list = []

    def add_pokemon(self, pokemon_to_add):

        if pokemon_to_add in self.pokemon_list:

            return "This pokemon is already caught"

        self.pokemon_list.append(pokemon_to_add)

        return f"Caught {pokemon_to_add.name} with health {pokemon_to_add.health}"

    def release_pokemon(self, pokemon_name):

        for pokeman in self.pokemon_list:

            if pokeman.name == pokemon_name:

                self.pokemon_list.remove(pokeman)

                return f"You have released {pokemon_name}"

        return "Pokemon is not caught"

    def trainer_data(self):

        trainer_data = f"Pokemon Trainer {self.name}\n" + f"Pokemon count {len(self.pokemon_list)}\n"

        for pokeman in self.pokemon_list:

            trainer_data = trainer_data + "- " + pokeman.pokemon_details() + "\n"

        return trainer_data

pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())