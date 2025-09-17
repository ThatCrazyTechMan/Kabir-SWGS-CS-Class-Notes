width = float(input("Enter the width of the Rectangle: "))
length = float(input("Enter the length of the Rectangle: "))
height = float(input("Enter the height of the Rectangle: "))

volume = width * length * height
print(volume)

face_one_area = length * height
face_two_area = width * height
face_three_area = length * width



surface_area = (2 * face_one_area) + (2 * face_two_area) + (2 * face_three_area)
print(surface_area)