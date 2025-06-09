n = int(input("enter a number: "))
charge = 0

# way 1
while n > 0:
    charge += n
    n -= 1
print(charge)

# way 2
i = 1
while i <= n:
    charge += i
    i += 1
print(charge)

# way 3
for i in range(1, n+1):
    charge += i
print(charge)
