import math as math
import random

input_number = int(input("Enter a number: "))
arr = []


for i in range(1, input_number + 1):
    arr.append(i)

print(arr)


def isConsecutive(num1, num2):
    if abs(num2 - num1) == 1:
        return True
    else:
        return False



def politeness(input_arr):
    current_sum = 0
    while current_sum != input_number:
        for in arr:

