Ask the user for their name
name = input("Enter your name: ")

# Ask the user for their age and convert it to a whole number (integer)
age = int(input("Enter your age: "))

# Greet the user
print(f"Hello, {name}!")

# Check if the user can vote (voting age is 18)
if age >= 18:
    print("You are eligible to vote!")
else:
    print("You are not old enouggit pushh to vote yet.")