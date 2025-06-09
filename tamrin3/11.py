a = int(input())
b = int(input())

sum_odd = 0
sum_even = 0
count_odd = 0
count_even = 0

# way 1
current_num = a
while current_num <= b:
    if current_num % 2 == 0:
        sum_even += current_num
        count_even += 1
    else:
        sum_odd += current_num
        count_odd += 1
    current_num += 1


print(f"sum of odd numbers: {sum_odd}")
print(f"sum of even numbers: {sum_even}")
print(f"even: {count_even}")
print(f"odd: {count_odd}")

# way 2
for num in range(a, b + 1):
    if num % 2 == 0:
        sum_even += num
        count_even += 1
    else:
        sum_odd += num
        count_odd += 1

print(f"sum of odd numbers: {sum_odd}")
print(f"sum of even numbers: {sum_even}")
print(f"even: {count_even}")
print(f"odd: {count_odd}")
