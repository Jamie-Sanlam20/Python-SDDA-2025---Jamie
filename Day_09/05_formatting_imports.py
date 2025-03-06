from datetime import datetime  # Imports on top of the file
from math import cos, pi  # Inbuilt

print(pi)
print(cos(pi / 2))
print(cos(0))

now = datetime.now()
print(now)


print(f"The Current date is: {now:%d-%m-%Y}")  # 06-03-2025
print(f"The Current date is: {now:%d/%m/%Y}")  # 06/03/2025
print(f"The Current date is: {now:%d %m %Y}")  # 06 03 2025
print(f"The Current date is: {now:%d %B %Y}")  # 06 March 2025
print(f"The Current date is: {now:%d %b %Y}")  # 06 Mar 2025

# 2025-12-28 # Dev
