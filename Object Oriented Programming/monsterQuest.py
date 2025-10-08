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
    def take_damage(self, damage_amount):
        self.health = self.health - damage_amount
    def change_catchphrase(self, new_catchphrase):
        self.catchphrase = new_catchphrase

class Weapon:
    def __init__(self, damage_amount, noise, target):
        self.damage_amount = damage_amount
        self.noise = noise
        self.target = target

    # Getters
    def get_noise(self):
        return self.noise
    def get_target(self):
        return self.target

    # Setters
    def attack(self):



damage_amount = 10

Puran = Monster('Puran', 'He was molested as a baby boy', '67')
print(Puran.get_name())
print(Puran.get_catchphrase())
print(Puran.get_health())
Puran.take_damage(damage_amount)
print(Puran.get_health())

Sonny = Monster('Sonny', 'Wadrdrdrdd I do?', '50')
print(Sonny.get_name())
print(Sonny.get_catchphrase())
print(Sonny.get_health())
Sonny.take_damage(damage_amount)
print(Sonny.get_health())

Vince = Monster('Vince', "My collar's blue, but my neck is red", '68')
print(Vince.get_name())
Vince.speak()
print(Vince.get_health())
Vince.take_damage(damage_amount)
print(Vince.get_health())


