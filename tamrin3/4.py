n = int(input("enter num of numbers: "))
sum_numbers = 0

# way 1
i = 1
while i <= n:
    number = int(input(f"enter number{i}: "))
    sum_numbers += number
    i += 1
print(sum_numbers)

# way 2
for i in range(1, n+1):
    number = int(input(f"enter number{i}: "))
    sum_numbers += number
print(sum_numbers)
