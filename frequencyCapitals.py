import string

input_arr = []
user_input = (input("Enter a word. Ensure that you only use letters A-F: "))
for entry in user_input:
    input_arr.append(str(entry))
# Change the "int()" to a "str()" if you want to append text
print(f"You entered {input_arr}")

validLetters = ['a, b, c, d, e, f']

for i in input_arr:
    if i in validLetters == False:
        print(f"Invalid letter: {i}")
        break


def most_common(lst):
    return max(set(lst), key=lst.count)

mostCommonLetter = most_common(input_arr)

for i in range(len(input_arr)):
    if i == mostCommonLetter:
        input_arr[i] = input_arr[i.upper]

print(input_arr)