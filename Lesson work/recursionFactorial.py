#Factorial

def factorial(num):
    if num == 0:
        result = 1
    else:
        result = num * factorial(num-1)
    return result

number = int(input("Enter the number you want to find the factorial of: "))
print(factorial(number))