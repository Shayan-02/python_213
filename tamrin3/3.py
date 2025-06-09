n = int(input("enter a number: "))
fact = 1

# way 1
i = 1
while i <= n:
    fact *= i
    i += 1
print(fact)

# way 2
for i in range(1, n+1):
    fact *= i
print(fact)

