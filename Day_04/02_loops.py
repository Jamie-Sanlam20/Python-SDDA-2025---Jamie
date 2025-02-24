# print("Vote for Jevan")
# print("Vote for Jevan")
# print("Vote for Jevan")

# Refactor in while loop

i = 1

# i <= 3 is our condition
# if the condition is true, it will keep on printing the statement (code runs)
# it will run until condition is false
# as long as i is 1 (less than 3). it will keep on printing

# while i <= 3:
#     print("Vote for Jevan")
#     i = i + 1
# print("voting has ended")

# we should increment i to end the loop (it will eventually equal 4)
# every iteration gets incremented\
# when i = 4. it will show voting has ended.


# Refactor in for loop
# for and range comes in a pair
# range always starts with 0
# range excludes the end/last value
# range will include 0,1,2 -> 3 is excluded
# range(start, end, step)
# if you just give 3, end value is 3

for i in range(3):
    print(i)

# range(start,end)
# for and range automatically increments `i` by 1

for i in range(1, 10):
    print(i)

# Task 1: Print only odd numbers from 1 to 50

# Task 1.1: Easy way - range(start, end, step)
# step -> default value is 1, change it to 2

for i in range(1, 50, 2):
    print(i)

# Task 1.2: Hard way
# mod gives you the remainder
# if mod(0), remainder should be 0

for i in range(1, 50):
    if i % 2 != 0:
        print(i)

# we are saying if i is divisible by 2 (even numbers), we don't want it (not equal to)
# this will show us odd numbers

# Task 1.3: Refactor in for loop
# for and range "Vote for Jevan"

for i in range(3):
    print("Vote for Jevan 🎊")
