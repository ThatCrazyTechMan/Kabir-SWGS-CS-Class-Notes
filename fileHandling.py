#Method 1
textFile = open("textFile.txt","w")
textFile.write("Hello World\n")
textFile.close()


#Method 2
try:
    with open("text_file.txt","w") as text_file:
        text_file.write("Hello World\n")
except FileNotFoundError:
        print("File not found")
textFile.close()




