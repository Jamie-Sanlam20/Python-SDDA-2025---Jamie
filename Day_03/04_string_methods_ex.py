secret_message = "     Programming in Python is not only powerful but also fun!   "

# 1. Solve it in the easiest way
# 2. Make it better

# Task 1.1

clean_message = secret_message.strip()
new_message = clean_message[15:21].upper() + "-" + clean_message[34:42].upper()
print(new_message)

# Task 1.2
flipped_message = "!nuf sseldnE dna seitinutroppo lufrewop htiw nohtyP"

# Expected Output
# "python 🗡️ powerful 🌸"

reverse_message = flipped_message[::-1]
new_message = reverse_message[0:6].lower() + " 🗡️ " + reverse_message[12:20] + " 🌸 "
print(new_message)


# Task 1.3

# After the 🔑
message = "    🚨🔍📱🔑secret_code✌️"

# Output
# SECRET_CODE✌️

key_index = message.find("🔑")
# because you don't know the index number - emojis included - you use find
decoded_msg = message[key_index + 1 :].upper()
print(decoded_msg)
