
# import random
# # result=random.randint(0,1)
# # if result==1:
# #     print("head")
# # else:
# #     print('tail')
# names_string=input()
# names=names_string.split(", ")
# print(names)
# num_item=len(names)
# cal=random.randint(0,num_item-1)
# print(names[cal]+" is going to buy a meal")
# line1=[" ", " ", " "]
# line2=[" ", " ", " "]
# line3=[" ", " ", " "]
# map=[line1, line2, line3]
# print("HIding the treasure! mark X spot")
# position=input()
# letter=position[0].lower()
# abc=['a','b','c']
# letter_index=abc.index(letter)
# number_index=int(position[1])-1
# map[number_index][letter_index]="X"
# print(f"{line1}\n {line2}\n {line3}")
import random
Rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game=[Rock,Paper,Scissors]
user=int(input("what do you choose: type 0 for 'rock' 1 for 'paper' 2 for scissor :"))
if user>=3 or user<0:
    print("invalid input, please try again ")
print(game[user])
computer=random.randint(0,2)
print("computer chooses:")
print(game[computer])
if user==0:
    if computer==0:
        print("draw")
    elif computer==1:
        print("You win")
    else:
        print("You loss")
elif user==1:
    if computer==1:
        print("draw")
    elif computer==2:
        print("You win")
    else:
        print("You loss")
elif user==2:
    if computer==2:
        print("draw")
    elif computer==1:
        print("You win")
    else:
        print("You loss")