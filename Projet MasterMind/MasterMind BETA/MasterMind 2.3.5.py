import tkinter as tk
from tkinter import*
from random import randint
import random

# Création de la fenêtre des règles du MasterMind
fenetre_regle= tk.Tk()
fenetre_regle.title("Mastermind")
fenetre_regle.geometry("1000x550")
fenetre_regle.resizable(height=False,width=False)

text_title = tk.Label(fenetre_regle,text = '✨ Les règles du MasterMind ✨', font=("Calibri",20),fg = 'red',)
text_title.pack()

cadre1 = tk.Frame(bg='black', bd='3',relief="sunken") #Le cadre
text_subtitle1 = tk.Label(cadre1, font=("Arial",13),fg = 'black',bg = 'white', justify="left",text = "\nLe MasterMind est un jeu à 2 joueurs dans lequel le Master choisit un code secret formé de 4 pions de couleur alignés et \nle joueur doit deviner ce code avec au maximum 10 essais de code.\n\nUn essai consiste à proposer un code et à le comparer au code secret. Huit couleurs sont disponibles dans le jeu et plusieurs\npions du code peuvent être de la même couleur. À chaque essai, le joueur qui décode peut obtenir les informations suivantes:\n\n    - Le nombre de pions bien placés (mais il ne sait pas lesquels), un pion est bien placé s’il a la même couleur que le pion qui\n      est à la même position dans le code secret.\n    - Le nombre de pions mal placés; un pion est mal placé s’il a la même couleur qu’un pion du code secret qui n’est pas à une\n      position d’un pion bien placé. De plus chaque pion du code secret peut compter pour au plus un pion mal placé.\n\nVous pouvez retrouver ces informations grâce aux pions sur le côté. Les pions blancs représentent les pions bien placés et\nles pions noirs représentent les pions mals placés.\nSi le joueur qui décode trouve le code secret en moins de 10 essais alors il gagne, sinon c'est le Master qui gagne.\n\nIl existe deux modes de notre MasterMind:\n\n    - Mode 1 joueur: Un code secret est choisi aléatoirement et c'est à vous de la décoder.\n    - Mode 2 joueurs: Un joueur sera le Master qui choisira le code secret et l'autre joueur sera le Décodeur, celui qui devra essayer\nde décoder le code secret. C'est plus drôle de jouer à deux👍\n")
text_subtitle1.pack()
cadre1.pack()

un_joueur = tk.Button(fenetre_regle,height = 1,width =16 ,font=("Calibri",13),text="Mode 1 joueur",fg='black', activebackground='white', command=fenetre_regle.destroy)
un_joueur.pack()

deux_joueur = tk.Button(fenetre_regle,height = 1,width =16 ,font=("Calibri",13),text="Mode 2 joueurs",fg='black', activebackground='white', command=fenetre_regle.destroy)
deux_joueur.pack()

fenetre_regle.mainloop()

couleurs=["Red","Blue","Green","Cyan","Purple","Yellow","Pink","Orange"]
ligne = 0
nb_couleur=len(couleurs)

#Ensemble de fonction qui permet d'avoir des couleurs aléatoire
#Fonctions qui viennent du deuxième TD d'info
def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def coul_alé():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    couleur = get_color(r,g,b)
    return couleur

#Fonction des Boutons
def quitter():
    fenetre.destroy()

def color(canvas):
    tableau_canvas[ligne//nb_couleur][canvas].itemconfig(boule, fill=couleurs[liste_proposition[ligne//nb_couleur][canvas]%nb_couleur])
    
# Lorsque on clique sur un boutton ça modifie la liste "liste_proposition" avec le numéro de couleur correspondant pour la colonne associée
def clicked1(event):
    liste_proposition[ligne//nb_couleur][0] += 1

def clicked2(event):
    liste_proposition[ligne//nb_couleur][1] += 1

def clicked3(event):
    liste_proposition[ligne//nb_couleur][2] += 1

def clicked4(event):
    liste_proposition[ligne//nb_couleur][3] += 1

def validate():
    global ligne
    pion_blanc = 0
    pion_noir = 0
    combinaison_copy = code_secret.copy()

    for i in range(len(code_secret)):
        #  correspond à la ligne dans la list/permet de prendre une colonne comprise entre 1 et 4 grace au %
        if liste_proposition[ligne//nb_couleur][i]%nb_couleur+1 == code_secret[i]:
            pion_blanc+=1 
    
    for i in range(len(code_secret)):
        if liste_proposition[ligne//nb_couleur][i]%nb_couleur+1 in combinaison_copy:
            combinaison_copy.remove(liste_proposition[ligne//nb_couleur][i]%nb_couleur+1)
            pion_noir +=1

    tableau_label[ligne//nb_couleur].config(text = "⚪ " + str(pion_blanc)  + '\n' + "⚫ " + str(pion_noir-pion_blanc))
    ligne+=nb_couleur
    
    # C'est gagné
    if pion_blanc == 4:
        Gg_perdu = tk.Tk()
        Gg_perdu.title("Tu as gagné !")
        canvasgg_perdu = tk.Canvas(Gg_perdu, width=400, height=200)
        canvasgg_perdu.pack()
        canvasgg_perdu.create_oval(100, 50, 300, 150, fill='yellow', width=3)
        canvasgg_perdu.create_oval(130, 75, 160, 90, fill='black')
        canvasgg_perdu.create_oval(240, 75, 270, 90, fill='black')
        canvasgg_perdu.create_arc(140, 65, 260, 140, start=0, extent=-180, width=3)  
        Gg_perdu.mainloop()

    # C'est perdu   
    if ligne == nb_ligne*nb_couleur and pion_blanc != 4:
        Gg_perdu = tk.Tk()
        Gg_perdu.title("Tu as Perdu !")
        canvasgg_perdu = tk.Canvas(Gg_perdu, width=400, height=200)
        canvasgg_perdu.pack()
        canvasgg_perdu.create_oval(100, 50, 300, 150, fill='red', width=3)
        canvasgg_perdu.create_oval(130, 75, 160, 90, fill='black')
        canvasgg_perdu.create_oval(240, 75, 270, 90, fill='black')
        canvasgg_perdu.create_arc(140, 100, 260, 160, start=0, extent=180, width=3)
        Gg_perdu.mainloop()
        
# fenetre du Mastermind
fenetre = tk.Tk()
fenetre.title("✨Mastermind✨")
fenetre.config(bg="lightgrey")
fenetre.resizable(height = False, width = False)
fenetre.geometry("600x750")

# création des canevas et des tableaux
liste_proposition=[]
tableau_canvas = []
tableau_label = []
code_secret = []
taille_code=4
nb_ligne=10

#On créer le code secret en liste de chiffre
code_secret = [randint(1, nb_couleur) for g in range(taille_code)]

#On créer une liste nul ([0,0,0,0]) pour chaque ligne 
liste_proposition = [[0-1 for f in range(taille_code)] for i in range(nb_ligne)]

#On créer une grille de canvas qu'on ajoute dans une liste, qui va être une liste de widget
tableau_canvas = [[tk.Canvas(fenetre, width=45, height=45, bg="lightgrey") for i in range(taille_code)] for j in range(nb_ligne)]
for j in range(nb_ligne):
    for i in range(taille_code):
        tableau_canvas[j][i].grid(row=j+1, column=i+2)

#ici on met dans chaque canvas créé précedement une boule blanche
for j in range(nb_ligne):
    for i in range(taille_code):
        boule = tableau_canvas[j][i].create_oval(10, 10, 40, 40, fill="white")
        
#ici on créer des zone de texte à chaque ligne pour y écrire le nombre de pions blanc et noir
for i in range(0,nb_ligne+1):
    lab_ga=tk.Label(fenetre,text="",bg="lightgrey")
    lab_ga.grid(column=6,row=i+1)
    tableau_label.append(lab_ga)

#Ici on créer la liste de couleur disponible
for i in range(0,nb_couleur):
    les_couleurs = tk.Canvas(fenetre,width=45, height=45, bg="lightgrey")
    les_couleurs.create_oval(10, 10, 40, 40, fill=couleurs[i])
    les_couleurs.grid(row=2+i,column = 0)

#On annote chaque ligne
for i in range(1,11):
    les_lignes = tk.Label(fenetre,text=i,bg="lightgrey")
    les_lignes.grid(row = i,column = 1 )




#
#
#Ici on créer ici l'emplacement  pour le code secret en mode 2 joueurs
def secret1(event):
    liste_secret[ligne_secret//nb_couleur][0] += 1

def secret2(event):
    liste_secret[ligne_secret//nb_couleur][1] += 1

def secret3(event):
    liste_secret[ligne_secret//nb_couleur][2] += 1

def secret4(event):
    liste_secret[ligne_secret//nb_couleur][3] += 1

def color_secret(canvas):
    tableau_secret[ligne_secret//nb_couleur][canvas].itemconfig(boule_secret, fill=couleurs[liste_secret[ligne_secret//nb_couleur][canvas]%nb_couleur])

def validate_secret():
    Bouton_1.destroy()
    Bouton_2.destroy()
    Bouton_3.destroy()
    Bouton_4.destroy()
    Bouton_val_secret.destroy()
    rectangle = tk.Canvas(fenetre,width = 5, height = 2)
    pass

liste_secret = []

tableau_secret = [[tk.Canvas(fenetre, width=45, height=45, bg="lightgrey") for i in range(taille_code)]]

#for i in range(taille_code):
    #tableau_secret.grid(row=12, column=i+5)

#for i in range(taille_code):
    #boule_secret= tableau_secret[i].create_oval(10, 10, 40, 40, fill="white")

Bouton_val_secret = tk.Button(fenetre, width=5, height=2, text="✅",bg="lightgreen", command=validate_secret,activebackground="lightgreen")
Bouton_val_secret.grid(row = 12, column= 6)

Bouton_1 = tk.Button(fenetre, width=5, height=1,command=lambda : color_secret(0))
Bouton_1.grid(row = 13, column= 2)
Bouton_1.bind("<Button-1>",secret1)

Bouton_2 = tk.Button(fenetre, width=5, height=1,command=lambda : color_secret(1))
Bouton_2.grid(row = 13, column= 3)
Bouton_2.bind("<Button-1>", secret2)

Bouton_3 = tk.Button(fenetre, width=5, height=1,command=lambda : color_secret(2))
Bouton_3.grid(row = 13, column= 4)
Bouton_3.bind("<Button-1>",secret3)

Bouton_4 = tk.Button(fenetre, width=5, height=1,command=lambda : color_secret(3))
Bouton_4.grid(row = 13, column= 5)
Bouton_4.bind("<Button-1>",secret4)


#
#





# Placement des bouttons 
Bouton_colonne_1 = tk.Button(fenetre, width=5, height=2, text="1",bg=coul_alé(),command=lambda : color(0),activebackground=coul_alé())
Bouton_colonne_1.grid(row = 0, column= 2)
Bouton_colonne_1.bind("<Button-1>",clicked1)

Bouton_colonne_2 = tk.Button(fenetre, width=5, height=2, text="2",bg=coul_alé(),command=lambda : color(1),activebackground=coul_alé())
Bouton_colonne_2.grid(row = 0, column= 3)
Bouton_colonne_2.bind("<Button-1>",clicked2)

Bouton_colonne_3 = tk.Button(fenetre, width=5, height=2, text="3",bg=coul_alé(),command=lambda : color(2),activebackground=coul_alé())
Bouton_colonne_3.grid(row = 0, column= 4)
Bouton_colonne_3.bind("<Button-1>",clicked3)

Bouton_colonne_4 = tk.Button(fenetre, width=5, height=2, text="4",bg=coul_alé(),command=lambda : color(3),activebackground=coul_alé())
Bouton_colonne_4.grid(row = 0, column= 5)
Bouton_colonne_4.bind("<Button-1>",clicked4)


Bouton_valider = tk.Button(fenetre, width=10, height=2, text="Valider",bg="lightgreen", command=validate,activebackground="lightgreen")
Bouton_valider.grid(row = 14, column= 7)

Quitter = tk.Button(fenetre, width=10, height=2, command=quitter,text="Quitter",bg="red",activebackground="red")
Quitter.grid(row = 14, column= 0)

label_combinaison=tk.Label(fenetre, text=code_secret,bg="lightgrey")
label_combinaison.grid(row=0, column=7)

Bouton_sauvegarder = tk.Button(fenetre, width=10, height=2, text = "Sauvegarder",bg="green",activebackground="green") #command
Bouton_sauvegarder.grid(row = 12, column= 0)

Bouton_charger = tk.Button(fenetre, width=10, height=2, text = "Charger",bg="lightgrey",activebackground="white")
Bouton_charger.grid(row = 13, column= 0)

fenetre.mainloop()