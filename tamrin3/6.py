user1_score, user2_score = 0, 0
rounds = int(input("enter rounds: "))

# way 1
i = 1
while i <= rounds:
    user1_choice = input(f"user1 (rock paper or scissors) round{i}: ")
    user2_choice = input(f"user2 (rock paper or scissors) round{i}: ")
    
    if user1_choice == user2_choice:
        print("draw")
    elif user1_choice == "rock" and user2_choice == "scissors":
        print("winner : user1")
        user1_score += 1
    elif user1_choice == "paper" and user2_choice == "rock":
        print("winner : user1")
        user1_score += 1
    elif user1_choice == "scissors" and user2_choice == "paper":
        print("winner : user1")
        user1_score += 1
    else:
        print("winner : user2")
        user2_score += 1
    i += 1

print("-------------------")
print(f"user1 score: {user1_score}")
print(f"user2 score: {user2_score}")
print(f"draw: {rounds - user1_score - user2_score}")
if user1_score == user2_score:
    print("draw")
else:
    print(f"winner : {user1_score > user2_score}")

# way 2
for i in range(1, rounds+1):
    user1_choice = input(f"user1 (rock paper or scissors) round{i}: ")
    user2_choice = input(f"user2 (rock paper or scissors) round{i}: ")
    
    if user1_choice == user2_choice:
        print("draw")
    elif user1_choice == "rock":
        if user2_choice == "scissors":
            print("winner : user1")
            user1_score += 1
        else:
            print("winner : user2")
            user2_score += 1
    elif user1_choice == "paper":
        if user2_choice == "rock":
            print("winner : user1")
            user1_score += 1
        else:
            print("winner : user2")
            user2_score += 1
    elif user1_choice == "scissors":
        if user2_choice == "paper":
            print("winner : user1")
            user1_score += 1
        else:
            print("winner : user2")
            user2_score += 1

print("-------------------")
print(f"user1 score: {user1_score}")
print(f"user2 score: {user2_score}")
print(f"draw: {rounds - user1_score - user2_score}")
if user1_score == user2_score:
    print("draw")
else:
    print(f"winner : {user1_score > user2_score}")
