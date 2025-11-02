import string

input_arr = []
user_input = (input("Enter a sentence: ")).lower()
for entry in user_input:
    input_arr.append(str(entry))
# Change the "int()" to a "str()" if you want to append text
print(f"You entered {input_arr}")

ALPHABET = []
for i in string.ascii_lowercase:
    ALPHABET.append(i)

foundLetters = []
for i in ALPHABET:
    if i in user_input:
        foundLetters.append(i)

differenceArray = list(set(ALPHABET) - set(foundLetters))

if len(differenceArray)==0:
    print("This is a valid pangram")
else:
    print(f"This is an invalid pangram. You missed {differenceArray}")
