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
        self._name = name
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

    def get_attack_name(self):
        # Returns name of attack
        return self._name

    def get_sides_of_die(self):
        return self._sides

    def get_number_of_die(self):
        return self._number


class Adventurer:

    # Encapsulates the concept of an adventurer
    def __init__(self, name, hit_points, defense, magic_defense, initiative):
        self._name = name
        self._hit_points = hit_points
        self._defense = defense
        self._magic_defense = magic_defense
        self._initiative = initiative

    def is_alive(self):
        return self.hit_points > 0

    def roll_initiative(self):
        return random.randint(0, self._initiative)

    def get_name(self):
        return self._name

    def get_hit_points(self):
        return self._hit_points

    def get_defense(self):
        return self._defense

    def get_mag_defense(self):
        return self._magic_defense

    def get_initiative(self):
        return self._initiative

    def take_damage(self, amount, damage_type):

        # Physical, reduce hit_points by amount - defense
        if damage_type == 'physical':
            # Checks if physical damage is > 0
            amount = amount - self._defense
            if amount > 0:
                self._hit_points -= amount
                if self._hit_points < 0:
                    self._hit_points = 0
                    print("{} suffers {} {} damage! Hit Points: {}".format(
                        self._name, amount, damage_type, self._hit_points))
                else:
                    amount = 0
                    print("{} suffers {} damage! Hit Points: {}".format(
                        self._name, amount, self._hit_points))
            else:
                amount = 0
        elif damage_type == 'magic':
            # Checks if magic damage is > 0
            amount = amount - self._magic_defense
            if amount > 0:
                self._hit_points -= amount
                # Checks if hit points is negative after taking damage
                if self._hit_points < 0:
                    self._hit_points = 0
                    print("{} suffers {} {} damage! Hit Points: {}".format(
                        self._name, amount, damage_type, self._hit_points))
            else:
                amount = 0
                print("{} suffers {} {} damage! Hit Points: {}".format(
                    self._name, amount, damage_type, self._hit_points))


class Fighter(Adventurer):
    _HP = 40
    _DEF = 10
    _MAG_DEF = 4

    def __init__(self, name, initiative):
        super().__init__(name, Fighter._HP, Fighter._DEF, Fighter._MAG_DEF, initiative)
        self._melee = Attack("Slash", 1, 8, "physical")

    def strike(self):
        # Calculates and returns information about a physical strike from this object
        # Returns a tuple consisting damage_value and damage_type
        self.damage_type = self._melee.get_attack_type()
        self.damage_value = self._melee.get_damage()
        print(self._name + 'attacks with' + self._melee.get_attack_name()
              + "for" + str(self.damage_value) + self.damage_type + "damage")
        return (self.damage_value, self.damage_type)

    def __str__(self):
        return (self.name + ' with ' + str(self.self_HP) + ' hit points and a ' +
                self._melee.get_attack_name() + ' attack (' +
                str(self._melee.get_number_of_die()) +
                'd' + str(self._melee.get_sides_of_die()))


class Wizard(Adventurer):
    _HP = 20
    _DEF = 4
    _MAG_DEF = 10

    def __init__(self, name, initiative):
        super().__init__(name, Wizard._HP, Wizard._DEF, Wizard._MAG_DEF, initiative)
        self._spell = Attack("Fireball", 3, 6, "magic")

    def cast(self):
        # Calculates and returns information about a magical strike form this object
        # Returns a tuple consisting damage_value and damage_type
        self.damage_type = self._spell.get_attack_type()
        self.damage_value = self._spell.get_damage()
        print(self._name + 'attacks with' self._spell.get_attack_name()
              + "for" + str(self.damage_value) + self.damage_type + "damage")
        return (self.damage_value, self.damage_type)

    def __str(self):
        return (self.name + ' with ' + str(self.self_HP) + ' hit points and a ' +
                self._spell.get_attack_name() + ' attack (' +
                str(self._spell.get_number_of_die() +
                    'd' + str(self._spell.get_sides_of_die())))


if __name__ == "__main__":
    # Create the Fighter
    a = Fighter("Aragorn", 20)
    print("Created: ", a)

    # Create the Wizard
    b = Wizard("Gandalf", 20)
    print("Created: ", b)

    # Creates variable to keep track of rounds of combat
    rounds_tracker = 0
    while a.is_alive() == b.is_alive():
        print("Test")
