user_input = input("Enter a number: ")

def isPalindrome(num):
    if str(num)[::-1] == str(num):
        return True
    else:
        return False

input_denary = int(user_input)
input_binary = bin(input_denary)[2:]

is_double_palindrome = False

if isPalindrome(input_denary) and isPalindrome(input_binary):
     is_double_palindrome = True
else:
    is_double_palindrome = False

if is_double_palindrome:
    print("Double palindrome")
else:
    print("Not double palindrome")