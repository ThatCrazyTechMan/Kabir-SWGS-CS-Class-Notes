radius = float(input("Enter the radius of the circle: "))
PI = 3.14159

area = PI * radius**2
area = round(area, 2)
print(area)


userInput = int(input("Enter an integer: "))
print(f"This is your input as an integer",userInput)
print(f"This is your output as a float",float(userInput))
print(f"This is your input as a string",str(userInput))
print(f"This is your output as a boolean",bool(userInput))

userInput = str(input("Enter an input: "))
print(userInput.upper())
print(userInput.lower())
print(len(userInput))
arr = []
for i in userInput:
    arr.append(i)

print(arr)

for i in arr:
