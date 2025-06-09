fib = int(input("enter a number: "))
f1 = 0
f2 = 1

# way 1
i = 1
while i <= fib:
    if i == 1:
        print(f1, end=" ")
    elif i == 2:
        print(f2, end=" ")
    else:
        f1, f2 = f2, f1+f2
        print(f2, end=" ")
    i += 1
