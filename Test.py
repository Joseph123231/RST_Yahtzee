import random
import math

Of_kind = [3,3,2,2,5]
Of_kind.sort()
# target = 3
# score = None
# _______________________3 of a kind check______________-
if len(set(Of_kind)) == 2 or len(set(Of_kind)) == 3:
    if Of_kind[2] == Of_kind[0] or Of_kind[2] == Of_kind[4]:
        if Of_kind[3] != Of_kind[4] or Of_kind[0] != Of_kind[1]:
            print("3 of kind")
            
    else:
         print("NOT 3 of a kind")
         print(Of_kind)
print(Of_kind)
#__________________________________4 of a kind check___________________
if len(set(Of_kind)) == 2:
    if Of_kind[0] == Of_kind[3] or Of_kind[4] == Of_kind[1]:
        print("4 of a kind")
        print(Of_kind)
    else:
         print("Not 4 of a kind")
#________________________________________________________________

#_________________________________ FUll HOUSE CHECK_______________________
if len(set(Of_kind)) == 2: 
    if Of_kind[0] != Of_kind[3] or Of_kind[4] != Of_kind[1] and Of_kind[2] == Of_kind[0] or Of_kind[4]:
        print("full house")
    else:
         print("Not Full house")
#________________________________________________________________________
#_________________________small straight check__________________ ### need to account for when there are duplicates in the dice but still add u
if len(set(Of_kind)) == 5 or len(set(Of_kind)) == 4:
    if Of_kind[1 + 1] == Of_kind[2] and Of_kind[0]!= Of_kind[4] :
        print("small straight")
        print(Of_kind)
    else:
        print("Not small straight")
#________________________________________________________________
#_____________________check fpr YAHTZEE____________
if len(set(Of_kind)) == 1:
    print("IT'S A YAHTZEE")
else:
    print("IT'S NOT A YAHTZEE")
