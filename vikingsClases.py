
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

    def receiveDamage (self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return(str(self.name) + ' has received ' + str(damage) + ' points of damage')
        else:
            return (str(self.name) + ' has died in act of combat')
    def battleCry(self):
        return 'Odin Owns You All!'

# Saxon
class Saxon(Soldier):
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return ('A Saxon has received ' + str(damage) + ' points of damage')
        else:
            return ('A Saxon has died in combat')
# War


class War:
    def __init__(self):
        vikingArmy = ()
        saxonArmy = ()
    def addViking(self, Viking):
        self.vikingArmy.append(Viking)
    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)
    def vikingAttack(self):
        receiveDamage(Saxon, self.strength)
        if Saxon.health >0:
            Saxon.saxonArmy.remove(Saxon)
        return receiveDamage(Saxon, self.strength)
    def saxonAttack(self):
        receiveDamage(Viking, self.strength)
        if Viking.health >0:
            Viking.vikingArmy.remove(Viking)
        return receiveDamage(Viking, self.strength)
    def showStatus(self):
        if len(vikingArmy(0)):
            return 'Vikings have won the war of the century!'
        elif len(saxoArmy(0)):
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."




