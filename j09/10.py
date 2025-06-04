num1 = int(input(" enter number1 :"))
num2 = int(input(" enter number2 :"))

for i in range(num1, num2 + 1):
    for j in range(2, (num2 // 2 + 1)):
        if i % j == 0:
            break
        print(i)
