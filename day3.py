print("welcome to treasure Island \n you mission is to find treasure")
stage1=input("your at a cross road, where do you want to go: type 'left' or 'right'")
if stage1=="left":
    stage2=input("you are at the lake, There is a island in the middle of lake: type 'wait'to wait for boat 'swim' to swim across")
    if stage2=="wait":
        stage3=input("you have arrived island unharmed, There is a house with 3 doors. one red, one blue and one yellow, which one want you choose :")
        if stage3=="yellow":
            print("you win")
else:
    print("Game Over")

print('Game Over')
        