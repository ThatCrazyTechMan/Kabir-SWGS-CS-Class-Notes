birth_year = int(input("What year were you born? "))


#Function example
def calculate_age(birth_year):
    import datetime
    age = datetime.date.today().year - birth_year
    return(age)

print(calculate_age(birth_year))




#procedure example
text = str(input("Enter the text you want to spam: "))
multiplier = int(input("Enter the number of times you want to spam the text: "))
def spam_print(text, multiplier):
    for i in range(0,multiplier+1):
        print(i,text)
spam_print(text, multiplier)


#Factorial

def factorial(num):
    if num == 0:
        result = 1
    else:
        result = num * factorial(num-1)
    return result

number = int(input("Enter the number you want to find the factorial of: "))
print(factorial(number))