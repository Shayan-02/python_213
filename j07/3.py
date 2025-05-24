majmoo = 0
tedad = 0
x = int(input("how many scores do you want to enter? "))
for i in range(x):
    num = int(input(f"enter number{i+1}: "))
    if 0 <= num <= 20:
        majmoo += num
        tedad += 1
    else:
        print("your score number is out of valid range")

avg = majmoo / tedad
if int(avg) == avg:
    print(int(avg))
else:
    print(avg)
