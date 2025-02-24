# secret_message = "   Programming in Python is not only powerful but also fun!   "
# clean_secret_message = secret_message.strip()
# clean_upper_msg = clean_secret_message.upper()
# print(clean_upper_msg)
# print(clean_upper_msg[15:21] + "-" + clean_upper_msg[34:42])


secret_message = "   Programming in Python is not only powerful but also fun!   "
# clean_secret_message = secret_message.strip()
# clean_upper_msg = clean_secret_message.upper()

# Dot Chaining
clean_upper_msg = secret_message.strip().upper()
print(clean_upper_msg)
print(clean_upper_msg[15:21] + "-" + clean_upper_msg[34:42])


# Task 1.1
# Expected Output
# "PYTHON-POWERFUL"


# 1. Solve
# 2. Make it better


# Task 1.2
flipped_message = "!nuf sseldnE dna seitinutroppo lufrewop htiw nohtyP"

# Expected Output
# "python 🗡️ powerful 🌸"

flipped_message_reverse = flipped_message[::-1].lower()
print(f"{flipped_message_reverse[0:6]} 🗡️ {flipped_message_reverse[12:20]} 🌸")


# Conditionals (Control flow)
# Take a decision -> Choice


# if...else
# if  no_of_person <=2 -> bike  else   car

no_of_person = 4

# Condition return boolean | if expects a boolean
if no_of_person <= 2:
    print("We will take the bike for the party")
else:
    print("We will take the car for the party")

# Lexical order -> Dictionary way of looking at it

# Task 1.1
# Get two person name and height
# Case 1:
# Ethan, Luvuyo
# 185cm, 175cm
# Ethan is taller than Luvuyo by 10cm


# person1 = input("Please tell me person1 name: ")
# person2 = input("Please tell me person2 name: ")
# height1 = float(input(f"Please tell me the height of {person1}: "))
# height2 = float(input(f"Please tell me the height of {person2}: "))


# if height1 > height2:
#     print(f"{person1} is taller than {person2} by {height1 - height2}cm")
# else:
#     print(f"{person2} is taller than {person1} by {height2 - height1}cm")


# Case 2:
# Ethan, Luvuyo
# 185cm, 194cm
# Luvuyo is taller than Ethan by 9cm


# Task 1.2
# Case 3:
# Ethan, Luvuyo
# 185cm, 185cm
# Ethan and Luvuyo are of the same height
# Clue: elif


# person1 = input("Please tell me person1 name: ")
# person2 = input("Please tell me person2 name: ")
# height1 = float(input(f"Please tell me the height of {person1}: "))
# height2 = float(input(f"Please tell me the height of {person2}: "))


# if height1 > height2:
#     print(f"{person1} is taller than {person2} by {height1 - height2}cm")
# elif height2 > height1:
#     print(f"{person2} is taller than {person1} by {height2 - height1}cm")
# else:
#     print(f"{person1} and {person2} are of the same height")

# only one if & else, multiple elif


# Task 1.3
# Improve code quality
# Clue: abs() -> Always +ve -> |x|


person1 = input("Please tell me person1 name: ")
person2 = input("Please tell me person2 name: ")
height1 = float(input(f"Please tell me the height of {person1}: "))
height2 = float(input(f"Please tell me the height of {person2}: "))
height_difference = abs(height1 - height2)

if height1 > height2:
    print(f"{person1} is taller than {person2} by {height_difference}cm")
elif height2 > height1:
    print(f"{person2} is taller than {person1} by {height_difference}cm")
else:
    print(f"{person1} and {person2} are of the same height")
