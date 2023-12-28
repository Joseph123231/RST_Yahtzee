import random

Of_kind = []
Of_kind.sort()
print("you rolled")
num_die = 5
for die in range(num_die):
    Of_kind.append(random.randint(1, 6))
Of_kind.sort()
print(Of_kind)

# _______________________3 of a kind check______________-
if len(set(Of_kind)) == 2 or len(set(Of_kind)) == 3:
    Of_kind.sort()
    if Of_kind[0] == Of_kind[1] and Of_kind[0] == Of_kind[2] or Of_kind[1] == Of_kind[2] and Of_kind[1] == Of_kind[3] or Of_kind[2] == Of_kind[3] and Of_kind[2] == Of_kind[4]:
            print("3 of kind")
            print(Of_kind)
    else:
         print("NOT 3 of a kind")
         print(Of_kind)
#__________________________________4 of a kind check___________________
if len(set(Of_kind)) == 2:
    Of_kind.sort()
    if Of_kind[0] == Of_kind[3] or Of_kind[4] == Of_kind[1]:
        print("4 of a kind")
        print(Of_kind)
    else:
         print("Not 4 of a kind")
#________________________________________________________________

#_________________________________ FUll HOUSE CHECK_______________________
if len(set(Of_kind)) == 2: 
    Of_kind.sort()
    if Of_kind[0] != Of_kind[3] or Of_kind[4] != Of_kind[1] and Of_kind[2] == Of_kind[0] or Of_kind[4]:
        print("full house")
    else:
         print("Not Full house")
#________________________________________________________________________
#_________________________small straight check__________________ ### need to account for when there are duplicates in the dice but still add u
if len(set(Of_kind)) == 5 or len(set(Of_kind)) == 4:
    Of_kind.sort()
    if Of_kind[1 + 1] == Of_kind[2] and Of_kind[0]!= Of_kind[4] :
        print("small straight")
        print(Of_kind)
    else:
        print("Not small straight")
#________________________________________________________________
#_____________________check fpr YAHTZEE____________
if len(set(Of_kind)) == 1:
    Of_kind.sort()
    print("IT'S A YAHTZEE")
else:
    print("IT'S NOT A YAHTZEE")
