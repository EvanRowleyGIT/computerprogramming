#Salary and bonus

salary = int(input("What is your salary? "))
years = int(input("How many years have you been working here? "))

if years >= 5:
    print(f"Congradulations, you get a bonus of ${salary * 0.05}.")
else:
    print("Sorry you do not qualify for a bonus.")


#Rectangle or square?

First = int(input("What is the length of the rectangle? "))
Second = int(input("what is the width of the rectangle? "))

if First == Second:
    print("This rectangle is actually a square!")
else:
    print("This is just rectangle")