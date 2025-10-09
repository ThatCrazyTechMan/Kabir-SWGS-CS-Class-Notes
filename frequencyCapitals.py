import string

input_arr = []
user_input = (input("Enter a word. Ensure that you only use letters A-F: "))
for entry in user_input:
    input_arr.append(str(entry))
# Change the "int()" to a "str()" if you want to append text
print(f"You entered {input_arr}")

def most_common(lst):
    return max(set(lst), key=lst.count)

valid = set('abcdef')

for i in input_arr:
    if i.lower() not in valid:
        print(f"Invalid letter: {i}")
        exit()
    else:
        mostCommonLetter = most_common(input_arr)

        for i in range(len(input_arr)):
            if input_arr[i] == mostCommonLetter:
                input_arr[i] = input_arr[i].upper()
    # Super annoying error, where if you input 'face', all letters apart from 'a' get capitalised. I want the output to be 'FACE' not 'FaCE'

print(input_arr)

output = ''.join(input_arr)

print(output)