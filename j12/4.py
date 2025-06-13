lst = []

for i in range(10, 21):
    if i % 2 == 0:
        lst.append(i)

lst2 = [i for i in range(10, 21) if i % 2 == 0]
print(lst2)

lst3 = [1, 2, 3, 4, 5]
lst4 = [i**2 for i in lst3]

lst5 = []
for i in lst3:
    lst5.append(i)
