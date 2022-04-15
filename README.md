# projet_mastermind

####################
# sujet : puissance 3
# groupe_3_BI_TD2  
# menbres du goupe : Maud Guidoni, Ines Bel-Hadj, Jessica Lima Pinto
# https://github.com/uvsq22104163/projet_mastermind
####################


#######################
# import des librairies

from tkinter import*
import random as rd

#######################
# définition des constantes

# Hauteur du canvas

HAUTEUR = 700

# Largeur du canvas

LARGEUR = 700






#######################
#fonctions


#######################
# programmme principale

# définiton des widgets

root = Tk()

root.title("Mastermind")

canvas = Canvas(root, width= LARGEUR, height= HAUTEUR, bg = "black")

bouton_1joueur = Button(root, text = "jeu 1 joueur")
bouton_2joueur = Button(root, text = "jeu 2 joueurs")
bouton_sauv = Button(root, text = "sauvegarder")
bouton_couleur = Button(root, text = "choisir une couleur")
bouton_arriere = Button(root, text = "revenir en arrière")

# emplacement des widgets

canvas.grid(row = 1, rowspan = 4, column = 1)

bouton_1joueur.grid(row = 1 , column = 0)
bouton_2joueur.grid(row = 2 , column = 0, sticky="n")
bouton_sauv.grid(row = 3, column = 0)
bouton_couleur.grid(row = 0, column = 1)
bouton_arriere.grid(row = 4, column = 0)

# boucle principale

root.mainloop()


 


