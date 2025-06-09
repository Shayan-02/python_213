n = int(input("enter a number: "))

# way 1
i = 1
while i <= n:
    print(n * " *")
    i += 1

print("--------------")

# way 2
for i in range(1, n+1):
    print(n * " *")
