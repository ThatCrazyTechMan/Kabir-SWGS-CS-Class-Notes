rpn = input("Please enter an RPN sum: ")
stack = []
operators = ["+", "-", "*", "/"]
for i in range(len(rpn)):
    if rpn[i] not in operators:
        stack.append(int(rpn[i]))
    else:
        num1 = stack.pop()
        num2 = stack.pop()
        if rpn[i] == "+":
            result = num1 + num2
            stack.append(result)
        elif rpn[i] == "-":
            result = num2 - num1
            stack.append(result)
        elif rpn[i] == "*":
            result = num1 * num2
            stack.append(result)
        elif rpn[i] == "/":
            result = num2 / num1
            stack.append(result)

print(stack)