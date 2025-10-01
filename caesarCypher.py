import string

input_arr = []
user_input = (input("Enter a word: "))
for entry in user_input:
    input_arr.append(str(entry))
# Change the "int()" to a "str()" if you want to append text
print(f"You entered {input_arr}")

shift_num = int(input("Enter a shift number: "))

def rightRotateByOne(arr, shift):
    for i in range(shift):
        temp = arr[0]
        for i in range(len(arr)-1):
            arr[i] = arr[i + 1]
        arr[-1] = temp
    return arr
def leftRotateByOne(arr, shift):
    for i in range(shift):
        arr.insert(0,arr[-1])
    return arr





print(rightRotateByOne(input_arr, shift_num))
print(leftRotateByOne(input_arr, shift_num))
