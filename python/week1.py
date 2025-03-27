num1 = int(input("What is the first number?"))
num2 = int(input("What is the second number?"))
sign = input("What is the operator?")

if sign == '+':
    print(f" {num1} {sign} {num2} = {num2 + num1}")
elif sign == '-':
    print(f" {num1} {sign} {num2} = {(num2 - num1)}")
elif sign == '*':
    print(f" {num1} {sign} {num2} = {(num2 * num1)}")    
elif sign == '/':
   print(f" {num1} {sign} {num2} = {(num2 / num1)}")
elif sign == '%':
    print(f" {num1} {sign} {num2} = {(num2 % num1)}") 
elif sign == '**':
    print(f" {num1} {sign} {num2} = {(num2 ** num1)}")
else:
    print("Invalid operator")                  