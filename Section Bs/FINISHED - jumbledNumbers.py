
input_arr = []
user_input = (input("Enter a series of numbers: "))
for entry in user_input:
    input_arr.append(int(entry))
# Change the "int()" to a "str()" if you want to append text
print(f"You entered {input_arr}")

is_jumbled = True

for i in range(len(input_arr) -1):
    if abs(input_arr[i] - input_arr[i+1]) > 1:
        is_jumbled = False

if is_jumbled:
    print('The number you entered is jumbled')
else:
    print('The number you entered is not jumbled')