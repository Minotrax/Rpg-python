from Class_RPG import *
from random import randint
from time import sleep
from sys import exit
import colorama
from colorama import Fore
from colorama import Style
from Sauvegarde_RPG import *


colorama.init()
killed_monster = []

def menu():
    print("_________________________")
    print("|  [1] Nouvelle Partie   | \n|  [2] Continuer         | \n|  [3] Option            | \n|  [4] Quitter           |")
    print("_________________________")
    choice_menu = int(input(": "))
    if choice_menu == 1:
        print("Nouvelle partie.")
        sleep(1)
        print(Fore.BLUE + Style.BRIGHT + "Bienvenue sur < RPGETIC > jeune apprenti, c'est la voix qui te parle dans t'as tête." + Style.RESET_ALL)
        sleep(2)
        print(Fore.BLUE + Style.BRIGHT + "\nDans ce monde étrange qu'est RPGETIC. Des monstres contrôlent les environs qui sont manipuler par un terrible monstre inconnu dans son donjon. " + Style.RESET_ALL)
        sleep(3)
        print(Fore.BLUE + Style.BRIGHT + "\nIl faut agir ! Et c'est toi qui va ten chargé, parceque j'ai la flemme." + Style.RESET_ALL)
        sleep(2)
        print(Fore.BLUE + Style.BRIGHT + "\nTu es acctuellement dans la foret d'RPGETIC et c'est ici que commence ton périple !" + Style.RESET_ALL)
        sleep(2)
        print(Fore.BLUE + Style.BRIGHT + "\nRentre les touches [Z] [Q] [S] [D] et appuie sur ENTRER pour te déplacer dans la carte." + Style.RESET_ALL)
        sleep(2)
    elif choice_menu == 2:
        load()
    elif choice_menu == 3:
        def menu2():
            print("___________________")
            print("|  [1] Commandes   | \n|  [2] Crédits     | \n|  [3] Sortir      |")
            print("___________________")
            choice_menu2 = int(input(" : "))
            if choice_menu2 == 1:
                print("Pour se déplacer : [Z] [Q] [S] [D]. \nVous pouvez faire des combats avec des armes que vous équipez. \nVous pouvez aussi attaquer avec des sorts qui ont des dégats magiques. \nVous pouvez utiliser les potions aussi de différentes puissance, faible moyenne et forte, de vie mana ou force.")
                menu2()
            if choice_menu2 == 2:
                print("- MALET Augustin\n- HA Adrien\n- GODART Robin\n- MOHALI Joeil ")
                menu2()
            if choice_menu2 == 3:
                return menu()
        menu2()  
    elif choice_menu == 4:
        print("A dieu")
        exit()
menu()

        
def Weapons():
    print("Votre inventaire des armes :", Player.inventory[1])
    choice_weapon = str(input("\nEntrer le nom de l'arme que vous voulez équiper : "))
    choice_weapon = choice_weapon.lower()
    if choice_weapon not in Player.inventory[1]:
        print("\ncette arme n'est pas dans votre inventaire réessayer\n")
        Weapons()

    else:
        if choice_weapon == "une épée":
            print("Vous avez équipé l'épée !")
            sleep(1)
            return Sword
        elif choice_weapon == "un arc":
            print("Vous avez équipé l'arc !")
            sleep(1)
            return bow
        elif choice_weapon == "une baguette magique":
            print("Vous avez équipé la baguette magique !")
            sleep(1)
            return magic_wand
    
def Potions():                                               
        choice_potions = input("\npotions :\n1 - Vie \n2 - Force \n3 - Mana \nVotre choix : ")
        # potion de vie
        if choice_potions == "1":
            if "Potion faible de vie" in Player.inventory[0] or "Potion moyenne de vie" in Player.inventory[0] or "Potion forte de vie" in Player.inventory[0]:
                choice_power = int(input("Voulez-vous une potion de soin : \n1/ Faible \n2/ Moyenne \n3/ Forte \nVotre choix :"))
                if choice_power == 1:
                    if "Potion faible de vie" in Player.inventory[0]:
                            Player.inventory[0].remove("Potion faible de vie")
                            Potion = low_health_potion
                    else:
                        print("Vous n'en avez plus dans l'inventaire !\n")
                        return
                elif choice_power == 2:
                    if "Potion moyenne de vie" in Player.inventory[0]:
                            Player.inventory[0].remove("Potion moyenne de vie")
                            Potion = medium_health_potion
                    else:
                        print("Vous n'en avez plus dans l'inventaire !\n")
                        return
                elif choice_power == 3:
                    if "Potion forte de vie" in Player.inventory[0]:
                            Player.inventory[0].remove("Potion forte de vie")
                            Potion = strong_health_potion
                    else:
                        print("Vous n'en avez plus dans l'inventaire !\n")
                        return
                
                Player.health = Player.health + Potion.power
                print("\nEffet ajouté ! +", Potion.power, "PDV. Vous avez maintenant", Player.health, "points de vie !\n")
            else:
                print("Vous n'en avez plus dans l'inventaire !\n")
                return
        
        # potion de force
        elif choice_potions == "2":
            if "Potion faible de force" in Player.inventory[0] or "Potion moyenne de force" in Player.inventory[0] or "Potion forte de force" in Player.inventory[0]:
                choice_power = int(input("Voulez-vous une potion de force : \n1/ Faible \n2/ Moyenne \n3/ Forte \nVotre choix :"))
                if choice_power == 1:
                    if "Potion faible de force" in Player.inventory[0]:
                            Player.inventory[0].remove("Potion faible de force")
                            Potion = low_strength_potion
                    else:
                        print("Vous n'en avez plus dans l'inventaire !\n")
                        return
                elif choice_power == 2:
                    if "Potion moyenne de force" in Player.inventory[0]:
                            Player.inventory[0].remove("Potion moyenne de force")
                            Potion = medium_strength_potion
                    else:
                        print("Vous n'en avez plus dans l'inventaire !\n")
                        return
                elif choice_power == 3:
                    if "Potion forte de force" in Player.inventory[0]:
                            Player.inventory[0].remove("Potion forte de force")
                            Potion = strong_strength_potion
                    else:
                        print("Vous n'en avez plus dans l'inventaire !\n")
                        return       
                    
                Player.strength = Player.strength + Potion.power
                print("\nEffet ajouté ! +", Potion.power, "force. Vous avez maintenant", Player.strength, "points de force !")
            else:
                print("Vous n'en avez plus dans l'inventaire !\n")
                return
        # potion de mana
        elif choice_potions == "3":
            if "Potion faible de mana" in Player.inventory[0] or "Potion moyenne de mana" in Player.inventory[0] or "Potion forte de mana" in Player.inventory[0]:
                choice_power = int(input("Voulez-vous une potion de mana : \n1/ Faible \n2/ Moyenne \n3/ Forte \nVotre choix :"))
                if choice_power == 1:
                    if "Potion faible de mana" in Player.inventory[0]:
                            Player.inventory[0].remove("Potion faible de mana")
                            Potion = low_mana_potion
                    else:
                        print("Vous n'en avez plus dans l'inventaire !\n")
                        return
                elif choice_power == 2:
                    if "Potion moyenne de mana" in Player.inventory[0]:
                            Player.inventory[0].remove("Potion moyenne de mana")
                            Potion = medium_mana_potion
                    else:
                        print("Vous n'en avez plus dans l'inventaire !\n")
                        return
                elif choice_power == 3:
                    if "Potion forte de mana" in Player.inventory[0]:
                            Player.inventory[0].remove("Potion forte de mana")
                            Potion = strong_mana_potion
                    else:
                        print("Vous n'en avez plus dans l'inventaire !\n")
                        return
                Player.mana = Player.mana + Potion.power
                print("\nEffet ajouté ! +", Potion.power, "mana. Vous avez maintenant", Player.mana, "points de mana !")
            else:
                print("Vous n'en avez plus dans l'inventaire !")
                return
        else:
            print("\nVous n'avez rien dans l'inventaire !\n")
            return

            

        
def system_attack(monster):
    Weapon = None
    print("\n --- Vous rentrez dans le mode combat ! ---\n")
    if monster.name == "Gros nounours":
        print(Fore.BLUE + Style.BRIGHT + "Tu te retrouve ici dans le système de combat. Ici tu peux choisir d'attaquer avec ton arme, ou d'attaquer avec tes sorts." + Style.RESET_ALL)
        sleep(2)
        print(Fore.BLUE + Style.BRIGHT + "\nTu peux également ouvrir ton inventaire pour équiper une arme ou utiliser une potion." + Style.RESET_ALL)
        sleep(2)
        print(Fore.BLUE + Style.BRIGHT + "\nT'as force augmente tes dégats physique, c'est à dire une attaque avec ton arme, elle n'a pas d'effet sur les attaques avec des sorts.\nTu retrouves ici tes stats avec tes points de vie en haut, t'as force et ton mana. Et celle du monstre en face" + Style.RESET_ALL)
    while monster.health > 0 and Player.health > 0:  #tant que 1 des 2 n'est pas mort on continue
        tour = False     #Système de tour par tour avec true/false 
        print("Vos stats :                               Stats du monstre :\n \---", Player.health,"PDV ---/                               \---",monster.health," PDV---/\n \---", Player.strength, "Force ---/                               \---", monster.attack,"Force---/\n \---", Player.mana, "mana ---/\n")
        sleep(1)
        if tour == False:
            choice = int(input("1 - Attaquer avec mon arme \n2 - Ouvrir la liste des compétences \n3 - Ouvrir l'inventaire \nVotre choix : "))
            if choice == 1:
                if Weapon != None:
                    monster.health -= Weapon.damage + Player.strength
                    print("Vous avez attaqué avec", Weapon.name) 
                    print(Fore.RED + "le monstre perd", Weapon.damage + Player.strength, "PDV !\n" + Style.RESET_ALL)
                    sleep(1)
                else:
                    print("\nIl vous faut une arme !\n")
                    sleep(1)
            elif choice == 2:
                print("\nVos sort : ", Player.spells)
                choice_spells = input("Quel sort voulez vous lancer ?\nVotre choix : ")
                if choice_spells == "1":
                    Spell = Spell_boule_feu
                elif choice_spells == "2":
                    Spell = Spell_kawaii
                elif choice_spells == "3":
                    Spell = Spell_canard
                if Player.mana > Spell.mana:
                    Player.mana = Player.get_mana(Spell.mana)
                    monster.health = Spell.damage(monster.health)
                    sleep(1)
                    print("Il reste", monster.health, "à", monster.name)
                    sleep(1)
                else:
                    print("Vous n'avez plus assez de mana !")
                    sleep(1)
                tour = True
                    
                    
            elif choice == 3:
                print("\nVotre inventaire :", Player.inventory) 
                choice_inventory = input("\nque voulez vous utiliser dans l'inventaire ? \n1 - potions \n2 - weapons \n3 - sortir \n : ")
                if choice_inventory == "1":
                    Potions()    
                elif choice_inventory == "2":
                    Weapon = Weapons()
                    
            if tour == True and monster.health > 0:
                Player.health -= monster.attack
                print(Fore.RED + "\nLe monstre attaque ! vous avez perdu",monster.attack,"pdv" + Style.RESET_ALL)
                print("\nIl vous reste",Player.health,"pdv\n")
                sleep(1)
                tour = False
            
            if monster.health <= 0:
              killed_monster.append(monster.name)
              if monster.name =="Gros nounours":
                  print("")
                  print(Fore.BLUE + Style.BRIGHT + "Bravo tu as réussi maintenant il va falloir que tu rentres dans une grotte, un monstre garde la clef qui permet d'accéder au donjon." + Style.RESET_ALL)
                  sleep(2)
                  print("")
                  print(Fore.BLUE + Style.BRIGHT + "Mais attention ! Si trouves par hasard le donjon n'entre surtout pas dedans, tu pourais clamssé." + Style.RESET_ALL)
                  sleep(2)
              if monster.name == "Loic":
                  print("\nVous avez drop la clef du donjon ! Vous pouvez maintenant rentrer dans la dernière salle du donjon.\n")
                  sleep(2)
                  print(Fore.BLUE + Style.BRIGHT + "Tu es maintenant pret à réalisé ton destin jeune apprenti poilu. Le sort de ce monde dépend de toi." + Style.RESET_ALL)
                  sleep(2)
                  print("")
                  print(Fore.BLUE + Style.BRIGHT + "Tu dois trouver le monstre qui rôde dans le donjon et ouvrir sa porte pour l'anéantir." + Style.RESET_ALL)
                  sleep(2)
                  print("")
                  print(Fore.BLUE + Style.BRIGHT + "Bonne chance à toi jeune apprenti !" + Style.RESET_ALL)
                  print("")
                  print(Fore.BLUE + Style.BRIGHT + "Mais avant il faudrait sortir de cette grotte.\n Il n'y a qu'une seul sortie c'est l'entrée." + Style.RESET_ALL)

              elif monster.name == "Les impôts":
                  print("")
                  print(Fore.BLUE + Style.BRIGHT + "Sacre bleu ! Tu as réussi le monde de RPGETIC peut vivre en paix maintenant !\nEt tout ça grâce à toi mon apprenti poilu !" + Style.RESET_ALL)
                  sleep(3)
                  print("\n\n*** VOUS AVEZ GAGNE ET FINI LE JEU ! ***\n")
                  print("\nLes dev : Augustin, Adrien, Robin, Joeil \nMerci d'avoir joué.")
                  exit()
              Player.xp += monster.xp
              print("Vous avez gagné le combat contre",monster.name," !")
              print("")
              print(Fore.YELLOW + " Vous avez gagné",monster.xp,"XP" + Style.RESET_ALL)
              sleep(1)
              drop_potions = randint(0, 1)
              drop_weapons = randint(0, 1)

              if drop_potions == 1:
                drop_alea_pot = randint(1, 100)
                if drop_alea_pot <= 60:
                    drop_low = randint(1, 3)
                    if drop_low == 1:
                        Player.inventory[0].append("Potion faible de vie")
                        print(Fore.GREEN + "\nvous avez drop une petite potion de vie !" + Style.RESET_ALL)
                    if drop_low == 2:
                        Player.inventory[0].append("Potion faible de mana")
                        print(Fore.GREEN + "\nvous avez drop une petite potion de mana !" + Style.RESET_ALL)
                    if drop_low == 3:
                        Player.inventory[0].append("Potion faible de force")
                        print(Fore.GREEN + "\nvous avez drop une petite potion de force !" + Style.RESET_ALL)
                elif drop_alea_pot <= 90:
                        drop_medium = randint(1, 3)
                        if drop_medium == 1:
                            Player.inventory[0].append("Potion moyenne de vie")
                            print(Fore.GREEN + "\nvous avez drop une moyenne potion de vie !" + Style.RESET_ALL)      
                        if drop_medium == 2:
                            Player.inventory[0].append("Potion moyenne de mana")
                            print(Fore.GREEN + "\nvous avez drop une moyenne potion de mana !" + Style.RESET_ALL) 
                        if drop_medium == 3:
                            Player.inventory[0].append("Potion moyenne de force")
                            print(Fore.GREEN + "\nvous avez drop une moyenne potion de force !" + Style.RESET_ALL) 
                else:
                    drop_large = randint(1, 3)
                    if drop_large == 1:
                        Player.inventory[0].append("Potion forte de vie")
                        print(Fore.GREEN + "\nvous avez drop une forte potion de vie !" + Style.RESET_ALL)       
                    if drop_large == 2:
                        Player.inventory[0].append("Potion forte de mana")
                        print(Fore.GREEN + "\nvous avez drop une forte potion de mana !" + Style.RESET_ALL)
                    if drop_large == 3:
                        Player.inventory[0].append("Potion forte de force")
                        print(Fore.GREEN + "\nvous avez drop une forte potion de force !" + Style.RESET_ALL)
              if drop_weapons == 1:
                    drop_alea_weapon = randint(1, 40)
                    if drop_alea_weapon <= 10:
                        drop_between = randint(1, 3)
                        if drop_between == 1:
                            Player.inventory[1].append(Sword.name)
                            print(Fore.GREEN + "\nVous avez drop une épée !" + Style.RESET_ALL)
                        if drop_between == 2:
                            Player.inventory[1].append(bow.name)
                            print(Fore.GREEN + "\nvous avez drop un Arc !" + Style.RESET_ALL)
                        if drop_between == 3:
                            Player.inventory[1].append(magic_wand.name)
                            print(Fore.GREEN + "\nvous avez drop un baton magique !" + Style.RESET_ALL)
              
              else:
                  if drop_potions == 0 and drop_weapons == 0:
                      print(Fore.GREEN + "Le monstre n'a rien drop !" + Style.RESET_ALL)
                      
                  
              print("\nVoici votre équipement maintenant :", Player.inventory)
              xp_player()

def xp_player():
    xp_max = 150
    if Player.xp >= xp_max:
        Player.level += 1
        print(Fore.YELLOW + "\nVous venez de gagner un niveau !\nVous êtes maintenant niveau :", Player.level, "\n" + Style.RESET_ALL)
        Player.xp = 0
        xp_max += 200
        if Player.level == 4:
            print(Fore.YELLOW + "\nGrace à votre niveau", Player.level, ":\n" + Style.RESET_ALL)
            print(Fore.GREEN + "vous avez drop un baton magique !\n" + Style.RESET_ALL)
            Player.inventory[1].append(magic_wand.name)
            print("Votre équipement : ", Player.inventory)
    
                
              
              



map1 = [[],[],[],
       [],[],[],
       [],[],[]]

map2 = [[],[],[],
        [],[],[],
        [],[],[]]

map3 = [[],[],[],
        [],[],[],
        [],[],[]]


def print_map1():
    print(map1[0], map1[1], map1[2],'\n', map1[3], map1[4], map1[5],'\n', map1[6], map1[7], map1[8],'\n')
def print_map2():
    print(map2[0], map2[1], map2[2],'\n', map2[3], map2[4], map2[5],'\n', map2[6], map2[7], map2[8],'\n')
def print_map3():
    print(map3[0], map3[1], map3[2],'\n', map3[3], map3[4], map3[5],'\n', map3[6], map3[7], map3[8],'\n')
       
player_print = "옷"
pos = 4
map1[pos].append(player_print)
print_map1()

First_time = True

def where(player_print):
    if player_print in map1[pos]:
        return map1[pos]
    elif player_print in map1[pos]:
        return map1[pos]
    elif player_print in map1[pos]:
        return map1[pos]

while player_print in map1[pos]:
  
  move = input("[Z] [Q] [S] [D] : ")
  
  if move == "save":
      print("Vous avez sauvegardé")
      save()
  if move == "ou":
      if player_print in map1[pos]:
          print("vous etes dans la map 1 à la position", pos)
      elif player_print in map2[pos]:
          print("vous etes dans la map 2 à la position", pos)
      elif player_print in map3[pos]:
          print("vous etes dans la map 3 à la position", pos)
      
  if move == "z":
      if player_print in map1[1] or map1[0] or map1[2]:
          print("Bim dans le mur là !")
          print_map1()
      else:
          if First_time == True:
              map1[pos].remove(player_print)
              map1[pos-3].append(player_print)
              pos = pos -3
              print_map1()
              First_time = False
              print(Fore.BLUE + Style.BRIGHT + "Super ! Maintenant, trouve le gros nounours en haut à droite pour faire ton premier combat !" + Style.RESET_ALL)
              sleep(2)
              print_map1()
          else:
              map1[pos].remove(player_print)
              map1[pos-3].append(player_print)
              pos = pos -3
              print_map1()
             
  if move == "s":
      if player_print in map1[6] or map1[7] or map1[8]:
          print("Bim dans le mur là !")
          print_map1()
      else:
          if First_time == True:
              map1[pos].remove(player_print)  
              map1[pos+3].append(player_print)
              pos = pos + 3
              print_map1()
              First_time = False
              print(Fore.BLUE + Style.BRIGHT + "Super ! Maintenant, trouve le gros nounours en haut à droite pour faire ton premier combat !" + Style.RESET_ALL)
              sleep(2)
              print_map1()
          else:
              map1[pos].remove(player_print)  
              map1[pos+3].append(player_print)
              pos = pos + 3
              print_map1()
  if move == "d":
      if player_print in map1[5] or map1[2] or map1[8]:
          print("Bim dans le mur là !")
          print_map1()
      else:
          if First_time == True:
              map1[pos].remove(player_print)    
              map1[pos+1].append(player_print)
              pos = pos + 1
              print_map1()
              First_time = False
              print(Fore.BLUE + Style.BRIGHT + "Super ! Maintenant, trouve le gros nounours en haut à droite pour faire ton premier combat !" + Style.RESET_ALL)
              sleep(2)
              print_map1()
          else:
              map1[pos].remove(player_print)    
              map1[pos+1].append(player_print)
              pos = pos + 1
              print_map1()
  if move == "q":
          if player_print in map1[0] or map1[3] or map1[6]:
              print("Bim dans le mur là !")
              print_map1()
          else:
              if First_time == True:
                  map1[pos].remove(player_print)    
                  map1[pos-1].append(player_print)
                  pos = pos - 1
                  print_map1()
                  First_time = False
                  print(Fore.BLUE + Style.BRIGHT + "Super ! Maintenant, trouve le gros nounours en haut à droite pour faire ton premier combat !" + Style.RESET_ALL)
                  sleep(2)
                  print_map1()
              else:
                  map1[pos].remove(player_print)    
                  map1[pos-1].append(player_print)
                  pos = pos - 1
                  print_map1()
  if player_print in map1[2] and Gros_nounours.name not in killed_monster:
    choice_fight_Gros_nounours = input("Attaquer le gros nounours ? \n 1 - Oui \n 2 - Non \n : ")
    if choice_fight_Gros_nounours == "1":
       system_attack(Gros_nounours)
    elif choice_fight_Gros_nounours == "2":
          print("vous avez fuiiiiiiiiiiiiiiiiis ^^' ")
          print_map1()
      
  if player_print in map1[8] and Brontis.name not in killed_monster and Player.level == 3:
    choice_fight_Brontis = input("Attaquer Brontis le tueur ? \n 1 - Oui \n 2 - Non \n : ")
    if choice_fight_Brontis == "1":
       system_attack(Brontis)
    elif choice_fight_Brontis == "2":
          print("vous avez fuiiiiiiiiiiiiiiiiis ^^' ")
          print_map1()
  if player_print in map1[8] and Brontis.name not in killed_monster and Player.level <= 2:
      print(Fore.BLUE + Style.BRIGHT + "Brontis le tueur sécurise la porte du donjon, malheureusement ton niveau actuel est trop bas pour l'affronter.\nSois sage et reviens plus tard jeune apprenti." + Style.RESET_ALL)
      sleep(2)
      print_map1()
  if player_print in map1[8] and Player.level == 4:
      print(Fore.BLUE + Style.BRIGHT + "Super ! Brontis le teur sécurisait l'entrée du donjon. Maintenant qu'il est mit KO first round, tu peux rentrer dans le donjon !" + Style.RESET_ALL)
      sleep(3)
      choice = input("Entrer dans le donjon ? \n1 - Oui \n2 - Non \nVotre choix: ")
      choice.lower()
      if choice == "1":
          map1[pos].remove(player_print)  
          map2[0].append(player_print)
          pos = 0
          print("vous etes dans le donjon !")
          sleep(1)
          print("")
          print(Fore.BLUE + Style.BRIGHT + "Trouve la porte vérouillée du donjon, et accomplie ton Destin fils. he non... pardon jeune apprenti !" + Style.RESET_ALL)
          sleep(1)
          print_map2()
          while player_print in map2[pos]:
              move = input("nord/sud/est/west : ")
              if move == "ou":
                  if player_print in map1[pos]:
                      print("vous etes dans la map 1 à la position", pos)
                  elif player_print in map2[pos]:
                      print("vous etes dans la map 2 à la position", pos)
                  elif player_print in map3[pos]:
                      print("vous etes dans la map 3 à la position", pos)
            
              if move == "z":
                  if player_print in map2[0] or map2[1] or map2[2] or map2[3] or map2[8]:
                      print("[Z] [Q] [S] [D] : ")
                      print_map2()
                  else:    
                      map2[pos].remove(player_print)
                      map2[pos-3].append(player_print)
                      pos = pos -3
                      print_map2()
              if move == "s":
                  if player_print in map2[0] or map2[5] or map2[6] or map2[7] or map2[8]:
                      print("Bim dans le mur là !")
                      print_map2()
                  else:
                      map2[pos].remove(player_print)  
                      map2[pos+3].append(player_print)
                      pos = pos + 3
                      print_map2()
              if move == "d":
                  if player_print in map2[2] or map2[3] or map2[4] or map2[5] or map2[8]:
                      print("Bim dans le mur là !")
                      print_map2()
                  else:
                      map2[pos].remove(player_print)    
                      map2[pos+1].append(player_print)
                      pos = pos + 1
                      print_map2()
              if move == "q":
                  if player_print in map2[0] or map2[3] or map2[4] or map2[5] or map2[6]:
                    print("Bim dans le mur là !")
                    print_map2()
                  else:
                      if player_print in map2[7] and Loic.name not in killed_monster:
                          print("La porte est verrouillée")
                      elif player_print in map2[7] and Loic.name in killed_monster:
                          print("la porte s'ouvre !")
                          sleep(1)
                          print("")
                          print(Fore.BLUE + Style.BRIGHT + "C'est maintenant ou jamais mon poilu ! Tue le BOSS finale ! Et puis après on joue à la console." + Style.RESET_ALL)
                      map2[pos].remove(player_print)    
                      map2[pos-1].append(player_print)
                      pos = pos - 1
                      print_map2()

              if player_print in map2[3] and Les_impots.name not in killed_monster:
                  choice_fight_Les_impots = input("Attaquer les impots en justice ? [BOSS FINALE] \n 1 - Oui \n 2 - Non \n : ")
                  if choice_fight_Les_impots == "1":
                     system_attack(Les_impots)
                  elif choice_fight_Les_impots == "2":
                          print("Vous avez fuis le combat.")
                          print_map2()


  if player_print in map1[0]:
    choice = input("Entrer dans la grotte ? \n1 - Oui \n2 - Non \nVotre choix : ")
    choice.lower()
    if choice == "1":
      map1[0].remove(player_print)  
      map3[0].append(player_print)
      pos = 0
      first_time_grotte = True
      print("vous etes dans grotte !")
      sleep(1)
      print("")
      print("Attention il y a des murs invisibles il faudra les évites")
      sleep(1)
      print_map3()
      first_time_grotte = True
      while player_print in map3[pos]:
          move = input("[Z] [Q] [S] [D] : ")
          if move == "ou":
              if player_print in map1[pos]:
                  print("vous etes dans la map 1 à la position", pos)
              elif player_print in map2[pos]:
                  print("vous etes dans la map 2 à la position", pos)
              elif player_print in map3[pos]:
                  print("vous etes dans la map 3 à la position", pos)
          if move == "z":
              if player_print in map3[0] or map3[1] or map3[2] or map3[5]:
                  print("Bim dans le mur là !")
                  print_map3()
              else:    
                  map3[pos].remove(player_print)
                  map3[pos-3].append(player_print)
                  pos = pos -3
                  print_map3()
          if move == "s":
              first_time_grotte = False
              if player_print in map3[2] or map3[6] or map3[7] or map3[8]:
                  print("Bim dans le mur là !")
                  print_map3()
              else:
                  map3[pos].remove(player_print)  
                  map3[pos+3].append(player_print)
                  pos = pos + 3
                  print_map3()
          if move == "d":
              if player_print in map3[0] or map3[2] or map3[3] or map3[5] or map3[8]:
                  print("Bim dans le mur là !")
                  print_map3()
              else:
                  map3[pos].remove(player_print)    
                  map3[pos+1].append(player_print)
                  pos = pos + 1
                  print_map3()
          if move == "q":
              if player_print in map3[0] or map3[1] or map3[3] or map3[4] or map3[6]:
                  print("Bim dans le mur là !")
                  print_map3()
              else:
                  map3[pos].remove(player_print)    
                  map3[pos-1].append(player_print)
                  pos = pos - 1
                  print_map3()   
          if player_print in map3[2] and Loic.name not in killed_monster:
            choice_fight_Loic = input("Attaquer Loic au cheuveux long ? \n 1 - Oui \n 2 - Non \n : ")
            if choice_fight_Loic == "1":
               system_attack(Loic)
            elif choice_fight_Loic == "2":
                print("vous avez fuiiiiiiiiiiiiiiiiis ^^' ")
                print_map3()
          elif player_print in map3[0] and first_time_grotte == False:
              choice = int(input("Voulez-vous sortir de la grotte ? \n1 - Oui \n2 - Non \nVotre choix : "))
              if choice == 1:
                print("Vous etes de retour dans la foret.")
                sleep(1)
                map1[0].append(player_print)  
                map3[0].remove(player_print)
                print_map1()
