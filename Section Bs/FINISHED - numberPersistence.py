import math
import re

user_input = (input("Enter a number followed by either 'm' or 'a': "))

persistence_kind = re.sub(r'[0-9]+', '', user_input)

user_input = re.sub(r'\D', '', user_input)

def add(num):
    return sum(int(digit) for digit in str(num))


def prod(num):
    arr = []
    for i in str(num):
        arr.append(int(i))
    return math.prod(arr)


counter = 0

if persistence_kind == "m":
    while len(str(user_input)) > 1:
        user_input = prod(user_input)
        counter += 1
elif persistence_kind == "a":
    while len(str(user_input)) > 1:
        user_input = add(user_input)
        counter += 1

print(counter)
