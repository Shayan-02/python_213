num1 = int(input("enter number1: "))
op = input("enter an operator: ")
num2 = int(input("enter number2: "))
r = 0
if op == "+" or op == "-" or op == "*" or op == "/":
    if op == "+":
        r = num1 + num2
    elif op == "-":
        r = num1 - num2
    elif op == "*":
        r = num1 * num2
    elif op == "/" and num2 == 0:
        print("division by zero")
    elif op == "/" and num2 != 0:
        r = num1 / num2
    print(f"resault: {num1} {op} {num2} = {r}")
else:
    print("invalid input")
