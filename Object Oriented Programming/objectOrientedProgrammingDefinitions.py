# Create a class
class Pet:
# Start the class
# We take in what will be the attributes as an input to the function
    def __init__(self, name, species, description):
        # Then, we give the class its attributes with the names we have passed into the function
        self.name = name
        self.species = species
        self.description = description

# Straight printing from the class is bad practise. Instead, we write a method to access the data called a 'Getter'
    def get_name(self):
        return self.name
    def get_species(self):
        return self.species
    def get_description(self):
        return self.description
# If we ever want to change an attribute, eg, the name, we write a function called a setter method
    def setName(self, name):
        self.name = name


# Here, we can add an instance of this class
my_pet_1 = Pet('Count Pubert Finklesworth VI, lord of darkness, angel of the bottomless pit, prince of lies and spawn of Satan', 'Calico', 'sillicate')
print(my_pet_1.name)
print(my_pet_1.species)
print(my_pet_1.description)

my_pet_2 = Pet('Countess Mimbulus Finklelsworth II, Progeny of evil, spouse of the lord of darkness, mistress of the dark fortress, guardian of evil', 'Orange', 'Hungry')

# Here, we call the getter to return the attributes
print(my_pet_1.get_name())
print(my_pet_1.get_species())
print(my_pet_1.get_description())

print(my_pet_2.get_name())
print(my_pet_2.get_species())
print(my_pet_2.get_description())

# Here, we can use setName to change the name of the cart
my_pet_1.setName("car")

print(my_pet_1.get_name())

