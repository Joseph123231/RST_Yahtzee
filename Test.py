import random
import math

dice = [1,4,2,3,5]
dice.sort()
if len(set(dice)) == 5:
    if dice[1 + 1] == dice[2] and dice[0]!= dice[4] :
        print("small straight")
        print(dice)
else:
    print("Not small straight")
    print(dice)

if len(set(dice)) == 5:
    if dice[0 + 1] == dice[1] and dice[0 + 4] == dice[4]:
        print("large staright")
    else:
        print("not large straight")
