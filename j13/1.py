num1 = int(input())
op = input()
num2 = int(input())

def calc(num1, op, num2):
    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "/":
        if num2 != 0:
            print(num1 / num2)
        else:
            print("can't devide by zero")
    else:
        print("invalid operator")

calc(num1, op, num2)

calc(30, "-", 5)
