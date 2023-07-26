from project.hero import Hero
import unittest


class HeroTester(unittest.TestCase):

    def setUp(self) -> None:
        self.hero = Hero("Username", 1, 100.0, 10.0)
        """
        self.username = "Username"
        self.level = 1
        self.health = 100.0
        self.damage = 10.0
        """
        self.enemy_hero = Hero("Enemy", 1, 100.0, 10.0)
        """
        self.username = "Enemy"
        """

    def test__battle_heroes_with_same_name__raise_ex(self):

        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test__battle_hero_health_0_or_negative__raises_ex(self):

        for health in [-1, 0]:
            self.hero.health = health

            with self.assertRaises(ValueError) as ve:
                self.hero.battle(self.enemy_hero)

            self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test__battle_enemy_hero_health_0_or_negative__raises_ex(self):

        for health in [-1, 0]:
            self.enemy_hero.health = health

            with self.assertRaises(ValueError) as ve:
                self.hero.battle(self.enemy_hero)

            self.assertEqual(f"You cannot fight {self.enemy_hero.username}. He needs to rest", str(ve.exception))

    def test__battle_draw__return_draw(self):
        self.hero.level = 10
        self.enemy_hero.level = 10

        expected_result = "Draw"
        actual_result = self.hero.battle(self.enemy_hero)

        self.assertEqual(expected_result, actual_result)

        # where hero is negative and enemy is 0
        self.setUp()
        self.hero.level = 10
        self.enemy_hero.level = 20

        actual_result = self.hero.battle(self.enemy_hero)

        self.assertEqual(expected_result, actual_result, "Your health is negative")

        self.setUp()
        self.hero.level = 20
        self.enemy_hero.level = 10

        actual_result = self.hero.battle(self.enemy_hero)

        self.assertEqual(expected_result, actual_result, "Enemy hero health is negative")

    def test__battle_hero_wins__increase_stats_return_message(self):

        # wining with enemy on 0 health
        self.hero.level = 10

        expected_result = "You win"
        actual_result = self.hero.battle(self.enemy_hero)

        self.assertEqual(expected_result, actual_result)

        # wining with enemy on negative health
        self.setUp()
        self.hero.level = 20

        actual_result = self.hero.battle(self.enemy_hero)

        self.assertEqual(expected_result, actual_result)
        self.assertEqual(21, self.hero.level)
        self.assertEqual(95, self.hero.health)
        self.assertEqual(15.0, self.hero.damage)

    def test__battle_enemy_wins__increase_stats_return_message(self):
        # losing with hero on 0 health
        self.enemy_hero.level = 10

        expected_result = "You lose"
        actual_result = self.hero.battle(self.enemy_hero)

        self.assertEqual(expected_result, actual_result)

        # losing with hero on negative health
        self.setUp()
        self.enemy_hero.level = 20

        actual_result = self.hero.battle(self.enemy_hero)

        self.assertEqual(expected_result, actual_result)
        self.assertEqual(21, self.enemy_hero.level)
        self.assertEqual(95, self.enemy_hero.health)
        self.assertEqual(15.0, self.enemy_hero.damage)

    def test__str_representation__returns_correct_info(self):

        expected_result = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
                          f"Health: {self.hero.health}\n" \
                          f"Damage: {self.hero.damage}\n"
        actual_result = self.hero.__str__()

        self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    unittest.main()
