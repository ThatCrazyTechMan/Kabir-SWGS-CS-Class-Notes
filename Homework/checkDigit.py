isbn = []
isbn_input = (input("Enter the ISBN: "))
for number in isbn_input:
    isbn.append(int(number))
print(f"You entered {isbn}")
last_digit = isbn.pop()
print(f"Without the last digit, the ISBN is: {isbn}")

weights = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3]
weighted_isbn = []

for count in range(len(isbn)):
    weighted_isbn.append(weights[count] * isbn[count])
print(f"The weighted ISBN is: {weighted_isbn}")

CalculatedDigit = sum(weighted_isbn)
if last_digit == 10 - (CalculatedDigit % 10):
    print("\nThe ISBN is valid")
else:
    print("\nThe ISBN is invalid")
