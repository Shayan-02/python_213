n = int(input("enter a number: "))

# way 1:
i = 1
while i <= n:
    j = 1
    while j <= n:
        print(i * j, end=" ")
        j += 1
    print()
    i += 1

# way 2:
for i in range(1, n+1):
    for j in range(1, n+1):
        print(i * j, end=" ")
    print()
