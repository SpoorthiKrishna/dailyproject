import random
from support14 import data # type: ignore
stop=True
count=0
while stop:
    def com(selection,person1,person2,count):   
        if selection=='a':
            if person1['follower_count'] > person2['follower_count']:
                count+=1
                print(f"your guess is correct!...your score is {count}")
                return count 
                
            else:
                print(f"you guess is wrong . your final score is {count} ")
                return stop
        else:
            if person1['follower_count'] < person2['follower_count']:
                count+=1
                print(f"your guess is correct!...your score is {count}")
                return count
                
            else:
                print(f"you guess is wrong .your final score is {count} ")
                return stop
                

    
    person1=random.choice(data)
    print(f"Compare A : {person1['name']},{person1['description']}, from {person1['country']}")

    person2=random.choice(data)
    print(f"against B : {person2['name']},{person2['description']}, from {person2['country']}")

    select=input("who has more followers type A or B ")
    final=com(select,person1,person2,count)
    if final == 'stop':
        stop=False

