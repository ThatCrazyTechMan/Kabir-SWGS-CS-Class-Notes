import random

class Game:
    def __init__(self, player_health):
        self.monsters = []
        friend1 = Friend("Sonny", "Wardrdrdr I do???", "67", "Put 'er there pal", "Monster energy")
        self.monsters.append(friend1)
        enemy1 = Enemy("Lilly", "I'm not posh, I'm comfortable!!!", "41", "I'm going to crashout!!", "Here's a knuckle sandwich!!")
        self.monsters.append(enemy1)
        self.player_health = player_health
        print("Completed method")
        self.play_game()

    def get_monsters_list(self):
        return self.monsters
    def take_damage(self, damage):
        self.player_health -= damage
    def get_health(self):#
        return self.player_health


    def play_game(self):
        while self.player_health > 0:
            opponent = random.choice(self.monsters)
            choice = input("Will you (f)ight or (h)ighfive?")
            if choice == "f":
                result = opponent.fight()
                self.player_health += result
                print("Health is: ", self.player_health)
            elif choice == "h":
                result = opponent.highFive
                self.player_health += result
                print("Health is: ", self.player_health)
        print("You Died!!")



        

class Monster:
    def __init__(self, name, catchphrase, health):
        self.name = name
        self.catchphrase = catchphrase
        self.health = int(health)

        # Call me David the way I Getter
    def get_name(self):
        return self.name
    def get_catchphrase(self):
        return self.catchphrase
    def get_health(self):
        return self.health
    def change_name(self, new_name):
        self.name = new_name
    def speak(self):
        print(self.catchphrase)

        # Setters
    def hurt(self, damage_amount):
        self.health = self.health - damage_amount
    def change_catchphrase(self, new_catchphrase):
        self.catchphrase = new_catchphrase
        print('You did 10 points of damage!!')
    def changeGift(self, new_gift):
        self.gift = new_gift

class Friend(Monster):
    def __init__(self, name, catchphrase, health, highfive_dialogue, gift):
        super().__init__(name, catchphrase, health)
        self.highfive_dialogue = highfive_dialogue
        self.gift = gift
        self.isFriend = True

    def highFive(self):
        print(self.name + ' raises their hand and says... ' + self.highfive_dialogue)
        print(self.name + ' then gives you ' + self.gift)
        return 10
    def giveGift(self):
        print(self.name + ' gives you ' + self.gift)
    def fight(self):
        print("Hey! You can't fight me! I'm your friend!!")
        return -10


class Enemy(Monster):
    def __init__(self, name, catchphrase, health, highfive_dialogue, gift):
        super(). __init__(name, catchphrase, health,)
        self.highfive_dialogue = highfive_dialogue
        self.gift = gift
        self.isFriend = False

    def highFive(self):
        print(self.highfive_dialogue)
        return -10
    def giveGift(self):
        print(self.gift)
    def fight(self):
        print("AAARRHGGGHH!!! I'll get you next time!!")
        self.health -= 10
        return 10

game1 = Game(50)



