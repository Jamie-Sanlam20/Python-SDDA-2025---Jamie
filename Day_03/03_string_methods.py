fav_movie = "John Wick"

# Only J

# Index - starts with 0
print(fav_movie[0])

# Only W
print(fav_movie[5])

# Only K (at the end)
# Python can read negative numbers -1 (at the end - comes in reverse direction)
# Negative Index

print(fav_movie[-1])

# Only 'Wick'

print(fav_movie[-4] + fav_movie[-3] + fav_movie[-2] + fav_movie[-1])

# Slice operator (:)
# called slicing, because it takes a slice of the word
# fav_movie[start:end] - end index not included (do not type 8 for k)

print(fav_movie[2:6])

# How to print till the end

print(fav_movie[2:9])  # add one to the index - solution 1
print(fav_movie[2:])  # printing till end - solution 2

# Prints entire word
# Can be used for Copying a string

print(fav_movie[0:])
print(fav_movie[:])  # Start value is 0 and prints till the end

# e.g:
a = fav_movie[:]

# Only 'Wick' using slice
print(fav_movie[5:])
print(fav_movie[5:9])
print(fav_movie[-4:])

# 3rd value: fav_movie[start:end:step] - default step is +1
# means that you're taking 1 step or 1 jump
# J +1 O +1 H +1 N

print(fav_movie[2:9:2])  # Skips every second letter
# Output h ik --> skipped n, W, c

# Reverse string, step < 0 (=-1)
print(fav_movie[::-1])  # kciW nhoJ

print(fav_movie[-4::-1])  # W nhoJ

print(
    fav_movie[-4:-2:-1]
)  # Won't work because we're trying to step in reverse, so we won't reach -2 (+1)
print(fav_movie[-4:-9:-1])

fav_hero = "The Hulk"

# Output: The hulk
# Strings are immutable - cannot modify

print(fav_hero[:3] + " h" + fav_hero[5:])

# Repeat operator (*)
print("💓" * 20)

# Case modifying methods
catchphrase = "I am Groot"

print(catchphrase.upper())  # I AM GROOT
print(catchphrase.lower())  # i am groot
print(catchphrase.capitalize())  # I am groot
print(catchphrase.title())  # I Am Groot
print(catchphrase.swapcase())  #

# .strip only removes leading & trailing characters
# String methods does not modify the original value (Immutable)

message = "   With great power comes great responsibility   "
clean_message = message.strip()
print(message)
print(clean_message)

coded_message = "********SO*S******"
decoded = coded_message.strip("*")
print(decoded)  # SO*S

# message.lstrip()
# message.rstrip()

# How many times Dream is repeated?
quote = "Dream is not something that you see in sleep, Dream is something that does not let you sleep"
print(quote.count("Dream"))

# Replace word Dreams

print(quote.replace("Dreams", "🛌☁️"))

# Find gives you the index of the first occurrence (first letter of the word)

print(quote.find("something"))  # index 13 (always first occurrence)
print(quote.find("**"))  # returns -1 (it's not found in sentence)
