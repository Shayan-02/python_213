a = input().split()

lst = []

for i in a:
    if int(i) % 2 == 0:
        lst.append(int(i))

print(lst)
