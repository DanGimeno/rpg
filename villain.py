from abc import ABC, abstractmethod

class Villain(ABC):
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

class Orc(Villain):
    
    def __init__(self, name):
        Villain.__init__(self, name)
        self.type = "Orco"
        self.stats = {}
        self.stats['health'] = 45
        self.stats['health_max'] = 45
        self.stats['strength'] = 11
        self.stats['defense'] = 9
        self.stats['dex'] = 6
        self.weapon = None
        self.main_attr_attack = "strength"

        self.defending_flag = 0
    
    def speak(self):
        print("Soy un Orco y me llamo " + self.name)
        
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
    

class Limo(Villain):
    
    def __init__(self, name):
        Villain.__init__(self, name)
        self.type = "Limo"
        self.stats = {}
        self.stats['health'] = 25
        self.stats['health_max'] = 25
        self.stats['strength'] = 30
        self.stats['defense'] = 9
        self.stats['dex'] = 7
        self.weapon = None
        self.main_attr_attack = "strength"

        self.defending_flag = 0
    
    def speak(self):
        print("Soy un Limo y me llamo " + self.name)
        
    def show_stats(self):
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