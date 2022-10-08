import random

class Weapon():
    def __init__(self, name):
        self.name = name
    
    def show_stats(self):
        raise NotImplementedError("Hay que definir la muestra de stats del arma")

class Sword(Weapon):
    
    def __init__(self, name, damage_min, damage_max):
        Weapon.__init__(self, name)
        self.damage_min = damage_min
        self.damage_max = damage_max

    def __str__(self):
        return f"Espada {self.name}: {self.damage_min} - {self.damage_max}"
        
    def show_stats(self):
        print(f"Espada {self.name}: {self.damage_min} - {self.damage_max}")
              
    def attack(self):
        return random.randint(self.damage_min,self.damage_max)

class Mace(Weapon):
    
    def __init__(self, name, damage_min, damage_max):
        Weapon.__init__(self, name)
        self.damage_min = damage_min
        self.damage_max = damage_max

    def __str__(self):
        return f"Maza {self.name}: {self.damage_min} - {self.damage_max}"
        
    def show_stats(self):
        print(f"Maza {self.name}: {self.damage_min} - {self.damage_max}")
              
    def attack(self):
        return random.randint(self.damage_min,self.damage_max)

class Bow(Weapon):
    
    def __init__(self, name, damage_min, damage_max):
        Weapon.__init__(self, name)
        self.damage_min = damage_min
        self.damage_max = damage_max

    def __str__(self):
        return f"Arco {self.name}: {self.damage_min} - {self.damage_max}"
        
    def show_stats(self):
        print(f"Arco {self.name}: {self.damage_min} - {self.damage_max}")
              
    def attack(self):
        return random.randint(self.damage_min,self.damage_max)

class Crossbow(Weapon):
    
    def __init__(self, name, damage_min, damage_max):
        Weapon.__init__(self, name)
        self.damage_min = damage_min
        self.damage_max = damage_max

    def __str__(self):
        return f"Ballesta {self.name}: {self.damage_min} - {self.damage_max}"
        
    def show_stats(self):
        print(f"Ballesta {self.name}: {self.damage_min} - {self.damage_max}")
              
    def attack(self):
        return random.randint(self.damage_min,self.damage_max)