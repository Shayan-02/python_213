num1 = int(input("enter a number: "))
op = input("enter an operator: ")
num2 = int(input("enter a number: "))

if op == "+":
    print("sum:", num1 + num2)
elif op == "-":
    print("sub:", num1 - num2)
elif op == "*":
    print("mul:", num1 * num2)
elif op == "/":
    # if num2 == 0:
    #     print("nemitavan adad ra taghsim bar 0 kard")
    # else:
    if num2 != 0:
        print("div:", num1 / num2)
    else:
        print("nemitavan adad ra taghsim bar 0 kard")
    print("taghsim")
