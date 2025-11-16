import datetime
from datetime import datetime

name = input("What's your name? ")

print(f"Hello, {name}! Nice to meet you.")

current_year = datetime.now().year

born_year = int(input("What year were you born? "))

age = current_year - born_year

if age > 90:
    print(f"It's shocking to know you are {age} year olds.")
else:
    print(f"It's great to know you are {age} year olds.")
