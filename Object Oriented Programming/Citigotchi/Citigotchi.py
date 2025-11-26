import random
import termcolor

class Citigotchi:
    def __init__(self, name, species, happiness, hunger, catchphrase):
        self.name = name
        self.species = species
        self.happiness = happiness
        self.hunger = hunger
        self.catchphrase = catchphrase

    # Getters
    def getName(self):
        return self.name
    def getSpecies(self):
        return self.species
    def getHappiness(self):
        return self.happiness
    def getHunger(self):
        return self.hunger
    def getCatchphrase(self):
        return self.catchphrase

    # Setters
    def setName(self, newName):
        self.name = newName
    def changeSpecies(self, newSpecies):
        self.species = newSpecies
    def changeHunger(self, newHunger):
        self.hunger -= newHunger
    def changeHappiness(self, newHappiness):
        self.happiness += newHappiness
    def setHunger(self, newHunger):
        self.hunger = newHunger


class Dolphin(Citigotchi):
    def __init__ (self, name, happiness, hunger, catchphrase):
        super().__init__(name, "Dolphin", "1", "0.1", "EE EE EE EE")

class CitiMech(Citigotchi):
    def __init__(self, name, species, happiness, hunger, catchphrase, ability):
        super().__init__(name, species, happiness, hunger, catchphrase)
        self.hunger = hunger
        self.ability = ability

    def getAbility(self):
        return self.ability
    def decreaseHunger(self, subtractor):
        self.hunger += subtractor
    def mechPower(self):
        return f'{self.getName()} uses {self.ability}'



class Action:
    def getCommand(self):
        pass

    def getMenuMessage(self):
        pass

    def doAction(self, pet):
        pass


class Eat(Action):
    @staticmethod
    def getCommand():
        return 'EAT'

    @staticmethod
    def getMenuMessage():
        return 'Feed your pet.'

    @staticmethod
    def doAction(pet):
        pet.changeHunger(0.25)
        if pet.getHunger() < 0.5:
            return 'Your pet is satisfied!'


        pet.changeHappiness(-0.1)
        return 'Your pet is still hungry!'


class Exercise(Action):
    @staticmethod
    def getCommand():
        return 'EXERCISE'

    @staticmethod
    def getMenuMessage():
        return 'Exercise with your pet.'

    @staticmethod
    def doAction(pet):
        pet.changeHunger(-0.25)
        if pet.getHunger() < 0.5:
            pet.changeHappiness(0.2);
            return 'Your pet had a good workout!'

        pet.changeHappiness(-0.25)
        return 'Your pet is exhausted and hungry!'


class speak(Action):
    @staticmethod
    def getCommand():
        return 'SPEAK'

    @staticmethod
    def getMenuMessage():
        return 'Make your pet speak'

    @staticmethod
    def doAction(pet):
        return termcolor.colored(pet.getCatchphrase(), 'red')


class getANewPet(Action):
    @staticmethod
    def getCommand():
        return 'NEW PET'
    @staticmethod
    def getMenuMessage():
        return 'Get a new pet.'
    @staticmethod
    def doAction(pet):
       return 'Saving your pet!'

class releasePet(Action):
    @staticmethod
    def getCommand():
        return 'RELEASE'
    @staticmethod
    def getMenuMessage():
        return 'Release your pet.'
    @staticmethod
    def doAction(pet):
        return 'Releasing your pet!'

class mechanise(Action):
    @staticmethod
    def getCommand():
        return 'MECHANISE'
    @staticmethod
    def getMenuMessage():
        return 'Mechanise your pet.'
    @staticmethod
    def doAction(pet):
        return 'Mechanising underway'

class mechPower(Action):
    @staticmethod
    def getCommand():
        return 'MECH POWER'
    @staticmethod
    def getMenuMessage():
        return 'Use your Mech power'
    @staticmethod
    def doAction(pet):
        if type(pet) == CitiMech:
            pet.decreaseHunger(0.1)
            return pet.mechPower()
        else:
            return 'You have not mechanised your pet yet! You cannot use a Mech power'

def main():
    petName = input('What is the name of your pet? ')
    speciesList = [['Dolphin', 'Monkey', 'Penguin', 'Shark', 'Octopus', 'Squid', 'Mouse', 'Blobfish', 'Snake', 'Vietnamese Mossy Frog'],['Screech', 'Ooh ooh aah aah', 'Squawk', 'Splish splash', 'Gurgle', 'Splosh', 'Squeak', 'Splat', 'Hisssssss', 'Ribbit'],['TurboSplash','SuperSwing', 'HyperHuddle', 'MegaBite','DeltaDazzle', 'InfititeInk', 'Infiltrate', 'DeepDive', 'CyberStrangle','KiloCloak']]


    species = random.choice(speciesList[0])
    index = speciesList[0].index(species)
    speciesCatchphrase = speciesList[1][index]
    MechPower = speciesList[2][index]


    pet = Citigotchi(petName, species, 1, 0.1, speciesCatchphrase)
    available_pets = [pet]
    actions = []
    actions.append(Eat())
    actions.append(Exercise())
    actions.append(getANewPet())
    actions.append(speak())
    actions.append(mechanise())
    actions.append(mechPower())
    actions.append(releasePet())

    print('########################\n')
    print(f'Welcome to Citigotchi! Your pet is {pet.getName()} the {pet.getSpecies()}')

    choice = ''

    while choice != 'QUIT':
        print(f'\n{pet.getName()} the {pet.getSpecies()} - Hunger: {pet.getHunger()}, Happiness: {pet.getHappiness()}\n')
        print(termcolor.colored('Enter one of the following commands:\n', 'yellow'))
        for action in actions:
            print('{} --- {}'.format(action.getCommand(), action.getMenuMessage()))
        print('QUIT --- Quit the game.')
        choice = input(">> ").upper()
        didAction = False
        for action in actions:
            if choice == action.getCommand():
                result = action.doAction(pet)
                if result == 'Mechanising underway':
                    pet = CitiMech(pet.getName(), pet.getSpecies(), pet.getHappiness(), pet.getHunger(), speciesCatchphrase, MechPower)
                elif result == 'Saving your pet!':
                    new_or_old_pet = input('Do you want a (n)ew pet, or to switch to an (e)xisting one: ')
                    if new_or_old_pet == 'e':
                        if pet not in available_pets:
                            available_pets.append(pet)
                            print(f'{pet.getName()} saved')

                        print('Your saved pets:\n')
                        for i, pet_string in enumerate(available_pets):
                            mech_status = " (MECH)" if type(pet) == CitiMech else ""
                            print(f'{i+1}: {pet_string.getName()} the {pet_string.getSpecies()} {mech_status}')
                        choice = input("\n>> ")
                        try:
                            pet_index = int(choice) - 1
                            if 0 <= pet_index < len(available_pets):
                                pet = available_pets[pet_index]
                                print(f'switched to {pet.getName()}!')
                            else:
                                print('Invalid choice!')
                        except ValueError:
                            print('Invalid input!')
                    else:
                        petName = input('What is the name of your new pet? ')
                        species = random.choice(speciesList[0])
                        index = speciesList[0].index(species)
                        speciesCatchphrase = speciesList[1][index]
                        MechPower = speciesList[2][index]

                        pet = Citigotchi(petName, species, 1, 0.1, speciesCatchphrase)
                        available_pets.append(pet)

                elif result == 'Releasing your pet!':
                    available_pets.remove(pet)
                    pet = random.choice(available_pets)


                print(f'{result}\n')
                didAction = True
                break
        if pet.getHunger() <= 0 or pet.getHunger() >= 2 or pet.getHappiness() <= 0:
            print('Your pet is dead!!')
            quit()
            return
        if not didAction and choice != 'QUIT':
            print('Invalid action. Try again.\n')

    print('\nThanks for playing Citigotchi! See you next time!\n')


main()


