import random
import math

start = True
yahtzee_scorecard = {
    "Ones": None,
    "Twos": None,
    "Threes": None,
    "Fours": None,
    "Fives": None,
    "Sixes": None,
    "BONUS": 35,
    "Upper total": None,
    "Three of a kind": None,
    "Four of a kind": None,
    "Full house": None,
    "Small straight": None,
    "Large straight": None,
    "Yahtzee": None,
    "Chance": None,
    "Lower total": None,
    "GRAND TOTAL": None
}
start_menu = ("Start Menu",
"EmptyScorecard [a]",
"Instructions [i]",
"Game rules [g]",
"Understanding scorecard [u]",
"Quit [q]",
"Start [s]")
while True:
    for x in start_menu:
        print(x)
    all_input = (input("Your Input: "))
    if all_input.lower() == "a":
        print("\nEmpty Scorecard\n")
        for key, value in yahtzee_scorecard.items():
            print(f"{key}: {value}")
    elif all_input.lower() == "i": # once working use filehandling 
        instrustions = (" \nThe game consists of thirteen rounds and at the end of the thirteenth round then the game will end. (All the categories on the players’ score cards will be completely filled in at that point.)",
        "\nAt the start of a turn, the player takes all 5 dice and rolls them. They can then roll some or all of the dice up to two more times, setting aside any dice they’d like to keep and rerolling the rest. The dice can be scored after any of the rolls, but scoring the dice ends the player’s turn. Setting dice aside after one roll does not prevent one or more of them from being rolled again on any subsequent roll if the player so chooses.",
        "\nEach player’s goal is to try and score as high as they can in one of the thirteen categories shown on their score card.\n")
        for tup in instrustions:
            print(tup)
        ret = input("To return press R to start press S to quit press Q: ")
        if ret.lower() == "r":
            continue
        elif ret.lower() == "q":
            print("exiting")
            quit()
        elif ret.lower() == "s":
            break
    elif all_input.lower() == "g":
        yahtzee_rules = (
        ("\nObjective", "Gain points by rolling dice combinations, player with the highest total score after 13 rounds wins."),
        ("Number of Players", "1"),
        ("Game Rounds", "Yahtzee consists of thirteen rounds. Each player gets a turn per round."),
        ("Scoring", "The objective of the game is to collect as many points as possible through dice combinations rolled. In multiplayer, the player with the greatest total points at the end of the game is the winner."),
        ("How to Play", "Each turn gives a player 3 opportunities to roll the dice in order to score the highest number of points from dice combinations. After 3 rolls, mark your score or a zero on your score card in the corresponding column. You may stop after the first roll if you are satisfied with the outcome.")
        )
        for rule in yahtzee_rules:
            print(*rule)
        ret = input("To return press R to start press S to quit press Q: ")
        if ret.lower() == "r":
            continue
        elif ret.lower() == "q":
            print("exiting")
            quit()
        elif ret.lower() == "s":
            break
    elif all_input.lower() == "u":  # Need to Add understanding for lower section
        score_under = ("\nOnes: After your three rolls you add up the amount of ones you rolled.",
                   "Twos: After your three rolls you add up the number of twos you rolled.",
                   "Threes: After your three rolls you add up the number of Threes you rolled.",
                   "fours: After your three rolls you add up the number of fours you rolled.", 
                   "fives: After your three rolls you add up the number of fives you rolled.",
                   "sixes: After your three rolls you add up the number of sixes you rolled.\n",)
        for under in score_under:
            print(under)
        ret = input("To return press R to start press S to quit press Q: ")
        if ret.lower() == "r":
            continue
        elif ret.lower() == "q":
            print("exiting")
            quit()
        elif ret.lower() == "s":
            break
    elif all_input.lower() == "q":
        print("Exiting  ")
        quit()
    elif all_input.lower() == "s":
        break
