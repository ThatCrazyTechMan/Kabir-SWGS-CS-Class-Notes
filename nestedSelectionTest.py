age = int(input("Enter your age: "))
weight = bool(input("Enter your weight: "))
height = bool(input("Enter your height: "))

if age < 10:
    print("You are too young")
elif weight < 40:
    print("You don't weigh enough")
elif height < 120:
    print("You're not tall enough")
else:
    print("Welcome")