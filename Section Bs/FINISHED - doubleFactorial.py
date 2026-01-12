
input_num = int(input('Enter a number: '))

numbers = []
while input_num > 0:
    numbers.append(input_num)
    input_num -= 2
print(numbers)

def findProduct(arr):
    product = 1
    for num in arr:
        product *= num
    return product

print(findProduct(numbers))