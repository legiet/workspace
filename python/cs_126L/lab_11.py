# Champ Foronda,
# CS 126L
# April 24th, 2018
# Lab 11 - Role-Playing Game

import random


class DiceRoller:
    # A ultility class for dice rolling.

    def roll(self, times, sides):
        # Rolls times number of sides-sided dice; returns the total
        total = 0
        for i in range(times):
            roll = random.randint(1, sides)
            total += roll
        return total

r = DiceRoller()


class Attack():
    # Encapsulates the concept of an attack

    def __init__(self, name, number_of_die, sides_of_die, damage_type):
        self._name = _name
        self._sides = sides_of_die
        self._number = number_of_die
        self._type = damage_type

    def get_attack_type(self):
        # Return attack type as a string
        return self._type

    def get_damage(self):
        # Rolls damage value and stores it into damage_value
        self.damage_value = r.roll(self._number, self._sides)
        return self.damage_value


class Adventurer:
    # Encapsulates the concept of an adventurer

    def __init__(self, name, hit_points, defense, magic_defense, initiative):
        pass

    def is_alive(self):
        pass

    def roll_initiative(self):
        pass

    def take_damage(self, amount, damage_type):
        pass


class Fighter(Adventurer):
    _HP = 40
    _DEF = 10
    _MAG_DEF = 4

    def __init__(self, name, initiative):
        super().__init__(name, Fighter._HP, Fighter._DEF, Fighter._MAG_DEF, initiative)
        self._melee = Attack("Slash", 1, 8, "physical")

    def strike(self):
        pass

    def __str__(self):
        pass


class Wizard(Adventurer):
    _HP = 20
    _DEF = 4
    _MAG_DEF = 10

    def __init__(self, name, initiative):
        pass

    def cast(self):
        pass

    def __str(self):
        pass


if __name__ == "__main__":
    a = Fighter("Aragorn", 20)
    print("Created: ", a)
