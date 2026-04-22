user_input = input('Enter a number in roman numerals: ')
input_array = []
for i in user_input:
    input_array.append(i)

def romanInDecimal(roman):
    if roman == 'I':
        return 1
    elif roman == 'V':
        return 5
    if roman == 'X':
        return 10

arrayInDecimal = []
for i in input_array:
    arrayInDecimal.append(romanInDecimal(i))

print(input_array)
print(arrayInDecimal)

sum = []


if all(arrayInDecimal[i] >= arrayInDecimal[i-1] for i in range(len(arrayInDecimal)-1)):


