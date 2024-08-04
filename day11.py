# import random

# cards=[11,1,2,3,4,5,6,7,8,9,10,10,10,10,10]
# my_list=[]
# computer_list=[]
# con=True
# while con:
#     first_chance=random.choice(cards)
#     my_list.append(first_chance)
#     second_chance=random.random(cards)
#     my_list.append(second_chance)
#     show=print(f"your score {my_list}")
#     computer_chance=random.randint(cards)
#     computer_list.append(computer_chance)
#     show2=print(f"computer Score is {[computer_list]}")
#     computer_chance2=random.randint(choice)
#     computer_list.append(computer_chance2)
#     if first_chance+second_chance <=21:
#         round1=input("type y to get  another card, n for pass ")
#         if round1 == "y":
#             third_chance=random.randint(choice)
#             my_list.append(third_chance)
#             show=print(f"your score {my_list}")
#             computer_chance2=random.randint(choice)
#             computer_list.append(computer_chance2)
#             show2=print(f"computer Score is {[computer_list]}")
#         else:
#             sum=0
#             for i in my_list:
#                 sum+=i
#             print(f"your final hand : {my_list} final_score : {sum}")
#             sum1=0
#             for i in computer_list:
#                 sum1+=i
#             print(f"your final hand : {computer_list} final_score : {sum1}")

#             if sum1>sum:
#                 print("you loss ")
#             else:
#                 print("you win")
import random
def deal_card():
    cards=[11,1,2,3,4,5,6,7,8,9,10,10,10,10,10]
    card = random.choice(cards)
    return card
def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)


    return sum(cards)
def compare(user_score,computer_score):
    if user_score == computer_score:
        print("draw")
    elif computer_score==0:
        print("loss, oppenent win ")
    elif user_score==0:
        print("win with a blackjeck ")
    elif user_score>21:
        print("you went over , you loss ")
    elif computer_score>21:
        print("computer went over, you win ")
    elif user_score>computer_score:
        print('you win')
    else:
        print("you loss ")
def play_game():
    my_list=[]
    computer_list=[]
    is_game_over=False
    for _ in range(2):
        my_list.append(deal_card())
        computer_list.append(deal_card())
    while not is_game_over:
        user_score=calculate_score(my_list)
        computer_score=calculate_score(computer_list)
        print(f"your card ; {my_list} and total score ; {user_score}")
        print(f"computer card ; {computer_list[0]}")
        if user_score==0 or computer_score==0 or user_score>21:
            is_game_over = True
        else:
            cont=input("type y to get  another card, n for pass ")
            if cont == 'y':
                my_list.append(deal_card())
            else:
                is_game_over=True

    while computer_score!=0 and computer_score <17:
        computer_list.append(deal_card())
        computer_score=calculate_score(computer_list)

    print(f"your final hand {my_list} and final score {user_score}")
    print(f"computer final hand {computer_list} and final score{computer_score}")
    print(compare(user_score,computer_score))

while input("do you want to play a game y for yes, n for no :")=='y':
    play_game()