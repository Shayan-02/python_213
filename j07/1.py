c = 50
n = 1
m = 3

print(f"you have {m} chances")
while n <= m:
    num = int(input(f"enter chance{n}: "))
    if num == c:
        print(f"you win in {n} chances")
        break
    else:
        if num > c:
            print(f"correct number is smaller than {num}")
        else:
            print("correct number is higher than", num)
        print(f"you have {m-n} another chances")
    n += 1
else:
    print("you loss")
