user_input = input('Enter a number in roman numerals: ')
input_array = []
for i in user_input:
    input_array.append(i)


for i in range(len(input_array)):
    if input_array[i] == 'X':
        input_array[i] = 10
    elif input_array[i] == 'V':
        input_array[i] = 5
    elif input_array[i] == 'I':
        input_array[i] = 1

print(input_array)

def is_descending(numbers):
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            return False
    return True

def sum_array(array):
    sum = 0
    for i in array:
        sum += i
    return sum


def subtractOne(array):
    for i in range(len(array)):
        if array[i-1] == 1:
            array[i] -= 1
            array.remove(array[i-1])
    return array

if is_descending(input_array):
    print(sum_array(input_array))
else:
    print(sum_array(subtractOne(input_array)))


