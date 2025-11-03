def validate_length(string):
    if 5 <= len(string) <= 7:
        return True
    else:
        return False

def is_uppercase(string):
    uppercase = string.upper()
    if uppercase == string:
        return True
    else:
        return False

def is_unique(string):
    arr = []
    for char in string:
        arr.append(char)
    unrepeated = set(arr)
    if len(unrepeated) == len(arr):
        return True
    else:
        return False

def ascii_sum(string):
    sum = 0
    for char in string:
        sum += ord(char)
    if 420 <= sum <= 600:
        return True
    else:
        return False

isValid = False
while isValid ==False:
    user_input = input("Enter a word: ")
    if validate_length(user_input):
        if is_uppercase(user_input):
            if is_unique(user_input):
                if ascii_sum(user_input):
                    print("The word is valid !!")
                    isValid = True
                else:
                    print("The word is not between 420 and 600 in ASCII")
            else:
                print("The word is not unique")
        else:
            print("The word is not uppercase")
    else:
        print("The word is not between 5 and 7 characters")

