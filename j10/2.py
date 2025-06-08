"""
a = []
b = int(input())
c = int(input())
for i in range(b, c+1):
    if i % 3 == 0:
        if i % 5 != 0:
            a.append(i)
print(a)
"""

a = [1, 2, 3]
a[1] = "ali"
print(a)

t = (1, 2, 3)
print(t)
print(type(t))
b = list(t)
b[1] = "ali"
t = tuple(b)
print(t)
print("salam", "hi")
