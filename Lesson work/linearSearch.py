cars = ["Vauxhaull","Skoda","Ford","Volvo","Volkswagen","Renault","Toyota","Nissan","Saab"]
search_car = input("Search car: ")

found = False

for i in range(len(cars)):
    if cars[i] == search_car:
        print(f"Found {cars[i]} at index {i}")
        found = True
        break


if not found:
    print(f"Could not find {search_car}")
