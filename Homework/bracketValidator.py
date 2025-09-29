
input_arr = []
user_input = (input("Enter a series of numbers: "))
for entry in user_input:
    input_arr.append(str(entry))
# Change the "int()" to a "str()" if you want to append text
print(f"You entered {input_arr}")

is_left_bracket = False

left_bracket_count = 0
right_bracket_count = 0
for entry in input_arr:
    if entry == "(":
        left_bracket_count += 1
        is_left_bracket = True
    elif entry == ")":
        right_bracket_count += 1
        is_left_bracket = False

if left_bracket_count == right_bracket_count and is_left_bracket == False:
    print("Your input is valid")
else:
    print("Your input is invalid")
