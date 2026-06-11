import random
print("ＷＥＬＣＯＭＥ  ＴＯ  ＴＨＥ  ＨＡＮＧＭＡＮ  ＧＡＭＥ！！")
stages = ['''
 +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''','''
+---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',''' 
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
  +---+
  |   |
      |
      |
      |
      |
=========''']

words = ['APPLE','PINEAPPLE','HANGMAN','MEASURING','EGGNOG','SOAK','CHEERFUL','ROMANTIC',
         'BASKETBALL','WHEEL','SCISSORS','SPARK','AVAILABLE','SCHOOL',
         'CELEBRITY','INSTAGRAM']
#CODE TO CHOOSE A RANDOM WORD FROM THE LIST.
random.word = random.choice(words)
print(random.word)
#CODE THE REPLACE THE WORD WITH A BLANK
placeholder = ""
for position in range(0, len(random.word)):
    placeholder += "_"
print(placeholder)
print("THE PLAYER HAS 5 LIVES")
print(stages[6])
game_over = False
correct_letter = []
lives = 6
#CODE FOR REPETING THE GUESSING PROCESS.
while not game_over:
    guess = input("Guess a letter: ").upper()
    print(guess)

    display = ""

    for letter in random.word:
        if letter == guess:
            display += letter
            correct_letter.append(guess)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"
    print(display)
    if guess not in random.word:
        lives -= 1
        if lives == 5:
            print(stages[5])
            print(f"YOU NOW HAVE {lives} LIVES LEFT!")
        elif lives == 4:
            print(stages[4])
            print(f"YOU NOW HAVE {lives} LIVES LEFT!")
        elif lives == 3:
            print(stages[3])
            print(f"YOU NOW HAVE {lives} LIVES LEFT!")
        elif lives == 2:
            print(stages[2])
            print(f"YOU NOW HAVE {lives} LIVES LEFT!")
        elif lives == 1:
            print(stages[1])
            print(f"YOU NOW HAVE  {lives} LEFT!")
        else :
            print(stages[0])
            game_over = True
            print("GAME OVER")

    if "_" not in display:
        game_over = True
        print("YOU WIN!!")
