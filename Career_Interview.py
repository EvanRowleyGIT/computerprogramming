UserInput1 = input("Hello there, what is your name? ")

UserInput2 = input(f"Hello {UserInput1}, what are you interested in within the computer programing field? ")

UserInput3 = input(f"Ah, very interesting, I was also interested in {UserInput2} back when I was new. Yes or No, have any of your previous jobs included programing? ")
if UserInput3 == "Yes":
    print("Great, we will keep that in mind.")
if UserInput3 == "No": 
    print("Hmm, thats to bad. Sorry, but we will only hire you if there are no other options. We will update you if we change our minds.")
    exit()

UserInput4 = input("How many years of experience do you have? ")
if UserInput4 > "1":
    print("That should be pretty useful.")
if UserInput4 == "1":
    print("That doesn't matter, we can still use just a year or so of experience. ")

UserInput5 = input("Now then, what would you like you're yearly salary to be? Please refrain from using the dollor sign if possible. ")
if UserInput5 <= "100000":
    print("Seems pretty reasonable for the job.")
if UserInput5 > "100000":
    print("Uhhhh, I dont think we can work with that. We will let you know if we change our minds.")
    exit()

UserInput6 = input("Do you know multiple coding languages? Answer Yes or No. ")
if UserInput6 == "Yes":
    print("Nice, That could be very useful. We require that a lot of the time, depending on the clients. Very useful.")
if UserInput6 == "No":
    print("I'm sorry, we require our employees to know multiple coding languages, as the clients opinions can vary. We cannot hire you.")
    exit()

UserInput7 = input("Do you have anything on you'r criminal record? ")
if UserInput7 == "Yes":
    print("We will look it over, but you seem like a good enough person. You're fine.")
if UserInput7 == "No":
    print("That is very good, so far, so good.")

UserInput8 = input("What kind of hobbies do you have, 1. sports, 2. video games, 3. reading, 4. Other? ")
list = ("1. Sports", "2. Video Games", "3. Reading", "4. Other") 
print(list)
if UserInput8 == "1":
    print("Very good, we'll have to test that out sometime, if you get the job, of course.")
if UserInput8 == "2":
    print("Yes, gaming is very fun, but we have to make sure it doesn't get in the way if you want this job.")
if UserInput8 == "3":
    print("Ah, a very respectable hobby. Anyways, lets continue")
if UserInput8 == "4":
    print("Very interesting. Lets continue")

UserInput9 = input("Do you have a very busy schedule? ")
if UserInput9 == "Yes":
    print("That's too bad, I'm sure we can find a work around of course though. ")
if UserInput9 == "No":
    print("Thats good, oftentimes people are too busy to fill in around here.")

UserInput10 = input("Well, so far everything has been good enough. However, you have one last question. Are you willing to work hard, and will you try to do you'r best to work as a team with the other employees? ")
if UserInput10 == "Yes":
    print("Great job then, we will accept your resume. We will let you know when your first day on the job will be. See you then!")
if UserInput10 == "No":
    print("Sorry, but if you are not going to have a hard working ethic, and you refuse to work as a team, we cannot hire you. We would still be willing to accept you if you change your mind. Until then, Goodbye.")
    exit()