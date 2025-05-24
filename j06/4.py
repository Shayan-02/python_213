num1 = int(input("enter a number: "))
num2 = int(input("enter a number: "))

i = 1
j = 1

while i <= num1:
    while j <= num2:
        print(i*j, end="\t")
        j+=1
    i+=1
