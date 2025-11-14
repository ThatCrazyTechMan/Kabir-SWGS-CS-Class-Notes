import random

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
        super().__init__(name, "Dolphin")

class CitiMech(Citigotchi):
    def __init__(self, name, species, happiness, hunger, catchphrase, ability):
        super().__init__(self, name, species, happiness, catchphrase)
        self.hunger = hunger
        self.ability = ability

    def getEnergy(self):
        return self.power
    def getAbility(self):
        return self.ability
    def decreaseHunger(self, subtractor):
        pet.setHunger(subtractor)



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
        print(pet.getHunger())
        if pet.getHunger() < 0.5:
            return 'Your pet is satisfied!'


        pet.happiness -= 0.1
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
            return 'Your pet had a good workout!.' + str(pet.getHunger()) + str(pet.getHappiness())

        pet.changeHappiness(-0.25);
        return 'Your pet is exhausted and hungry!' + str(pet.getHunger()) + str(pet.getHappiness())

#class fightADragon(Action):
#    @staticmethod
#    def getCommand():
#        return 'FIGHTADRAGON'
#
#    @staticmethod
#    def getMenuMessage():
#        return 'fight a dragon!!.'
#
#    @staticmethod
#    def doAction(pet):
#        dragons = [['firebreather', 'icebreather', 'asthmatic', 'arthritic'],[100,75,50,25],[0.20, 0.4,0.55,0.75]]
#        number = random.randint(0,3)
#        opponentDragon = Dragon(dragons[0][number], dragons[1][number], dragons[2][number])
#        choice = input('Do you want to (f)ight or (s)hield?')
#        if choice == 'f':
#            opponentDragon.damageDragon(10)


class speak(Action):
    @staticmethod
    def getCommand():
        return 'SPEAK'

    @staticmethod
    def getMenuMessage():
        return 'Make your pet speak'

    @staticmethod
    def doAction(pet):
        return pet.getCatchphrase()


class getANewPet(Action):
    @staticmethod
    def getCommand():
        return 'NEW PET'
    @staticmethod
    def getMenuMessage():
        return 'Get a new pet.'
    @staticmethod
    def doAction(pet):
        main()

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

    actions = []
    actions.append(Eat())
    actions.append(Exercise())
    actions.append(getANewPet())
    actions.append(speak())
    actions.append(mechanise())
    actions.append(mechPower())

    print('########################\n')
    print(f'Welcome to Citigotchi! Your pet is {pet.getName()} the {pet.getSpecies()}')

    choice = ''

    while choice != 'QUIT':

        print('Enter one of the following commands:\n')
        for action in actions:
            print('{} --- {}'.format(action.getCommand(), action.getMenuMessage()))
        print('QUIT --- Quit the game.')

        choice = input(">> ").upper()
        didAction = False
        for action in actions:
            if choice == action.getCommand():
                result = action.doAction(pet)
                if result == 'Mechanising underway':
                    pet = CitiMech(pet.getName, pet.getSpecies, pet.getHappiness, pet.getHunger, speciesCatchphrase, MechPower)
                print(result + '\n')
                didAction = True
                break
        if pet.getHunger() == 1 or pet.getHappiness() == 0:
            print('Your pet is dead!!')
            quit()
        if not didAction and choice != 'QUIT':
            print('Invalid action. Try again.\n')

    print('\nThanks for playing Citigotchi! See you next time!\n')


main()


