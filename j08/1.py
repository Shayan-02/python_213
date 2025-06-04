f1 = 0
f2 = 1
n = int(input("enter a number: "))

i = 1
while i <= n:
    f1, f2 = f2, f1+f2
    i+=1
    print(f1, end="")
