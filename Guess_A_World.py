word = "COMPUTER" 
guesses = "_ _ _ _ _ _ _ _"
win = False
while win == False:
    loopword = ""
    print(">>> Welcome to Hangman!")
    print("Here is your original line!")
    print(guesses)
    guess = input(print(">>> Guess a letter!"))
    if len(guess) > 1:
        if guess == word:
            win = True
            break
    if word.find(guess) != -1:
        for i in range(len(word)):
            if guess == word[i] or guesses.find(word[i]) > -1:
                loopword = loopword + word[i] + " "
            else: loopword = loopword + "_ "
    guesses = loopword
    print(guesses)
    print(">>> Great job!")
    print(">>> Here is your line now")
    print(">>> If you are finished with the word, type it all in and if its right you WIN!!")
    
print(">>> YOU WON!")