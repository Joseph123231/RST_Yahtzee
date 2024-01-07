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
print("""
 _       __     __                             __           __  __      __    __                
| |     / /__  / /________  ____ ___  ___     / /_____      \\ \\/ /___ _/ /_  / /_____  ___  ___ 
| | /| / / _ \\/ / ___/ __ \\/ __ `__ \\/ _ \\   / __/ __ \\      \\  / __ `/ __ \\/ __/_  / / _ \\/ _ \\
| |/ |/ /  __/ / /__/ /_/ / / / / / /  __/  / /_/ /_/ /      / / /_/ / / / / /_  / /_/  __/  __/
|__/|__/\\___/_/\\___/\\____/_/ /_/ /_/\\___/   \\__/\\____/      /_/\\__,_/_/ /_/\\__/ /___/\\___/\\___/
""")

while True:
    for x in start_menu:
        print(x)
    all_input = (input("Your Input: "))
    if all_input.lower() == "a":
        print("\nEmpty Scorecard\n")
        for key, value in yahtzee_scorecard.items():
            print(f"{key}: {value}")
            ret = input("To return press R to start press S to quit press Q: ")
        if ret.lower() == "r":
            continue
        elif ret.lower() == "q":
            print("exiting")
            quit()
        elif ret.lower() == "s":
            break
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
        ret = input("\nTo return press R to start press S to quit press Q: ")
        if ret.lower() == "r":
            continue
        elif ret.lower() == "q":
            print("exiting")
            quit()
        elif ret.lower() == "s":
            break
    elif all_input.lower() == "u":  # Need to Add understanding for lower section
        score_under = ("\nONES: After your three rolls you add up the amount of ones you rolled.",
                   "TWOS: After your three rolls you add up the number of twos you rolled.",
                   "THREES: After your three rolls you add up the number of Threes you rolled.",
                   "FOURS: After your three rolls you add up the number of fours you rolled.", 
                   "FIVES: After your three rolls you add up the number of fives you rolled.",
                   "SIXES: After your three rolls you add up the number of sixes you rolled.",
                   "BONUS: If your total points from the upper half is 63 or more then you will be given a bonus of 35 points at the end of the game.",
                   "3 OF A KIND: Whenever you roll 3 dice that are the same and the other 2 dice can either be the same or different, your score is calculated by adding the value of all the dice you rolled.",
                   "4 OF A KIND: Same as 3 of a kind except 4 dice must be the same and the scoring works the same as 3 of a kind.",
                   "FULL HOUSE: Whenever you finish your turn and 3 dice faces are the same and the other 2 dice faces are different from the 3 but are also the same eg. [2,2,2,4,4].",
                   "SMALL STRAIGHT: Whenever you finish your turn and the 4 of the dice go in ascending order and the 5th dice can be anything eg. [2,3,4,5,1], you will always get 30 points if you get a small straight.",
                   "LARGE STRAIGHT: Whenever you finish your turn and all of your dice faces go in ascending order eg. [1,2,3,4,5,] or [2,3,4,5,6], you will always get 40 points if you get a large straight.",
                   "YAHTZEE: If all of your dice are the same at the end of your turn, you will get 50 points always, if you get more then 1 yahtzee then you wil get an additional 100 bonus points for each. ",
                   "CHANCE: If you don't want to score your points to any category you score it to chance and get the value of the dice faces added to your score")
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
#-----------------------------------game starts now------------------------
num_die = 5 
rolled_dice = []

def roll():
    for die in range(num_die):
        rolled_dice.append(random.randint(1, 6))
    print(f"you rolled {rolled_dice}.")
    rolled_dice.sort()
roll()

print(rolled_dice)
