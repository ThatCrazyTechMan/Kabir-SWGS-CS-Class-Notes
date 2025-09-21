numberInput = int(input("Enter a number: "))


def addNumbers(number):

    if number <= 0:
       return str("Negative numbers aren't supported")
    else:
        return number + addNumbers(number - 1)


print(addNumbers(numberInput))