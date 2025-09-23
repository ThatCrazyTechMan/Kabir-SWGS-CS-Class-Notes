input_arr = []
user_input = (input("Enter a series of numbers: "))
numbers = user_input.split()
for number in numbers:
    input_arr.append(float(number))
print(f"You entered {input_arr}")

def add_numbers(adding_input):
    if adding_input == 1:
        return 0
    else:
        return adding_input [0] + add_numbers(adding)

result = add_numbers(input_arr)
print(result)