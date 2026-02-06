## Read text file
try:
    with open("text_file.txt", "r") as text_file:
        print(text_file.read())
except FileNotFoundError:
    print("File not found")

try:
    with open("text_file.txt", "a") as text_file:
        text_file.write("Hello World\n")

except FileNotFoundError:
    print("File not found")

# Read specific lines
try:
    with open("text_file.txt", "r") as text_file:
        file = text_file.readlines()
except FileNotFoundError:
    print("File not found")
