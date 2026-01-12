
input_arr = []
user_input = (input("Enter a series of numbers: "))
for entry in user_input:
    input_arr.append(int(entry))
# Change the "int()" to a "str()" if you want to append text
print(f"You entered {input_arr}")

workingNumbers = ''
for i in range(0, len(input_arr)):
    if input_arr[i] == 9:
        workingNumbers += str(input_arr[i]) + str(input_arr[i + 1])

print(workingNumbers)
