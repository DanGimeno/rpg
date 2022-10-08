from abc import ABC, abstractmethod

class Hero(ABC):
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        raise NotImplementedError("Debes implementar la funcion de hablar")
        
    def showStats(self):
        raise NotImplementedError("Debes implementar la funcion de mostrar stats")

    def giveWeapon(self, weapon):
        raise NotImplementedError("Debes implementar la funcion de dar un arma")

    @abstractmethod
    def heal(self, hp):
        raise NotImplementedError()

    @abstractmethod
    def damage(self, hp):
        raise NotImplementedError()

    def defending(self, defending):
        raise NotImplementedError()

class Warrior(Hero):
    
    def __init__(self, name):
        Hero.__init__(self, name)
        self.type = "Guerrero"
        self.stats = {}
        self.stats['health'] = 100
        self.stats['health_max'] = 100
        self.stats['strength'] = 15
        self.stats['defense'] = 9
        self.stats['dex'] = 8
        self.weapon = None
        self.main_attr_attack = "strength"

        self.defending_flag = 0

    def speak(self):
        print("Soy un Guerrero y me llamo " + self.name)
        
    def showStats(self):
        for stat in self.stats:
            print(stat, self.stats[stat], sep=": ")

    def __str__(self):
        return '''
%s, %s
Vida: %s / %s 
''' % (self.name, self.type, self.stats['health'], self.stats['health_max'])        

    def giveWeapon(self, weapon):
        self.weapon = weapon

    def heal(self, hp):
        self.stats['health'] = min(self.stats['health'] + hp, self.stats['health_max'])

    def damage(self, hp):
        self.stats['health'] = max(self.stats['health'] - hp, 0)
        return self.stats['health'] > 0

    def defending(self, defending):
        self.defending_flag = defending

    

class Archer(Hero):
    
    def __init__(self, name):
        Hero.__init__(self, name)
        self.type = "Arquero"
        self.stats = {}
        self.stats['health'] = 80
        self.stats['health_max'] = 80
        self.stats['strength'] = 8
        self.stats['defense'] = 7
        self.stats['dex'] = 15
        self.main_attr_attack = "dex"
        self.weapon = None
        
        self.defending_flag = 0
    
    def speak(self):
        print("Soy un Arquero y me llamo " + self.name)
        
    def showStats(self):
        for stat in self.stats:
            print(stat, self.stats[stat], sep=": ")

    def __str__(self):
        return '''
%s, %s
Vida: %s / %s 
''' % (self.name, self.type, self.stats['health'], self.stats['health_max'])     

    def giveWeapon(self, weapon):
        self.weapon = weapon

    def heal(self, hp):
        self.stats['health'] = min(self.stats['health'] + hp, self.stats['health_max'])

    def damage(self, hp):
        self.stats['health'] = max(self.stats['health'] - hp, 0)
        return self.stats['health'] > 0

    def defending(self, defending):
        self.defending_flag = defending
