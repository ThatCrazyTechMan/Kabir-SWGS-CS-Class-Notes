input_arr = []
user_input = (input("Enter a series of numbers: "))
numbers = user_input.split()
for number in numbers:
    input_arr.append(int(number))
print(f"You entered {input_arr}")

for number in input_arr:
    result = input_arr[number] + input_arr[number+1]
print(result)