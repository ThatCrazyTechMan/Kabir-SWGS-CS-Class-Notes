user_input = input("Enter a word: ")

input_arr = []
for char in user_input:
    input_arr.append(char.lower())

VOWELS = ['a', 'e', 'i', 'o', 'u', ]

vowels_in_word = []
for char in range(len(user_input)):
    if user_input[char] in VOWELS:
        vowels_in_word.append(user_input[char])
        input_arr[char] = '#'

print(vowels_in_word)
vowels_in_word.reverse()
print(vowels_in_word)

counter = 0
for i in range(len(input_arr)):
    if input_arr[i] == '#':
        input_arr[i] = vowels_in_word[counter]
        counter += 1
print(''.join(input_arr))