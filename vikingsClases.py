
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength
    def receiveDamage(self, damage):
        self.health = self.health - damage


# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
    def attack(self):
        return self.strength
    def receiveDamage (self):
        self.health = self.health - damage
        if self.health > 0:
            return(str(name) + ' has received ' + str(damage) + ' points of damage')
        else:
            return (str(name) + ' has died in act of combat')
    def battleCry(self):
        return 'Odin Owns You All!'

# Saxon
class Saxon(Soldier):
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    def attack(self):
        return self.strength

    def receiveDamage(self):
        self.health = self.health - damage
        if self.health > 0:
            return ('Saxon has received ' + str(damage) + ' points of damage')
        else:
            return ('Saxon has died in act of combat')
# War


class War:
    pass
