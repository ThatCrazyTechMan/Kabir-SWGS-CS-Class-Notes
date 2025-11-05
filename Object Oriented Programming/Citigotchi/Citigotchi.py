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
        self.hunger = newHunger
    def changeHappiness(self, newHappiness):
        self.happiness = newHappiness


class Dragon:
    def __init__(self, dragonSpecies, dragonHealth, randomCritChance):
        self.dragonSpecies = dragonSpecies
        self.dragonHealth = dragonHealth
        self.randomCritChance = randomCritChance

    def getDragonSpecies(self):
        return self.dragonSpecies
    def getDragonHealth(self):
        return self.dragonHealth
    def getRandomCritChance(self):
        return self.randomCritChance
    def damageDragon(self, damage):
        self.dragonHealth -= damage


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
        pet.hunger -= 0.25
        if pet.hunger < 0.5:
            pet.happiness += 0.25
            return 'Your pet is satisfied!'
        elif pet.hunger == 1:
            print('Your pet died')

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
        pet.hunger += 0.4;
        if pet.hunger < 0.5:
            pet.happiness += 0.2
            return 'Your pet had a good workout!.'

        pet.happiness -= 0.25;
        return 'Your pet is exhausted and hungry!'

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
        print(Pet.getCatchphrase)






def main():
    petName = input('What is the name of your pet? ')
    speciesList = ['Dolphin', 'Monkey', 'Penguin', 'Shark', 'Octopus', 'Squid', 'Mouse', 'Blobfish', 'Snake', 'Vietnamese Mossy Frog']
    speciesCatchphrase = ['Screech', '']

    species = random.choice(speciesList)

    pet = Citigotchi(petName, species, '100', '10', '')

    actions = []
    actions.append(Eat())
    actions.append(Exercise())

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
                print(action.doAction(pet) + '\n')
                didAction = True
                break

        if not didAction and choice != 'QUIT':
            print('Invalid action. Try again.\n')

    print('\nThanks for playing Citigotchi! See you next time!\n')


main()


