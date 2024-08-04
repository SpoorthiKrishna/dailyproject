word=['spoorthi','ramya','sinchana']
logo='''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
'''
import random
stages= ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

lives=6
print(logo)
choose_word=random.choice(word)
print(f"the choosen word is {choose_word}")
res=[]
word_count=len(choose_word)
for _ in range(word_count):
    res+="_"
print(res)
end_of_game=False
while not end_of_game:
    guess=input("Guess letter : ")
    if guess in res:
        print(f"you already guessed this letter {guess}")
    for position in range(word_count):
        letter=choose_word[position]
        if letter == guess:
            res[position] = letter
    print(res)
    if guess not in choose_word:
        print(f"you letter {guess} is not in word")
        lives-=1
        if lives==0:
            end_of_game=True
            print("You loss")

    if "_" not in res:
        end_of_game=True
        print("you won")
    print(stages[lives])