from Class_RPG import *
from Fonctions_RPG import *


def save(): # sauvegarde
    fichier = open("save.txt", "w")

    fichier.write(Player.name + "\n")
    fichier.write(str(Player.health) + "\n")
    fichier.write(str(Player.strength) + "\n")
    fichier.write(str(Player.mana) + "\n")
    fichier.write(str(Player.inventory) + "\n")
    fichier.write(str(Player.xp) + "\n")
    fichier.write(str(Player.level) + "\n")


def load(): # chargement de la partie (L'inventaire n'est pas chargé)
    save = open('save.txt', 'r')
    
    Liste_Player = save.readlines()
    Player_name = Liste_Player[0].strip()
    Player_health = Liste_Player[1].strip()
    Player_strength = Liste_Player[2].strip()
    Player_mana = Liste_Player[3].strip()
    Player_inventory = Liste_Player[4]
    Player_xp = Liste_Player[5].strip()
    Player_level = Liste_Player[6].strip()
    Monster_Killer = Liste_Player[7].strip()
    First_time_check = Liste_Player[8].strip()
    clef_check = Liste_Player[9].strip()
    first_time_grotte_check = Liste_Player[10].strip()
    
    
    Player.name = Player_name
    Player.health = int(Player_health)
    Player.strength = int(Player_strength)
    Player.mana = int(Player_mana)
    Player.xp = int(Player_xp)
    Player.level = int(Player_level)
    killed_monster = Monster_Killer
    First_time = First_time_check
    first_time_grotte = first_time_grotte_check

        

    save.close()
