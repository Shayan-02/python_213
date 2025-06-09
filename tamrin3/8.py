n = int(input())

# way 1:
i = 1
while i <= n:
    j = 1
    while j <= n:
        if i == 1 or i == n or j == 1 or j == n:
            print("*", end="")
        else:
            print(" ", end="")
        j += 1
    print()
    i += 1

print("----------------")

# way 2:
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == 1 or i == n or j == 1 or j == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()
