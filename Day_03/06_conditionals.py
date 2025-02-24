# Make a decision --> Whenever you have a CHOICE

# Conditionals (Control flow)

# if ... else
# if no_of_person <=2 --> bike else car

# no_of_person = 1

# # semi colon shows that the if statement is done
# # remember to indent the line by pressing tab

# if no_of_person <= 2:
#     print("We will take the bike to the party")
# else:
#     print("We will take the car to the party")

# Condition should return boolean (either true or false) | if expects a boolean
# If there is less than 2, the first statement will show.
# If there is more than 2, the else statement will show.

# Task 1.2
# Case 3:
# Ethan, Luvuyo
# 185cm, 185cm
# Ethan and Luvuyo are of the same height
# Clue: elif

# person1_name = input("Person 1 Name: ")
# person1_height = float(input("Person 1 Height: "))
# person2_name = input("Person 2 Name: ")
# person2_height = float(input("Person 2 Height: "))

# if person1_height > person2_height:
#     print(
#         f"{person1_name} is taller than {person2_name} by {person1_height - person2_height} cm"
#     )
# elif person1_height == person2_height:
#     print(f"{person1_name} and {person2_name} are the same height")
# else:
#     print(
#         f"{person2_name} is taller than {person1_name} by {person2_height - person1_height} cm"
#     )

# there can be ONLY one if & else, but multiple elif

# Task 1.3
# Improve code quality
# Clue: abs()
# Absolute will always give you positive values (you won't have to do big - small)
# small - big will give you a positive value with abs()

# person1_name = input("Person 1 Name: ")
# person1_height = float(input("Person 1 Height: "))
# person2_name = input("Person 2 Name: ")
# person2_height = float(input("Person 2 Height: "))
# height_difference = abs(person1_height - person2_height)

# if person1_height > person2_height:
#     print(
#         f"{person1_name} is taller than {person2_name} by {person1_height - person2_height} cm"
#     )
# elif person1_height == person2_height:
#     print(f"{person1_name} and {person2_name} are the same height")
# else:
#     print(
#         f"{person2_name} is taller than {person1_name} by {person2_height - person1_height} cm"
#     )
