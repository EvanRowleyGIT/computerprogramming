
# print("What is the first number?")
# input()
# print("what is the second number?")
# input()
# print("What operation would you like to use? Divide, Multiply, Subtract, Add")

# operation1 = "Divide"
# operation2 = "Multiply"
# operation3 = "Subtract"
# operation4 = "subract"






# def print_my_name(name):
#     print(name)

# print_my_name('Bob')

# def trip_planner(start, end, duration, mode):
#     print(f"It looks like you're taking a trip to {start}")
#     print(f"You are planning to get to {end}")
#     print(f"It should take you about {duration} hours")
#     print(f"I see you are taking a {mode}")
# trip_planner("Paradigm", "The Delta Center", "0.5", "car")



# input()







# option1 = "Multiply"
# option2 = "Divide"
# option3 = "Add"
# option4 = "Subtract"

# if input("Multiply"):
#     (user_number1 * user_number2)
#     print(user_number1 * user_number2)
 



# add_two_numbers2(user_number1, user_number2)

# user_input = int(input("Give me a number: "))
# user_input2 = int (input("Give me a second number: "))
# operation = int(input("Give me an operation: "))
# print("What is the first number?")
# input()
# print("what is the second number?")
# input()
# print("What operation would you like to use? Divide, Multiply, Subtract, Add")

# def add(num1 + num2)
#     print(num1 + num2)
 
# def subtract(num1 - num2)
#     print(num1 - num2)

# def multiply(num1 * num2)
#     print(num1 * num2)

# def divide(num1 / num2)
#     print(num1 / num2)

# if  operation == '+':
#     add(num1, num2)

# if operation == '-':
#     subtract(num1, num2)

# if operation == '*':
#     multiply(num1, num2)

# if operation == '/':
#     divide(num1, num2)

# Python program for simple calculator
 
# Function to add two numbers
def add(num1, num2):
    return num1 + num2
 
def subtract(num1, num2):
    return num1 - num2
 
def multiply(num1, num2):
    return num1 * num2
 
def divide(num1, num2):
    return num1 / num2
 
print("Choose the operation"
        "1.Add"
        "2.Subtract"
        "3.Multiply"
        "4.Divide")
 
 
select = int(input("Select operations form 1, 2, 3, 4 :"))
 
number_1 = int(input("1st number: "))
number_2 = int(input("2nd number: "))
 
if select == 1:
    print(number_1, "+", number_2, "=",
    add(number_1, number_2))
 
elif select == 2:
    print(number_1, "-", number_2, "=",
    subtract(number_1, number_2))
 
elif select == 3:
    print(number_1, "*", number_2, "=",
     multiply(number_1, number_2))
 
elif select == 4:
    print(number_1, "/", number_2, "=",
    divide(number_1, number_2))