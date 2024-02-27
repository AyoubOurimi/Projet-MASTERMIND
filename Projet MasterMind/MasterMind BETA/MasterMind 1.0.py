import tkinter as tk
import random
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

taille_ball=20
taille_ballref=10

fenetre= tk.Tk()
fenetre.title("Mastermind")
fenetre.geometry("1000x875")
fenetre.resizable(height=False,width=False)

canvas0 = tk.Canvas(fenetre, bg="grey",borderwidth=3,relief="groove",width=400,height=810) #Interface sur laquelle on va travailler le jeu 

#Boules à choix (des qu'on appuie sur l'une d'entre elles la boules de la ligne X changera de couleur)
Redball = canvas0.create_oval((100,15), (100+taille_ball,15+taille_ball),outline="black",fill="Red")
Blueball = canvas0.create_oval((125,15), (125+taille_ball,15+taille_ball),outline="black",fill="blue")
Greenball= canvas0.create_oval((150,15), (150+taille_ball,15+taille_ball),outline="black",fill="green")
Yellowball= canvas0.create_oval((175,15), (175+taille_ball,15+taille_ball),outline="black",fill="yellow")
Orangeball= canvas0.create_oval((200,15), (200+taille_ball,15+taille_ball),outline="black",fill="orange")
Purpleball= canvas0.create_oval((225,15), (225+taille_ball,15+taille_ball),outline="black",fill="purple")
Pinkball= canvas0.create_oval((250,15), (250+taille_ball,15+taille_ball),outline="black",fill="pink")
Cyanball= canvas0.create_oval((275,15), (275+taille_ball,15+taille_ball),outline="black",fill="cyan")

#Boules qui vont changer de couleurs en fonction du choix de l'utilisateur
"ligne1"
Ball1_1 = canvas0.create_oval((50,100), (50+taille_ball,100+taille_ball),outline="black",fill="white")
Ball1_2 = canvas0.create_oval((75,100), (75+taille_ball,100+taille_ball),outline="black",fill="white")
Ball1_3 = canvas0.create_oval((100,100), (100+taille_ball,100+taille_ball),outline="black",fill="white")
Ball1_3 = canvas0.create_oval((125,100), (125+taille_ball,100+taille_ball),outline="black",fill="white")
"ligne2"
Ball2_1 = canvas0.create_oval((50,175), (50+taille_ball,175+taille_ball),outline="black",fill="white")
Ball2_2 = canvas0.create_oval((75,175), (75+taille_ball,175+taille_ball),outline="black",fill="white")
Ball2_3 = canvas0.create_oval((100,175), (100+taille_ball,175+taille_ball),outline="black",fill="white")
Ball2_3 = canvas0.create_oval((125,175), (125+taille_ball,175+taille_ball),outline="black",fill="white")
"ligne3"
Ball3_1 = canvas0.create_oval((50,250), (50+taille_ball,250+taille_ball),outline="black",fill="white")
Ball3_2 = canvas0.create_oval((75,250), (75+taille_ball,250+taille_ball),outline="black",fill="white")
Ball3_3 = canvas0.create_oval((100,250), (100+taille_ball,250+taille_ball),outline="black",fill="white")
Ball3_3 = canvas0.create_oval((125,250), (125+taille_ball,250+taille_ball),outline="black",fill="white")
"ligne4"
Ball4_1 = canvas0.create_oval((50,325), (50+taille_ball,325+taille_ball),outline="black",fill="white")
Ball4_2 = canvas0.create_oval((75,325), (75+taille_ball,325+taille_ball),outline="black",fill="white")
Ball4_3 = canvas0.create_oval((100,325), (100+taille_ball,325+taille_ball),outline="black",fill="white")
Ball4_3 = canvas0.create_oval((125,325), (125+taille_ball,325+taille_ball),outline="black",fill="white")
"ligne5"
Ball5_1 = canvas0.create_oval((50,400), (50+taille_ball,400+taille_ball),outline="black",fill="white")
Ball5_2 = canvas0.create_oval((75,400), (75+taille_ball,400+taille_ball),outline="black",fill="white")
Ball5_3 = canvas0.create_oval((100,400), (100+taille_ball,400+taille_ball),outline="black",fill="white")
Ball5_3 = canvas0.create_oval((125,400), (125+taille_ball,400+taille_ball),outline="black",fill="white")
"ligne6"
Ball6_1 = canvas0.create_oval((50,475), (50+taille_ball,475+taille_ball),outline="black",fill="white")
Ball6_2 = canvas0.create_oval((75,475), (75+taille_ball,475+taille_ball),outline="black",fill="white")
Ball6_3 = canvas0.create_oval((100,475), (100+taille_ball,475+taille_ball),outline="black",fill="white")
Ball6_3 = canvas0.create_oval((125,475), (125+taille_ball,475+taille_ball),outline="black",fill="white")
"ligne7"
Ball7_1 = canvas0.create_oval((50,550), (50+taille_ball,550+taille_ball),outline="black",fill="white")
Ball7_2 = canvas0.create_oval((75,550), (75+taille_ball,550+taille_ball),outline="black",fill="white")
Ball7_3 = canvas0.create_oval((100,550), (100+taille_ball,550+taille_ball),outline="black",fill="white")
Ball7_3 = canvas0.create_oval((125,550), (125+taille_ball,550+taille_ball),outline="black",fill="white")
"ligne8"
Ball8_1 = canvas0.create_oval((50,625), (50+taille_ball,625+taille_ball),outline="black",fill="white")
Ball8_2 = canvas0.create_oval((75,625), (75+taille_ball,625+taille_ball),outline="black",fill="white")
Ball8_3 = canvas0.create_oval((100,625), (100+taille_ball,625+taille_ball),outline="black",fill="white")
Ball8_3 = canvas0.create_oval((125,625), (125+taille_ball,625+taille_ball),outline="black",fill="white")
"ligne9"
Ball9_1 = canvas0.create_oval((50,700), (50+taille_ball,700+taille_ball),outline="black",fill="white")
Ball9_2 = canvas0.create_oval((75,700), (75+taille_ball,700+taille_ball),outline="black",fill="white")
Ball9_3 = canvas0.create_oval((100,700), (100+taille_ball,700+taille_ball),outline="black",fill="white")
Ball9_3 = canvas0.create_oval((125,700), (125+taille_ball,700+taille_ball),outline="black",fill="white")
"ligne10"
Ball10_1 = canvas0.create_oval((50,775), (50+taille_ball,775+taille_ball),outline="black",fill="white")
Ball10_2 = canvas0.create_oval((75,775), (75+taille_ball,775+taille_ball),outline="black",fill="white")
Ball10_3 = canvas0.create_oval((100,775), (100+taille_ball,775+taille_ball),outline="black",fill="white")
Ball10_3 = canvas0.create_oval((125,775), (125+taille_ball,775+taille_ball),outline="black",fill="white")

#Boules référentiels pour savoir: Si boule bien placé orange, Si mal placé gris orange , Si n'existe pas dans la combi aléatoire noir
"ligne1"
Ballref1_1 = canvas0.create_oval((300,95), (300+taille_ballref,95+taille_ballref),outline="black",fill="white")
Ballref1_2 = canvas0.create_oval((320,95), (320+taille_ballref,95+taille_ballref),outline="black",fill="white")
Ballref1_3 = canvas0.create_oval((300,115), (300+taille_ballref,115+taille_ballref),outline="black",fill="white")
Ballref1_4 = canvas0.create_oval((320,115), (320+taille_ballref,115+taille_ballref),outline="black",fill="white")
"ligne2"
Ballref2_1 = canvas0.create_oval((300,170), (300+taille_ballref,170+taille_ballref),outline="black",fill="white")
Ballref2_2 = canvas0.create_oval((320,170), (320+taille_ballref,170+taille_ballref),outline="black",fill="white")
Ballref2_3 = canvas0.create_oval((300,190), (300+taille_ballref,190+taille_ballref),outline="black",fill="white")
Ballref2_4 = canvas0.create_oval((320,190), (320+taille_ballref,190+taille_ballref),outline="black",fill="white")
"ligne3"
Ballref3_1 = canvas0.create_oval((300,245), (300+taille_ballref,245+taille_ballref),outline="black",fill="white")
Ballref3_2 = canvas0.create_oval((320,245), (320+taille_ballref,245+taille_ballref),outline="black",fill="white")
Ballref3_3 = canvas0.create_oval((300,265), (300+taille_ballref,265+taille_ballref),outline="black",fill="white")
Ballref3_4 = canvas0.create_oval((320,265), (320+taille_ballref,265+taille_ballref),outline="black",fill="white")
"ligne4"
Ballref4_1 = canvas0.create_oval((300,320), (300+taille_ballref,320+taille_ballref),outline="black",fill="white")
Ballref4_2 = canvas0.create_oval((320,320), (320+taille_ballref,320+taille_ballref),outline="black",fill="white")
Ballref4_3 = canvas0.create_oval((300,340), (300+taille_ballref,340+taille_ballref),outline="black",fill="white")
Ballref4_4 = canvas0.create_oval((320,340), (320+taille_ballref,340+taille_ballref),outline="black",fill="white")
"ligne5"
Ballref5_1 = canvas0.create_oval((300,395), (300+taille_ballref,395+taille_ballref),outline="black",fill="white")
Ballref5_2 = canvas0.create_oval((320,395), (320+taille_ballref,395+taille_ballref),outline="black",fill="white")
Ballref5_3 = canvas0.create_oval((300,415), (300+taille_ballref,415+taille_ballref),outline="black",fill="white")
Ballref5_4 = canvas0.create_oval((320,415), (320+taille_ballref,415+taille_ballref),outline="black",fill="white")
"ligne61"
Ballref6_1 = canvas0.create_oval((300,470), (300+taille_ballref,470+taille_ballref),outline="black",fill="white")
Ballref6_2 = canvas0.create_oval((320,470), (320+taille_ballref,470+taille_ballref),outline="black",fill="white")
Ballref6_3 = canvas0.create_oval((300,490), (300+taille_ballref,490+taille_ballref),outline="black",fill="white")
Ballref6_4 = canvas0.create_oval((320,490), (320+taille_ballref,490+taille_ballref),outline="black",fill="white")
"ligne7"
Ballref7_1 = canvas0.create_oval((300,545), (300+taille_ballref,545+taille_ballref),outline="black",fill="white")
Ballref7_2 = canvas0.create_oval((320,545), (320+taille_ballref,545+taille_ballref),outline="black",fill="white")
Ballref7_3 = canvas0.create_oval((300,565), (300+taille_ballref,565+taille_ballref),outline="black",fill="white")
Ballref7_4 = canvas0.create_oval((320,565), (320+taille_ballref,565+taille_ballref),outline="black",fill="white")
"ligne8"
Ballref8_1 = canvas0.create_oval((300,620), (300+taille_ballref,620+taille_ballref),outline="black",fill="white")
Ballref8_2 = canvas0.create_oval((320,620), (320+taille_ballref,620+taille_ballref),outline="black",fill="white")
Ballref8_3 = canvas0.create_oval((300,640), (300+taille_ballref,640+taille_ballref),outline="black",fill="white")
Ballref8_4 = canvas0.create_oval((320,640), (320+taille_ballref,640+taille_ballref),outline="black",fill="white")
"ligne9"
Ballref9_1 = canvas0.create_oval((300,695), (300+taille_ballref,695+taille_ballref),outline="black",fill="white")
Ballref9_2 = canvas0.create_oval((320,695), (320+taille_ballref,695+taille_ballref),outline="black",fill="white")
Ballref9_3 = canvas0.create_oval((300,715), (300+taille_ballref,715+taille_ballref),outline="black",fill="white")
Ballref9_4 = canvas0.create_oval((320,715), (320+taille_ballref,715+taille_ballref),outline="black",fill="white")
"ligne10"
Ballref10_1 = canvas0.create_oval((300,770), (300+taille_ballref,770+taille_ballref),outline="black",fill="white")
Ballref10_2 = canvas0.create_oval((320,770), (320+taille_ballref,770+taille_ballref),outline="black",fill="white")
Ballref10_3 = canvas0.create_oval((300,790), (300+taille_ballref,790+taille_ballref),outline="black",fill="white")
Ballref10_4 = canvas0.create_oval((320,790), (320+taille_ballref,790+taille_ballref),outline="black",fill="white")


canvas0.grid(row=0,column=0)

fenetre.mainloop()
