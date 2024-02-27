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
fenetre.geometry("1000x820")
fenetre.resizable(height=False,width=False)

canvas = tk.Canvas(fenetre, bg="grey",borderwidth=3,relief="groove",width=550,height=720) #Interface sur laquelle on va travailler le jeu
canvas.pack(side=LEFT)
#
#Création des paramètress
cadre2 = tk.LabelFrame(fenetre, text="Paramètres et Commande",font=("Arial",13),fg = 'black')
#cadre2.pack(side=RIGHT,fill="y", expand="yes") #permet de faire une fenetre qui va contenir les boutons etc
cadre2.place(x=700,y=100)


bouton1 = tk.Radiobutton(cadre2, text="facile")#les petits boutons avec le quel tu coche
bouton2 = tk.Radiobutton(cadre2, text="moyen")
bouton3 = tk.Radiobutton(cadre2, text="difficile")
start = tk.Button(cadre2,text= "Start")
bouton=tk.Button(cadre2,text="Quitter")
bload = tk.Button(cadre2,text="Charger")
bsav = tk.Button(cadre2,text= "Sauvegarder")
brep= tk.Button(cadre2,text="Correction")
bhelp= tk.Button(cadre2,text= "aide")

bhelp.pack()
bouton1.pack(side=TOP)
bouton2.pack(side=TOP)
bouton3.pack(side=TOP)
brep.pack()
bsav.pack()
bload.pack()

fenetre.mainloop()