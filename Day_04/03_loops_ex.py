# Repetition operator (*) -> means it will be repeated

# Task 1.1
i = 1

while i <= 5:
    print("🔥" * i)  # Repeat "🔥" by i times
    i = i + 1

# Task 1.2

for i in range(1, 6):
    print("🔥" * i)  # Repeat "🔥" by i times

# Task 1.3

no_of_rows = int(input("Please tell me the no of rows: "))
pattern = input("Please tell me the pattern: ")

while i == no_of_rows:
    print(pattern * i)  # Not necessary to format since it isn't a string (no f)
    i = i + 1

# Task 1.4

no_of_rows = int(input("Please tell me the no of rows: "))
pattern = input("Please tell me the pattern: ")

# have to add one to end value (since its excluded)

for i in range(1, no_of_rows + 1):
    print(f"{pattern * i}")

# 90% of the time --> for loop
# only use While loop sometimes
