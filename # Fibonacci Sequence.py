# Fibonacci Sequence
FibonacciTerms = int(input("how many terms?"))

num1, num2 = 0, 1
count = 0

if FibonacciTerms == 1:
   print("Fibonacci sequence until",FibonacciTerms,":")
   print(num1)
else:
   print("Fibonacci sequence:")
while count < FibonacciTerms:
       print(num1)
       
       nth = num1 + num2
       num1 = num2
       num2 = nth
       count += 1