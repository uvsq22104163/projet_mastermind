# projet_mastermind

####################
# sujet : mastermind
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

#constantes code
#choix des couleurs
code_couleur = [ "null", "blue", "green", "yellow", "purple", "red", "orange", "grey", "pink"]
# longueur du code
lg_code = 4
# nombre de couleur
nb_couleur = 8
#nombre d'essai
essai = 0
#nombre de coup
nb_coup = 10

#constantes du canvas
# Hauteur du canvas
HAUTEUR = 500
# Largeur du canvas
LARGEUR = 300

#conctantes des cercles
#taille des cerles
taille_cercle = 30
#espaces entre les cercles
espace_cercle = 5

#variables 
root = Tk()

root.title("Mastermind")

couleur1_var = IntVar()
couleur2_var = IntVar()
couleur3_var = IntVar()
couleur4_var = IntVar()
resultats_var = StringVar()
resultats_var.set('')
couleur1_var.set('')
couleur2_var.set('')
couleur3_var.set('')
couleur4_var.set('')


#######################
# generation du code
code_random = []
for i in range(0, lg_code) :
    code_random.extend([rd.randint(1, nb_couleur)])
print(code_random)

#######################
# fonctions
# fonction pour que chaque valeurs de la liste ce transforme en ronds de couleurs 
def choisir_couleur() :
    # control partie en cours
    
    global essai
    code_a_tester=[ couleur1_var.get(),couleur2_var.get(), couleur3_var.get(), couleur4_var.get()]
    for i in range (0, lg_code) :
        cercle_code(i*(taille_cercle+espace_cercle), taille_cercle+essai*(taille_cercle+espace_cercle), code_a_tester[i])
    couleur1_var.set('')
    couleur2_var.set('')
    couleur3_var.set('')
    couleur4_var.set('')
    
    # cacul de la verfication
    place_exact, place_similaire = verif_code(list(code_a_tester), list(code_random))
    print("le conde random : ",code_random)
    print("Place exacte    : ",place_exact)
    print("Place similaire : ",place_similaire)
    # affichage verification
    for i in range (0, place_exact+place_similaire) :
        if i < place_exact :
            cercle_verif(i*(taille_cercle+espace_cercle), taille_cercle+essai*(taille_cercle+espace_cercle), "black")
        else :
            cercle_verif(i*(taille_cercle+espace_cercle), taille_cercle+essai*(taille_cercle+espace_cercle), "white")
    
    # fin de partie gagnée
    essai = essai + 1 
    print("nombre d'essai :", essai)

    if place_exact == 4 :
        if essai <= 10 :
            print(resultats_var.set("gagner"))
           
    # fin de partie perdue
 
    if place_exact != 4 :
        if essai >= 10 :
            print(resultats_var.set("perdu"))
            

    # fin de fonction

    
# cacul de la verfication

def verif_code(c_test, c_orig) :
    nb_exact =0 
    nb_similaire = 0
    # recherche des exacts en remplacant par zero
    for i in range (len(c_test)) :
        for j in range (len(c_orig)) :
            if i == j and c_test[i] == c_orig[j] :
                nb_exact = nb_exact + 1
                c_orig[j] = 0
                c_test[i] = 0
    # recherche des similaires differents de zero
    for i in range (len(c_test)) :
        for j in range (len(c_orig)) : 
            if i != j and c_test[i] == c_orig[j] and c_test[i] != 0 :
                nb_similaire = nb_similaire + 1 
                c_orig[j] == 0 
                c_test[i] = 0          
    return nb_exact, nb_similaire

# cercle affichage code
def cercle_code(x, y, c) :
    canvas.create_oval((x, y), (x+taille_cercle, y+taille_cercle), fill = code_couleur[c])

# cercle affichage verification
def cercle_verif(x, y, c) :
    canvas2.create_oval((x, y), (x+taille_cercle, y+taille_cercle), fill = c)

#######################
# programmme principale


# définiton des widgets

canvas = Canvas(root, width= LARGEUR, height= HAUTEUR, bg = "white")
canvas2 = Canvas(root, width= LARGEUR, height= HAUTEUR, bg = "white")

bouton_1joueur = Button(root, text = "jeu 1 joueur")
bouton_2joueur = Button(root, text = "jeu 2 joueurs")
bouton_sauv = Button(root, text = "sauvegarder")
bouton_recharger = Button(root, text = "recharger")
bouton_arriere = Button(root, text = "revenir en arrière")

saisie_couleur1 = Entry(root, textvariable=couleur1_var, width = 3)
saisie_couleur2 = Entry(root, textvariable=couleur2_var, width = 3)
saisie_couleur3 = Entry(root, textvariable=couleur3_var, width = 3)
saisie_couleur4 = Entry(root, textvariable=couleur4_var, width = 3)
bouton_soumettre = Button(root, text='Soumettre', command=choisir_couleur)
bouton_aide = Button(root, text='aide', command=choisir_couleur)
resultats = Label(textvariable = resultats_var )
regles = Label(text = "code couleur :""\n""\n1 = bleu\n2 = vert\n3 = jaune\n4 = violet\n5 = rouge\n6 = orange\n7 = gris\n8 = rose""\n""\n""rond noir = bien placé""\n""rond blanc = mal placé ")

# emplacement des widgets

canvas.grid(row = 1, rowspan = 10, column = 1, columnspan = 4)
canvas2.grid(row = 1, rowspan = 10, column = 5, columnspan = 4)

bouton_1joueur.grid(row = 1 , column = 0)
bouton_2joueur.grid(row = 2 , column = 0, sticky="n")
bouton_sauv.grid(row = 3, column = 0)
bouton_recharger.grid(row = 4, column = 0)
bouton_arriere.grid(row = 5, column = 0)

saisie_couleur1.grid(row = 12, column=1)
saisie_couleur2.grid(row = 12, column=2)
saisie_couleur3.grid(row = 12, column=3)
saisie_couleur4.grid(row = 12, column=4)
bouton_soumettre.grid (row = 12, column=5)
bouton_aide.grid (row = 12, column=6)
resultats.grid(row = 0, column = 6)
regles.grid(row = 7, column = 0)

# boucle principale

root.mainloop()


 


