input_arr = []
user_input = (input("Enter a word: "))
for letter in user_input:
    input_arr.append((letter))
print(f"You entered {input_arr}")

final_array = []
last_char = ""
last_char_count = 0
for i in range(len(user_input)):
    if user_input[i - 1] == user_input[i]:
        final_array.append(f"{user_input[i]}, 1")
    else:
        last_char_count += 1
        final_array.append(f"{user_input[i]}, {last_char_count}")

print(final_array)

