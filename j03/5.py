firstName = input("enter your firstname: ")
lastName = input("enter your lastname: ")
age = int(input("enter your age: "))
sen = 20

# print("your firstname is", firstName, ", your lastname is", lastName)
# print("So your full name is", firstName, lastName)
# print("Your age is", age, "years old.")

# format
print("your firstname is {} your lastname is {} sen e shoma {} saal ast.".format(firstName, lastName, sen))

# f-string
print(f"your firstname is {firstName} your lastname is {lastName}")
