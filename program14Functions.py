####################################################################
"""
Developer: Julian Cotto
Date: 12/10/2023
File Name: program14Functions.py
Description: This file contains the functions used in program14
"""
####################################################################
from program14Classes import CupRoll
from program14Classes import Iterator
from program14Classes import ResultFilter


def getProgPurpose():
    print("This program calculates the probability of rolling the same number on 5 standard 6-sided dice\n"
          "The program runs this experiment 100 times for a total of 1 million rolls and returns the average\n"
          "probability across each 100,000 iterations of dice rolls and calculates the difference between the\n"
          "Empirical Probability and Theoretical Probability")


def runExperiment():
    cup_roll = CupRoll()
    iterator = Iterator(cup_roll)
    results = iterator.run()
    result_filter = ResultFilter(results)
    same_number_results = result_filter.filter()
    numSame = len(same_number_results)
    actualProb = (len(same_number_results) / 100000) * 100
    statProb = (1/1296) * 100
    difference = actualProb - statProb
    return numSame, actualProb, statProb, difference


def getMain():
    iterations = 100
    experiments = []
    for i in range(0, iterations):
        print("Running Iteration " + str(i))
        numSame, actualProb, statProb, difference = runExperiment()
        experiments.append([numSame, actualProb, statProb, difference])
    numSameAvg = None
    actualProbAvg = None
    statProbAvg = None
    differenceAvg = None

    for i in range(len(experiments)):
        numSameAvg = sum(experiment[0] for experiment in experiments) / iterations
        actualProbAvg = sum(experiment[1] for experiment in experiments) / iterations
        statProbAvg = sum(experiment[2] for experiment in experiments) / iterations
        differenceAvg = sum(experiment[3] for experiment in experiments) / iterations

    print("\nAverage Occurrences:", numSameAvg)
    print("Average Actual Probability:", actualProbAvg)
    print("Average Calculated Probability:", statProbAvg)
    print("Average Difference:", differenceAvg)


def outro():
    print("Thank you for running the program - Julian Cotto")
    input("\nPress Enter to Exit...")
