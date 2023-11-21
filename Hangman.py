# word = "COMPUTER" 
# guesses = "_ _ _ _ _ _ _ _ "
# win = False

# while win == False:
#     loopword = ""
#     print(">>> Welcome to Hangman!")
#     print(">>> Here is your original line!")
#     print(guesses)
#     guess = input(print(">>> Guess a letter!"))
#     if len(guess) > 1:
#         if guess == word:
#             win = True
#             break
#     if word.find(guess) != -1:
#         for i in range(len(word)):
#             if guess == word[i] or guesses.find(word[i]) > -1:
#                 loopword = loopword + word[i] + " "
#             else: loopword = loopword + "_ "
#     guesses = loopword
#     print(guesses)
#     print(">>> Good Guess!")
#     print(">>> Here is your line now")
#     print(">>> If you are finished with the word, type it all in and if its right you WIN!!")
    
# print(">>> YOU WON!")

# word = "COMPUTER" 
# guesses = "_ _ _ _ _ _ _ _ "
# win = False

# while win == False:
#     loopword = ""
#     print(">>> Welcome to Hangman!")
#     print(">>> Here is your original line!")
#     print(guesses)
#     guess = input(print(">>> Guess a letter!"))
#     if len(guess) > 1:
#         if guess == word:
#             win = True
#             break
#     if word.find(guess) != -1:
#         for i in range(len(word)):
#             if guess == word[i] or guesses.find(word[i]) > -1:
#                 loopword = loopword + word[i] + " "
#             else: loopword = loopword + "_ "
#     guesses = loopword
#     print(guesses)
#     print(">>> Good Guess!")
#     print(">>> Here is your line now")
#     print(">>> If you are finished with the word, type it all in and if its right you WIN!!")
    
# print(">>> YOU WON!")

#     print("Incorrect. You have 3 guesses left")
# if guess == False == 2:
#     print("Incorrect. You have 2 guesses left")
# if guess == False == 3:
#     print("Incorrect. You have 1 guess left, Be careful!")
# if guess == False == 4:
#     print("Incorrect, You have lost.")
#     exit()


import random 

with open("sowpods.txt", "r") as file: 
	allText = file.read() 
	words = list(map(str, allText.split())) 


word = random.choice(words)
guessed = "_" * len(word)
word = list(word)
guessed = list(guessed)
lstGuessed = []
letter = input("guess letter: ").upper()
lives = 10
while True:
    if letter in lstGuessed:
        letter = ''
        print("Already guessed!!")
    elif letter in word:
        index = word.index(letter)
        guessed[index] = letter
        word[index] = '_'
    else:
        print(''.join(guessed))
        if letter != '':
            lstGuessed.append(letter)
        letter = input("guess letter: ").upper()

    if letter not in guessed:
        lives -= 1
        print(f"You have {lives} lives left")
    
    if '_' not in guessed:
        print("YOU WON")
        print(f"Your word was: {''.join(guessed)}")
        exit()

    if lives == 0:
        print("Better luck next time. You're out of lives.")
        exit()