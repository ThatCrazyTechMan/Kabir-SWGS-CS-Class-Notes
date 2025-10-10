def convert_to_nibbles(input):
    output = [(input[i:i+4]) for i in range(0, len(input), 4)]
    return output

input_arr = []
user_input = (input("Enter a series of numbers: "))
for entry in user_input:
    input_arr.append(int(entry))
# Change the "int()" to a "str()" if you want to append text
print(f"You entered {input_arr}")



PLACE_VALUE = [8, 4, 2, 1]
HEX_VALUES = ['A', 'B', 'C', 'D', 'E', 'F']

def nibble_to_hex(nibble):

    output = 0
    for i in range(0, len(nibble)):
        output += PLACE_VALUE[i]*int(nibble[i])

    try:
        hex_output = HEX_VALUES[int(str(output)[1])]
    except:
        hex_output = output
    return hex_output

input = convert_to_nibbles(user_input)

final_output = ''
for i in range(0, len(input)):
    final_output += str(nibble_to_hex(input[i]))
print(final_output)


