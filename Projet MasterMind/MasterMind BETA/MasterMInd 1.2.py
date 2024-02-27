import tkinter as tk
from tkinter import*
#
# Création de la fenêtre des règles du MasterMind

fenetre_regle= tk.Tk()
fenetre_regle.title("Mastermind")
fenetre_regle.geometry("1000x550")
fenetre_regle.resizable(height=False,width=False)

text_title = tk.Label(fenetre_regle,text = '✨ Les règles du MasterMind ✨', font=("Calibri",20),fg = 'black',)
text_title.pack()

cadre1 = tk.Frame(bg='black', bd='3',relief="sunken") #Le cadre
text_subtitle1 = tk.Label(cadre1, font=("Arial",13),fg = 'black',bg = 'white', justify="left",text = "\nLe MasterMind est un jeu à 2 joueurs dans lequel le Master choisit un code secret formé de 4 pions de couleur alignés et \nle joueur doit deviner ce code avec au maximum 10 essais de code.\n\nUn essai consiste à proposer un code et à le comparer au code secret. Huit couleurs sont disponibles dans le jeu et plusieurs\npions du code peuvent être de la même couleur. À chaque essai, le joueur qui décode peut obtenir les informations suivantes:\n\n    - Le nombre de pions bien placés (mais il ne sait pas lesquels), un pion est bien placé s’il a la même couleur que le pion qui\n      est à la même position dans le code secret.\n    - Le nombre de pions mal placés; un pion est mal placé s’il a la même couleur qu’un pion du code secret qui n’est pas à une\n      position d’un pion bien placé. De plus chaque pion du code secret peut compter pour au plus un pion mal placé.\n\nVous pouvez retrouver ces informations grâce aux pions sur le côté. Les pions rouges représentent les pions bien placés et\nles pions noirs représentent les pions mals placés.\nSi le joueur qui décode trouve le code secret en moins de 10 essais alors il gagne, sinon c'est le Master qui gagne.\n\nIl existe deux modes de notre MasterMind (qui sont très similaires à un petit détail près):\n\n    - Mode 1 joueur: Le robot choisit un code secret et c'est à vous de la décoder.\n    - Mode 2 joueurs: Un joueur sera le Master qui choisira le code secret et l'autre joueur sera le Décodeur, celui qui devra essayer\nde décoder le code secret. C'est plus drôle de jouer à deux que contre un ornidateur.👍\n")
text_subtitle1.pack()
cadre1.pack()

Quitter1 = tk.Button(fenetre_regle,height = 2,width =16 ,font=("Calibri",13),text="OK j'ai compris chef",fg='black', activebackground='white', command=fenetre_regle.destroy)
Quitter1.pack()

fenetre_regle.mainloop()
#
#Création du plateau de jeu

fenetre= tk.Tk()
fenetre.title("Mastermind")
fenetre.geometry("1000x825")
fenetre.resizable(height=False,width=False)

canvas = tk.Canvas(fenetre, bg="grey",borderwidth=3,relief="groove",width=550,height=800) #Interface sur laquelle on va travailler le jeu
canvas.pack(side=LEFT)

#Paramètres de présentation
#Taille des cercles et de l'espace entre eux
ball_taille = 30
ball_espace_ligne= 10

ball_taille_couleur = 35

ball_taille_ind = 10
ball_espace_ind = 10 

#Position initiale pour dessiner les cercles de l'air de jeu
x_jeu = 50
y_jeu = 100

x_ind = 400
y_ind = 80

x_couleur = 80
y_couleur = 20

#Nombre de cercles par ligne et de lignes
nb_boule_ligne = 4
nb_ligne = 10
nb_boule_ind = 2
nb_ligne_ind = 30

#Nombre d'essaie
for i in range(nb_ligne): #parcours les lignes et les colonnes
    for j in range(nb_boule_ligne):
        x = x_jeu + j * (ball_taille + ball_espace_ligne) 
        y = y_jeu + i * (ball_taille + ball_espace_ligne)
        canvas.create_oval(x, y, x+ball_taille, y+ball_taille, fill="white",outline="black")
    y_jeu += 30

#Les couleurs
couleurs=["Red","Green","Blue","Orange","Yellow","Brown","Cyan","Pink"]

Boutons = []
for i in range(8):
    #taille de chaque bouton ChatGPT
    x1 = x_couleur + i*50  # Coordonnées x pour le coin supérieur gauche du bouton
    y1 = y_couleur # Coordonnées y pour le coin supérieur gauche du bouton
    x2 = x1 + 40   # Coordonnées x pour le coin inférieur droit du bouton
    y2 = y1 + 40   # Coordonnées y pour le coin inférieur droit du bouton
    bouton = tk.Button(canvas, bg=couleurs[i], activebackground=couleurs[i], bd=2, command=lambda event=None: None)
    bouton.place(x=x1, y=y1, width=40, height=40)
    bouton.bind("<Button-1>")
    Boutons.append(bouton)

#Les indications
for i in range(nb_ligne_ind):
    for j in range(nb_boule_ind):
        x = x_ind + j * (ball_taille_ind + ball_espace_ind)
        y = y_ind + i * (ball_taille_ind+ ball_espace_ind)
        canvas.create_oval(x,y,x+ball_taille_ind,y+ball_taille_ind,fill="white",outline="black")
    y_ind += 40

fenetre.mainloop()