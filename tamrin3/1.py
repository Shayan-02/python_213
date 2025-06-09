correct = 50
user = int(input("enter a number: "))
chance = 5

print(f"you have {chance} chances")
# way 1
while chance > 0:
    if user > correct:
        print("too high")
    elif user < correct:
        print("too low")
    else:
        print("correct")
    chance -= 1
else:
    print("you loss")

# way 2
for i in range(chance):
    if user > correct:
        print("too high")
    elif user < correct:
        print("too low")
    else:
        print("correct")
else:
    print("you loss")
