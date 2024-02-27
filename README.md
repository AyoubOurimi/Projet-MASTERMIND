# Projet-MASTERMIND
Quand vous téléchargez le fichier Projet_Mastermind, il y'aura un fichier nommé Mastermind 3.0 qui sera le jeu Mastermind, et un autre dossier Mastermind BETA qui regroupe tous les fichiers sur lequel nous avons fait et comment on a anvacé au fur et à mesure de notre projet, pour que vous ayez un odre d'idée.

Quand le programme "Mastermind_Jeu" sera lancé, une première interface va apparaître, elle contient les règles du jeu à lire impérativement avant de cliquer sur l'un des deux boutons : "Mode 1 joueur" et "Mode 2 joueurs" afin de connaître les règles du jeu du MasterMind.

Une fois avoir cliqué sur l'un des deux boutons, la première interface se ferme et en ouvre une deuxième : elle contient l'interface graphique du plateau de jeu. A partir de là : une grille de boules blanche apparaît et, juste au dessus, quatre boutons de couleur aléatoire numérotés de 1 à 4. Ceux-ci, une fois appuyés vont changer la couleur des boules : le bouton 1 change les boules de la première colonne, etc. Une colonne contenant les couleurs disponibles est située à gauche de la grille de bloules.

Une fois les quatre boules de la ligne les couleurs choisies, il faut appuyer sur le bouton valider situé à droite des boutons à numéro. Ce bouton va va passer à la ligne de boule suivante et affichera le nombre de boules ayant la même couleur que celui du code secret, indiqué par une petite boule noir et un numéro, et le nombre de boules ayant la même couleur ainsi que la même position que celui du code secret, indiqué par une petite boule blanche et un numéro. Si l'une des tentatives du joueur ne lui convient pas, celui-ci peut choisir de revenir en arrière grâce au bouton "Retour". (qui est censé être de la triche dans le jeu officiel)

Si le code secret à été trouvé par le joueur, la fenêtre du plateau de jeu se fermera et ouvrira automatiquement une fenêtre appelée "Tu as gagné !" avec un smiley jaune souriant disant "Bien joué ! le code était:" et le code secret d'affiché. Dans le cas où le joueur n'a pas réussi à trouver le code dans les 10 essais accordés par le jeu, la fenêtre du plateau de jeu se fermera automatiquement et ouvrira une fenêtre appelée "Tu as perdu!" avec un smiley rouge triste disant "Dommage ! le code était:" et le code sera affiché. Si vous il reste des boules blanches dans lorsque vous faites une proposition du code secret, cela affichera un message d'erreur qui vous demandera de remplir toutes les boules blanches.

Pour une meilleure expérience en mode un joueur, il est conseillé de mettre en commentaire dans la fonction "init " les parties qui sont noté entre deux ##, en locurrence le boutou afficher code, cacher code, le bouton retour si vous voulez pas tricher et l'affichage du code secret.

Attention, dans le mode 2 joueurs, le joueur écrivant le code secret doit impérativement le faire AVANT que le le second joueur ne commence à jouer, sinon un les boutons qui sont situés en haut du tableau de jeu ne s'afficheront pas et pas conséquent, vous ne pourrez pas commencer à jouer, de même ce code secret ne doit pas contenir de boule blanche car dans le cas contraire, un message d'erreur indiquant de retirer cette boule blanche apparaîtra. Une fois le code validé, le code doit être disimulé grâce au bouton "Cacher".

La partie peut enfin commencer pour le second joueur.

Ce qui marche : Les boutons "Mode 1 joueur", "Mode 2 joueurs", "Quitter", "Retour", "Afficher", "Cacher", "Valider ( de symbole "Validé")", "1", "2", "3" et "4" focntionnent. Sauvegarder fonctionne mais il est inutile car charger ne fonctionne pas (vous pouvez retrouver la fonction charger à la toute fin de notre code)

Ce qui ne marche pas : Les boutons "Sauvegarder" et "Charger" ne fonctionnent pas, le bouton "Aide" n'existe pas et ces fonctions se situent à la fin du code en commentaire.
