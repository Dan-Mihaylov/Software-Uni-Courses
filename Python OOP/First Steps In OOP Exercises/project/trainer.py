from project.pokemon import Pokemon

class Trainer:

    def __init__(self, name: str, pokemons=[]):
        self.name = name
        self.pokemons = pokemons

    def add_pokemon(self, pokemon: Pokemon):

        for pok in self.pokemons:
            if pok.name == pokemon.name:
                return f"This pokemon is already caught"
                break

        else:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str):

        for pok in self.pokemons:
            if pok.name == pokemon_name:
                self.pokemons.remove(pok)
                return f"You have released {pokemon_name}"
                break

        else:
            return f"Pokemon is not caught"

    def trainer_data(self):

        result = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}\n"

        for pokemon in self.pokemons:
            result += f"- {pokemon.pokemon_details()}\n"

        return result


# pokemon = Pokemon("Pikachu", 90)
# print(pokemon.pokemon_details())
# trainer = Trainer("Ash")
# print(trainer.add_pokemon(pokemon))
# second_pokemon = Pokemon("Charizard", 110)
# print(trainer.add_pokemon(second_pokemon))
# print(trainer.add_pokemon(second_pokemon))
# print(trainer.release_pokemon("Pikachu"))
# print(trainer.release_pokemon("Pikachu"))
# print(trainer.trainer_data())
