num1 = float(input("Enter First Number => "))
num2 = float(input("Enter Second Number => "))
opr = str(input("Enter Opeartions (+, -, *, /) => "))

if opr == '+':
    total = ("The addition of given two numbers is", num1 + num2)
elif opr == '-':
    total = ("The substraction of given two numbers is", num1 - num2)
elif opr == '*':
    total = ("The multiplication of given two numbers is", num1 * num2)
elif opr == '/':
    total = ("The division of given two numbers is", num1 / num2)
else:
    total = str("Please Enter a Valid Operation")       

print(total)             