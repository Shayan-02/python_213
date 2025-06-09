n = input("enter a number:")
sums = 0

for i in range(9):
    a = (10 - i) * int(n[i])
    sums += a

r = sums % 11
print(r)
re = 11 - r

if int(re) == int(n[9]):
    print("valid")
else:
    print("invalid")
