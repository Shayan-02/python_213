n = int(input())

# way 1:
if n == 0:
    count = 1
else:
    if n < 0:
        n = -n

    count = 0
    while n > 0:
        n = n // 10
        count += 1

print(count)

# way 2:
for i in range(1, n+1):
    count = 0
    while i > 0:
        i = i // 10
        count += 1
print(count)

# way 3
for i in str(n):
    count += 1
print(count)

# way 4
print(len(str(n)))
