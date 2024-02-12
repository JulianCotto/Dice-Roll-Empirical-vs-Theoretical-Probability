####################################################################
"""
Developer: Julian Cotto
Date: 12/10/2023
File Name: program14Classes.py
Description: This file contains the classes used in the program14
"""
####################################################################
import random


class CupRoll:
    def __init__(self):
        self.dice = [0] * 5
        self.sides = 6

    def roll(self):
        self.dice = [random.randint(1, self.sides) for _ in range(5)]
        return self.dice

    def reroll(self, dice_to_reroll):
        if dice_to_reroll > 5 or dice_to_reroll < 0:
            return "Invalid number of dice to reroll. Please enter a number between 0 and 5."
        else:
            for i in range(dice_to_reroll):
                self.dice[i] = random.randint(1, self.sides)
            return self.dice

    def get_results(self):
        return self.dice


class Iterator:
    def __init__(self, cup_roll):
        self.cup_roll = cup_roll
        self.results = []

    def run(self):
        for _ in range(100000):
            self.cup_roll.roll()
            self.results.append(self.cup_roll.get_results())
        return self.results


class ResultFilter:
    def __init__(self, results):
        self.results = results

    def filter(self):
        same_number_results = []
        for result in self.results:
            if len(set(result)) == 1:
                same_number_results.append(result)
        return same_number_results
