#Codage du jeu sans atribution au widget du plateau de jeu en-dessous


import random

# Variable de base pour le jeu
longueur_combi = 4
tentas_max = 10
couleurs = ["R","V","B","O","J","M","C","G"] #Couleurs possible pour le code secret / combinaison du joueur : Rouge/Vert/Bleu/Orange/Jaune/Marron/Cyan/Gris

# Fonction qui créer le code secret aleatoirement (pour mode 1 joueur)
def creation_code_secret():
    code_secret = []
    for i in range(longueur_combi):
        couleur = random.choice(couleurs)
        code_secret.append(couleur)
    return code_secret


# Fonction qui va verifier la combinaison proposé par le joueur
def verifier_combi_du_joueur(code_secret, combi_du_joueur):
    pion_noir = 0   #couleurs présentent, mais pas bien placées
    pion_blanc = 0  #couleurs présentent, et bien placées

    for i in range(longueur_combi):
        if combi_du_joueur[i] == code_secret[i]:
            pion_blanc += 1
        elif combi_du_joueur[i] in code_secret:
            pion_noir += 1
    return pion_blanc, pion_noir
#Verification un par un des boules de la combinaison du joueur, qui va génerer des pions blancs ou noirs en fonction de la validité de la position ou de la couleur dans le code secret



# Lancement de la partie 
def Lancement_De_La_Partie():

    print("Bienvenue dans le jeu Mastermind!")

    code_secret = creation_code_secret()
    nombre_tentas = 0

    while nombre_tentas < tentas_max:
        print(f"\nTentative {nombre_tentas + 1}/10: ")
        combi_proposé = list(input().upper())
        if len(combi_proposé) != longueur_combi or not all(couleur in couleurs for couleur in combi_proposé): 
#Verification 1er verif: si la combi proposé par le joueur est bien de la meme longueur que le code_secret, 2eme verif: si les couleurs, choisit par le joueur sont bien dans la liste couleur        
            print(f"Veuillez entrer une combinaison de {longueur_combi} couleurs parmi {couleurs}")
            continue
#Si, ces deux conditions ne sont pas réspectés, alors on redemande au joueur une nouvelle combinaison qui respecte les verifications de au-dessus

        pion_blanc,pion_noir=verifier_combi_du_joueur(code_secret, combi_proposé)
        
        print(f"Nombre de pions noir : {pion_noir}")
        print(f"Nombre de pions blanc : {pion_blanc}")
        

        if pion_blanc == longueur_combi:
            print("Félicitations! Vous avez trouvé le code secret.")
            return
        
        nombre_tentas += 1
    print(f"Vous avez épuisé vos 10 tentatives. Le code secret était {code_secret}.")

Lancement_De_La_Partie()

