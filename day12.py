# enemies=1
# def en():
#     enemies=1
#     print(f"the {enemies}")
#     return enemies+1

# en()
# print(f"the {enemies}")

import random
print("Welcome! to the number guessing Game ")
print("i'm thinking the number between 1 to 100 ")
user_choice=input("choose your difficulty 'easy' or 'hard' : ")
if user_choice == "easy":
    print("you have 10 attempt ")
    attempt=10
else:
    print("tou  have 5 attempt ")
    attempt=5

computer_guess=random.randint(1,100)

def guesses(user_choice):
    for i in range(user_choice,0,-1):
        print(f"you have {i} attempts to guess the number ")
        user_guess=int(input("make a guess : "))
        if user_guess > computer_guess :
            print("too high")
        elif user_guess < computer_guess :
            print("too low")
        else:
            print(f"you got it, the ans is {computer_guess}")

        print("guess again")
    print(f"the number is {computer_guess}")
guesses(attempt)