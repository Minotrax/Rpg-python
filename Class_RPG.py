from random import randint
import colorama
from colorama import Fore
from colorama import Style




colorama.init()

class Player:
    def __init__(self, name, health, strength, defense, mana, spells, xp, level):
        self.name = name
        self.health = health 
        self.strength = strength
        self.defense = defense
        self.mana = mana
        self.inventory = [["Potion forte de force"],[Sword.name]]
        self.spells = spells
        self.xp = xp
        self.level = level
    
    def get_damage(self, damage):
        self.health -= damage
        return self.health

    def get_mana(self, cout_mana):
        self.mana -= cout_mana
        print("Le sort coûte", cout_mana, "en mana ! Il vous reste", self.mana, "de mana !")
        return self.mana

    def get_damage_weapon(self):
        pass
            
class Monster:
    def __init__(self, name, type, health, attack, defense,xp):
        self.name = name
        self.type = type # feu, eau, air, terre
        self.health = health
        self.attack = attack
        self.defense = defense
        self.xp = xp


class Spell:
    def __init__(self, name, type, damage, mana):
        self.name = name
        self.type = type # feu, eau, air, terre
        self.damage_spell = damage
        self.mana = mana # coût en mana
        
    def damage(self, Monster_health):
        print(Fore.MAGENTA + "Vous lancez", self.name, "!\n" + Style.RESET_ALL)
        print(Fore.RED + "Le monstre prend", self.damage_spell,"de dégats !" + Style.RESET_ALL)
        Monster_health = Monster_health - self.damage_spell
        return Monster_health
        
    
        

class Weapon:
    def __init__(self, name, type, damage):
        self.name = name
        self.type = type # feu, eau, air, terre
        self.damage = damage

class Potions:
    def __init__(self, name, type, power, ):
        self.name = name
        self.type = type #vie, force, mana
        self.power = power

    def add_caract(self, value_stat):
        return self.power + value_stat 


# ---- class spell
Spell_boule_feu = Spell("Boule de feu", "feu", randint(30,50), 25)
Spell_kawaii = Spell("Poussière d'étoile", "air", randint(25,35), 15)
Spell_canard = Spell("Couin Couin", "eau", randint(35,45), 25)
#Spell_canard_2 = Spell("Couin Couin 2 ", "eau 2", randint(35,45), 25)

# ---- class potions
low_health_potion = Potions("Potion faible de vie","vie", 50)
medium_health_potion = Potions("Potion moyenne de vie","vie", 100)
strong_health_potion = Potions("Potion forte de vie","vie", 150)

low_strength_potion = Potions("Potion faible de force","force", 50)
medium_strength_potion = Potions("Potion moyenne de force","force", 100)
strong_strength_potion = Potions("Potion forte de force","force", 150)

low_mana_potion = Potions("Potion faible de mana","mana", 50)
medium_mana_potion = Potions("Potion moyenne de mana","mana", 100)
strong_mana_potion = Potions("Potion forte de mana","mana", 150)

# ---- class weapons
Sword = Weapon("une épée", "acier", 20)
bow = Weapon("un arc", "bois", 15)
magic_wand = Weapon("une baguette magique", "feu", 40)

# ---- class Monster                                                                                                                                               
Gros_nounours = Monster("Gros nounours", "terre", 150, 40, 20, 150)
Brontis = Monster("Brontis", "feu", 200, 60, 30, 300)
Loic = Monster("Loic", "eau", 250, 80, 40, 450)
Les_impots = Monster("Les impôts", "air", 400, 150, 60, 600)

# ---- class player
Player = Player("Bob",5000, 50, 50, 1000, [Spell_boule_feu.name, Spell_kawaii.name, Spell_canard.name], 0, 1)
