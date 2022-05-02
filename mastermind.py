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

# longueur du code
lg_code = 4
# nombre de couleur
nb_couleur =6
# Hauteur du canvas
HAUTEUR = 500
# Largeur du canvas
LARGEUR = 300
taille_cercle = 30
espace_cercle = 5
essai = 0
nb_coup = 10
code_couleur = [ "null", "blue", "green", "yellow", "magenta", "red"]



root = Tk()

root.title("Mastermind")

couleur1_var = IntVar()
couleur2_var = IntVar()
couleur3_var = IntVar()
couleur4_var = IntVar()



#######################
# fonctions
def choisir_couleur() :
    # control partie en cours
    
    global essai
    code_a_tester=[ couleur1_var.get(),couleur2_var.get(), couleur3_var.get(), couleur4_var.get()]
    for i in range (0, lg_code) :
        cercle_code(i*(taille_cercle+espace_cercle), taille_cercle+essai*(taille_cercle+espace_cercle), code_a_tester[i])
    # cacul de la verfication

    # affichage verification

    # fin de partie gagnée
    
    
    
    essai = essai + 1 
    # fin de partie perdue
    print(code_a_tester)

#######################
# programmme principale


#######################
# generation du code
code_random = []
for i in range(0, lg_code) :
    code_random.extend([rd.randint(1, nb_couleur)])
print(code_random)

# cercle affichage code
def cercle_code(x, y, c) :
    canvas.create_oval((x, y), (x+taille_cercle, y+taille_cercle), fill = code_couleur[c])

# cercle affichage verification
def cercle_verif(x, y, c) :
    canvas2.create_oval((x, y), (x+taille_cercle, y+taille_cercle), fill = code_couleur[c])

# définiton des widgets





canvas = Canvas(root, width= LARGEUR, height= HAUTEUR, bg = "white")
canvas2 = Canvas(root, width= LARGEUR, height= HAUTEUR, bg = "white")

bouton_1joueur = Button(root, text = "jeu 1 joueur")
bouton_2joueur = Button(root, text = "jeu 2 joueurs")
bouton_sauv = Button(root, text = "sauvegarder")
bouton_arriere = Button(root, text = "revenir en arrière")
saisie_couleur1 = Entry(root, textvariable=couleur1_var, width = 1)
saisie_couleur2 = Entry(root, textvariable=couleur2_var, width = 1)
saisie_couleur3 = Entry(root, textvariable=couleur3_var, width = 1)
saisie_couleur4 = Entry(root, textvariable=couleur4_var, width = 1)
bouton_soumettre = Button(root, text='Soumettre', command=choisir_couleur)

# emplacement des widgets

canvas.grid(row = 1, rowspan = 10, column = 1, columnspan = 4)
canvas2.grid(row = 1, rowspan = 10, column = 5, columnspan = 4)

bouton_1joueur.grid(row = 1 , column = 0)
bouton_2joueur.grid(row = 2 , column = 0, sticky="n")
bouton_sauv.grid(row = 3, column = 0)
bouton_arriere.grid(row = 4, column = 0)
saisie_couleur1.grid(row = 12, column=1)
saisie_couleur2.grid(row = 12, column=2)
saisie_couleur3.grid(row = 12, column=3)
saisie_couleur4.grid(row = 12, column=4)
bouton_soumettre.grid (row = 12, column=5)


# boucle principale

root.mainloop()


 


