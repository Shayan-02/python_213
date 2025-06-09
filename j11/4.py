import random
words = ["apple", "banana", "cherry", "tomato", "potato", "water melon", "cucumber"]
# n = int(input("enter a number between 0 to 6: "))
# if n in range(0, 7):
#     correct_word = words[n]
#     for i in range(3):
#         answer = input(f"enter choice{i+1}: ")
#         if answer == correct_word:
#             print(f"you won in {i+1} round")
#             break
#         else:
#             print("wrong")
#     else:
#         print(f"game over.correct word was {correct_word}")
# else:
#     print("invalid number")
# correct_word = words[random.randint(0, 6)]
correct_word = random.choice(words)
for i in range(3):
    answer = input(f"enter choice{i+1}: ")
    if answer == correct_word:
        print(f"you won in {i+1} round")
        break
    else:
        print("wrong")
else:
    print(f"game over.correct word was {correct_word}")
