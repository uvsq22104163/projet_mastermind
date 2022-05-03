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

#listes vides
code_random = []
list_essais = []
list_verification = []
objects1 = []
objects2 = []

#constantes du canvas
# Hauteur du canvas
HAUTEUR = 500
# Largeur du canvas
LARGEUR = 150
# decalage des cercles vis à vis du canvas(recentrage)
DECALAGE = 8

#constantes des cercles
# taille des cerles
taille_cercle = 30
# espaces entre les cercles
espace_cercle = 5

# formation des variables 
root = Tk()

root.title("Mastermind")

couleur1_var = IntVar()
couleur2_var = IntVar()
couleur3_var = IntVar()
couleur4_var = IntVar()
resultats_var = StringVar()


#######################
#fonctions


# fonction pour que chaque valeurs de la liste ce transforme en ronds de couleurs 
def choisir_couleur() :
    # assimilation des numeros en listes
    global essai
    code_a_tester=[couleur1_var.get(),couleur2_var.get(), couleur3_var.get(), couleur4_var.get()]
    
    # verification de la saisie dans les codes couleurs(impossible de mettre 0)
    if control_de_saisie(code_a_tester) == 0 :
        return
    
    # affichage du code saisi avec les cercles de couleur
    for i in range (0, lg_code) :
        cercle_code(i*(taille_cercle+espace_cercle), taille_cercle+essai*(taille_cercle+espace_cercle), code_a_tester[i])
    
    # effacement des zones de saisie
    raz_zones_saisies()
    
    # cacul de la verfication entre le code que l'utilisatuer a saisie et le code genere aleatoirement
    place_exact, place_similaire = verif_code(list(code_a_tester), list(code_random))
    print("le code random  : ",code_random)
    print("Place exacte    : ",place_exact)
    print("Place similaire : ",place_similaire)
    print("Essai           : ",essai)
    # affichage verification, 
    for i in range (0, place_exact+place_similaire) :
        if i < place_exact :
            cercle_verif(i*(taille_cercle+espace_cercle), taille_cercle+essai*(taille_cercle+espace_cercle), "black")
        else :
            cercle_verif(i*(taille_cercle+espace_cercle), taille_cercle+essai*(taille_cercle+espace_cercle), "white")
    
    # sauvegarde de l'essai de l'utilisateur
    list_essais.append(code_a_tester)
    # sauvegarde de la vérification de l'essai de l'utilisateur (rond noir/blanc)
    list_verification.append([place_exact, place_similaire])
    print("liste essais : ",list_essais)
    print("liste verification : ",list_verification)
    # nombre d'essai
    essai = essai + 1 

    # fin de partie gagnée
    if place_exact == 4 :
        if essai <= 10 :
            resultats_var.set("Gagné !!")
            fin_partie()
    # fin de partie perdue
    else :
        if essai >= 10 :
            resultats_var.set("Perdu :(")
            fin_partie()
        
# cacul de la verification pour la creation des ronds noir/blanc
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
    global objects1
    x += DECALAGE
    objects1.append(canvas.create_oval((x, y), (x+taille_cercle, y+taille_cercle), fill = code_couleur[c]))

# cercle affichage verification
def cercle_verif(x, y, c) :
    global objects2
    x += DECALAGE
    objects2.append(canvas2.create_oval((x, y), (x+taille_cercle, y+taille_cercle), fill = c))

# cercle affichage code solution
def cercle_saisi(x, y, c) :
    x += DECALAGE
    canvas3.create_oval((x, y), (x+taille_cercle, y+taille_cercle), fill = code_couleur[c])

# initialisation des canvas, des zones de saisies... retour à zeros
def initialisation() :
    canvas.delete("all")
    canvas2.delete("all")
    canvas3.delete("all")
    resultats_var.set('')
    raz_zones_saisies()
    global list_essais, list_verification
    list_essais = []
    list_verification = []
    global essai 
    essai = 0

# partie un joueur avec le code genere au hasard 
def partie_1_joueur() :
    #ajout de la fonction d'initialisation quand in appui sur le bouton
    initialisation()
    #les boutons et les saisies activés
    bouton_soumettre['state'] = NORMAL
    bouton_aide['state'] = NORMAL
    etat_saisie_couleur(NORMAL)
    # generation du code genere au hasard
    global code_random
    code_random =[]
    # sauvegarde du code genere au hasard
    for i in range(0, lg_code) :
        code_random.extend([rd.randint(1, nb_couleur)])
    print("code genere : ",code_random)

# partie à deux joeurs avec le premier joueur qui tape son code et l'autre qui joue
def partie_2_joueurs() :
    #ajout de la fonction d'initialisation quand in appui sur le bouton
    initialisation()
    # le bouton soumettre est activé
    bouton_soumettre['state'] = NORMAL
    # le bouton aide est desactivé
    bouton_aide['state'] = DISABLED
    #les aisies sont activées 
    etat_saisie_couleur(NORMAL)
    # le bouton soumettre est affecter à la fonction choisir couleur
    bouton_soumettre['command'] = saisie_code_j2

# le deuxieme joueur tape son code
def saisie_code_j2() :
    global code_random
    # assimilation des numeros en listes
    code_random = [ couleur1_var.get(),couleur2_var.get(), couleur3_var.get(), couleur4_var.get()]
    # verification de la saisie dans les codes couleurs(impossible de mettre 0)
    if control_de_saisie(code_random) == 0 :
        return
    print("code saisi : ",code_random)
    # le bouton aide devient accessible
    bouton_aide['state'] = NORMAL
    # effacement des zones de saisie
    raz_zones_saisies()
    # le bouton soumettre est affecter à la fonction choisir couleur
    bouton_soumettre['command'] = choisir_couleur

# fin de partie 
def fin_partie() :
    # les boutons et les saisies sont desactivés
    bouton_soumettre['state'] = DISABLED
    bouton_aide['state'] = DISABLED
    # les cercles sont effacés
    for i in range (0, lg_code) :
        cercle_saisi(i*(taille_cercle+espace_cercle), 5, code_random[i])
    etat_saisie_couleur(DISABLED)
    print ("Fin de partie")

# choix des etats des zones de saisie ( normal = actif et disabled = pas actif)
def etat_saisie_couleur(etat) :
    saisie_couleur1['state'] = etat
    saisie_couleur2['state'] = etat
    saisie_couleur3['state'] = etat
    saisie_couleur4['state'] = etat

# zones de saisie vides
def raz_zones_saisies() :
    couleur1_var.set('')
    couleur2_var.set('')
    couleur3_var.set('')
    couleur4_var.set('')

# controle de saisie avec impossibiliter de mettre 0 et au dessus de 8, si maivaise saisie : affichage erreur de saisie 
def control_de_saisie(code_a_verifier) :
    codevalide = 1
    for i in range (0, lg_code) :
        if code_a_verifier[i] < 1 or code_a_verifier[i] > 8 :
            codevalide = 0
    if codevalide == 0 :
            resultats_var.set("Erreur de saisie")
    else :
        resultats_var.set('')
    return codevalide

# aide pour le joueur
def aide() :
    temoin_unique = 0
    while temoin_unique == 0 :
        code_test = []
        for i in range(0, lg_code) :
            code_test.extend([rd.randint(1, nb_couleur)])
        temoin_unique = 1
        for i in range(0, len(list_essais)) :
            if code_test == list_essais[i] :
                temoin_unique = 0
        for i in range(0, len(list_verification)):
            place_exact, place_similaire = verif_code(list(code_test), list(code_random))
            [tempvar1 , tempvar2 ] = list_verification[i]
            #if [place_exact, place_similaire] == list_verification[i] :
            if place_exact == tempvar1 :
                temoin_unique = 0
    couleur1_var.set(code_test[0])
    couleur2_var.set(code_test[1])
    couleur3_var.set(code_test[2])
    couleur4_var.set(code_test[3])

def defaire() :
    global essai
    if len(objects1) > 0 :
        for i in range(0, lg_code) :
            canvas.delete(objects1[-1])
            del(objects1[-1])
        place_exact, place_similaire = list_verification[-1]
        for i in range(0,  place_exact+place_similaire) :
            canvas2.delete(objects2[-1])
            del(objects2[-1])
        del(list_essais[-1])
        del(list_verification[-1])
        essai -= 1



#######################
# programmme principale
raz_zones_saisies()

# définiton des widgets

#premier canvas (gauche)
canvas = Canvas(root, width= LARGEUR, height= HAUTEUR, bg = "white")
#deuxieme cavas (droite)
canvas2 = Canvas(root, width= LARGEUR, height= HAUTEUR, bg = "white")
#troisième canvas (haut, gauche)
canvas3 = Canvas(root, width= LARGEUR, height= 50, bg = "white")

bouton_1joueur = Button(root, text = "jeu 1 joueur", command= partie_1_joueur)
bouton_2joueur = Button(root, text = "jeu 2 joueurs", command= partie_2_joueurs)
bouton_sauv = Button(root, text = "sauvegarder")
bouton_recharger = Button(root, text = "recharger")
bouton_arriere = Button(root, text = "revenir en arrière", command=defaire)

# la fonction entry vient d'internet ( zone de saisie)
saisie_couleur1 = Entry(root, textvariable=couleur1_var, width = 3, state= DISABLED)
saisie_couleur2 = Entry(root, textvariable=couleur2_var, width = 3, state= DISABLED)
saisie_couleur3 = Entry(root, textvariable=couleur3_var, width = 3, state= DISABLED)
saisie_couleur4 = Entry(root, textvariable=couleur4_var, width = 3, state= DISABLED)
bouton_soumettre = Button(root, text='Soumettre', command=choisir_couleur, state= DISABLED)
bouton_aide = Button(root, text='aide', command=aide, state= DISABLED)
# la fonction entry vient d'internet ( zone de texte)
resultats = Label(textvariable = resultats_var )
regles = Label(text = "code couleur :""\n""\n1 = bleu\n2 = vert\n3 = jaune\n4 = violet\n5 = rouge\n6 = orange\n7 = gris\n8 = rose""\n""\n""rond noir = bien placé""\n""rond blanc = mal placé ")

# emplacement des widgets

canvas.grid(row = 1, rowspan = 10, column = 1, columnspan = 4)
canvas2.grid(row = 1, rowspan = 10, column = 5, columnspan = 4)
canvas3.grid(row = 0, rowspan = 1, column = 1, columnspan = 4)

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
resultats.grid(row = 0, column = 5)
regles.grid(row = 7, column = 0)

# boucle principale

root.mainloop()


 


