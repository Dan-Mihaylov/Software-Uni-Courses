class Controller:

    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *players) -> str:

        successfully_added = []

        for player in players:
            if player not in self.players:
                self.players.append(player)
                successfully_added.append(player.name)

        return f"Successfully added: {', '.join(successfully_added)}"

    def add_supply(self, *supplies) -> None:
        self.supplies.extend(supplies)

    def __take_last_supply(self, supply_type: str):

        for i in range(len(self.supplies) - 1, -1, -1):
            if self.supplies[i].__class__.__name__ == supply_type:
                return self.supplies.pop(i)

        if supply_type in ["Food", "Water"]:
            raise Exception(f"There are no {supply_type.lower()} supplies left!")

    def __find_player_by_name(self, name: str):
        for player in self.players:
            if player.name == name:
                return player

    def sustain(self, player_name: str, sustenance_type: str):

        player = self.__find_player_by_name(player_name)
        if player.stamina == 100:
            return f"{player.name} have enough stamina."

        supply = self.__take_last_supply(sustenance_type)
        if supply:
            if player.stamina + supply.energy > 100:
                player.stamina = 100
            else:
                player.stamina += supply.energy
            return f"{player_name} sustained successfully with {supply.name}."

    @staticmethod
    def __attack(player_one, player_two) -> str or None:

        if player_two.stamina - player_one.stamina / 2 < 0:
            player_two.stamina = 0

        else:
            player_two.stamina -= (player_one.stamina / 2)

        if player_one.stamina - (player_two.stamina / 2) < 0:
            player_one.stamina = 0

        else:
            player_one.stamina -= (player_two.stamina / 2)

        if player_one.stamina < player_two.stamina:
            return f"Winner: {player_two.name}"

        else:
            return f"Winner: {player_one.name}"

    @staticmethod
    def __check_if_the_players_cannot_duel(*players) -> str or None:

        result = []
        for player in players:

            if player.stamina == 0:
                result.append(f"Player {player.name} does not have enough stamina.")

        if result:
            return '\n'.join(result)

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = self.__find_player_by_name(first_player_name)
        second_player = self.__find_player_by_name(second_player_name)

        result = self.__check_if_the_players_cannot_duel(first_player, second_player)
        if result:
            return result

        if first_player.stamina < second_player.stamina:
            return self.__attack(first_player, second_player)
        else:
            return self.__attack(second_player, first_player)

    def next_day(self) -> None:

        for player in self.players:
            if player.stamina - (player.age * 2) < 0:
                player.stamina = 0
            else:
                player.stamina -= (player.age * 2)

        for player in self.players:
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self) -> str:

        info = []

        for player in self.players:
            info.append(str(player))

        for supply in self.supplies:
            info.append(supply.details())

        return "\n".join(info)
