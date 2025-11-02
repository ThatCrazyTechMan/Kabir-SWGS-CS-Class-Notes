
input_arr = []
user_input = (input("Enter a series of numbers: "))
for entry in user_input:
    input_arr.append(int(entry))
# Change the "int()" to a "str()" if you want to append text
print(f"You entered {input_arr}")

sort_arr = sorted(input_arr)

def is_lucky(num):
    return len(num) == len(set(num))

print(is_lucky(sort_arr))