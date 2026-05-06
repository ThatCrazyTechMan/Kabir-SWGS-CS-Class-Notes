
def roman(user_input):
    expression = list(user_input)

    isValid = True
    sum = 0

    # test for too many vals

    xCount = len([i for i in expression if i == "X"])
    vCount = len([i for i in expression if i == "V"])

    firstV = expression.index("V")
    lastV = 0

    # check for too many Is
    for i in range(len(expression) - 1, 0, -1):
        if expression[i] == "V":
            lastV = i
            break

    iCountEnd = len([i for i in expression[lastV + 1:] if i == "I"])
    iCountBefore = len([i for i in expression[:lastV] if i == "I"])
    print(lastV)
    print(iCountBefore)

    # check for invalid num of chars
    if xCount > 3 or vCount > 3 or iCountEnd > 3:
        isValid = False

    print(xCount, vCount)

    # check for invalid Is
    if iCountBefore > 0:
        if "I" in expression[:xCount - 1]:
            isValid = False
        if "I" in expression[xCount:(xCount + vCount - 2)]:
            isValid = False


    for i in range(len(expression)):
        # look at Xs
        if expression[i] == "X":
            sum += 10
        if expression[i] == "V":
            sum += 5
        if expression[i] == "I":
            if expression[i + 1] == "X" or expression[i + 1] == "V":
                sum -= 1
            else:
                sum += 1
    if isValid:
        return sum
    else:
        return -1
user_input = input("Enter a roman numeral expression: ").upper()
expression = roman(user_input)

print(expression)