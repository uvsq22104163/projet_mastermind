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
# longueur du resultat de verification
lg_verifi = 2
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

# variables pour les widgets label et entry
couleur1_var = IntVar()
couleur2_var = IntVar()
couleur3_var = IntVar()
couleur4_var = IntVar()
resultats_var = StringVar()


#######################
#fonctions


# fonction pour que chaque valeurs de la liste ce transforme en ronds de couleurs 
def choisir_couleur() :
    global essai
    # assimilation des numeros en listes
    code_a_tester=[couleur1_var.get(),couleur2_var.get(), couleur3_var.get(), couleur4_var.get()]
    
    # verification de la saisie dans les codes couleurs(impossible de mettre 0)
    if control_de_saisie(code_a_tester) == 0 :
        return
    
    # affichage du code saisi avec les cercles de couleur
    for i in range (0, lg_code) :
        cercle_code(i*(taille_cercle+espace_cercle), taille_cercle+essai*(taille_cercle+espace_cercle), code_a_tester[i])
    
    # remise à 0 des zones de saisie
    raz_zones_saisies()
    
    # cacul de la verfication entre le code que l'utilisatuer a saisie et le code genere aleatoirement
    place_exact, place_similaire = verif_code(list(code_a_tester), list(code_random))
    print("le code random  : ",code_random)
    print("Place exacte    : ",place_exact)
    print("Place similaire : ",place_similaire)
    print("Essai           : ",essai)
    # affichage verification (rond noir/blanc). les ronds noirs sont placés en premier 
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
    # si le nombre d'essai est superieur à 0 alors bouton retour de arriere active
    if essai > 0 :
        bouton_arriere['state'] = NORMAL

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
            # détection des couleurs avec une coincidence exacte et mise à zero des couleurs indentiques
            if i == j and c_test[i] == c_orig[j] :
                nb_exact = nb_exact + 1
                c_orig[j] = 0
                c_test[i] = 0
    # recherche des similaires differents de zero
    for i in range (len(c_test)) :
        for j in range (len(c_orig)) : 
            # détection des couleurs avec une coincidence sinmilaire, en evitant les zero et mise à zero des couleurs correspondantes
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
    # remise à 0 des canvas et des zones de saisies et aucun message
    canvas.delete("all")
    canvas2.delete("all")
    canvas3.delete("all")
    resultats_var.set('')
    raz_zones_saisies()
    # bouton sauvegarde desactivé
    bouton_sauv['state'] = DISABLED
    global list_essais, list_verification
    list_essais = []
    list_verification = []
    global essai 
    essai = 0
    global code_random
    code_random = []

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
    # bouton sauvegarde activé
    bouton_sauv['state'] = NORMAL

# partie à deux joeurs avec le premier joueur qui tape son code et l'autre qui joue
def partie_2_joueurs() :
    #ajout de la fonction d'initialisation quand in appui sur le bouton
    initialisation()
    # le bouton soumettre est activé
    bouton_soumettre['state'] = NORMAL
    # le bouton aide est desactivé
    bouton_aide['state'] = DISABLED
    #les saisies sont activées 
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
    bouton_sauv['state'] = NORMAL
    # effacement des zones de saisie
    raz_zones_saisies()
    # le bouton soumettre est affecter à la fonction choisir couleur
    bouton_soumettre['command'] = choisir_couleur

# fin de partie 
def fin_partie() :
    # les boutons et les saisies sont desactivés
    bouton_soumettre['state'] = DISABLED
    bouton_aide['state'] = DISABLED
    bouton_arriere['state'] = DISABLED
    bouton_sauv['state'] = DISABLED
    # affichage du code à trouver
    for i in range (0, lg_code) :
        cercle_saisi(i*(taille_cercle+espace_cercle), 5, code_random[i])
    # zones de saisies desactivees
    etat_saisie_couleur(DISABLED)

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

# controle de saisie avec impossibilite de mettre 0 et au dessus de 8 
def control_de_saisie(code_a_verifier) :
    codevalide = 1
    for i in range (0, lg_code) :
        if code_a_verifier[i] < 1 or code_a_verifier[i] > 8 :
            codevalide = 0
    # problème de syntaxe alors message d'erreur
    if codevalide == 0 :
            resultats_var.set("Erreur de saisie")
    # sinon aucun message
    else :
        resultats_var.set('')
    return codevalide

# aide pour le joueur
def aide() :
    temoin_unique = 0
    # la boucle continue si le code d'aide n'est pas unique par rapport aux codes déjà saisis et aux résultats de verification déjà existants
    while temoin_unique == 0 :
        code_test = []
        # génration du code d'aide (random)
        for i in range(0, lg_code) :
            code_test.extend([rd.randint(1, nb_couleur)])
        temoin_unique = 1
        # recherche du code d'aide dans les codes déjà saisis
        for i in range(0, len(list_essais)) :
            if code_test == list_essais[i] :
                temoin_unique = 0
        # cette boucle va chercher les valeurs de vérification du code d'aide dans les vérification déjà effectuées
        for i in range(0, len(list_verification)):
            place_exact, place_similaire = verif_code(list(code_test), list(code_random))
            [tempvar1 , tempvar2 ] = list_verification[i]
            # la ligne en dessous permet de tester en plus les ronds blanc
            #####if [place_exact, place_similaire] == list_verification[i] :
            # controle que la vérification du code d'aide ne donne pas une vérification exacte déjà trouvée par les essais de l'utilisateur
            if place_exact == tempvar1 :
                temoin_unique = 0
    # ajouter les valeurs de l'aide dans les zones de saisie
    couleur1_var.set(code_test[0])
    couleur2_var.set(code_test[1])
    couleur3_var.set(code_test[2])
    couleur4_var.set(code_test[3])

# revenir en arrière
def defaire() :
    global essai
    # boucle qui permet de revenir en arriere jusqu'à l'essai 0
    if len(objects1) > 0 :
        # effacement des 4 ronds de couleur
        for i in range(0, lg_code) :
            canvas.delete(objects1[-1])
            del(objects1[-1])
        place_exact, place_similaire = list_verification[-1]
        # effacement des possible ronds noir/blanc
        for i in range(0,  place_exact+place_similaire) :
            canvas2.delete(objects2[-1])
            del(objects2[-1])
        # effacement des dernières valeurs des listes et enleve un essai
        del(list_essais[-1])
        del(list_verification[-1])
        essai -= 1
    # si essai inferieur à 1 le bouton se desactive
    if essai < 1 :
        bouton_arriere['state'] = DISABLED

# sauvegarde dans un fichier
def sauvegarde() :
    # ouverture du fichier et ecriture
    fic = open("sauvegarde", "w")
    # ecriture du code saisi au hasard
    for valeur in code_random :
            fic.write(str(valeur)+",")
    fic.write("\n")
    for i in range(0, len(list_essais)) :
        # ajout des valeurs des essaies dans le fichier
        for valeur in list_essais[i] :
            fic.write(str(valeur)+",")
        fic.write("\n")
        # ajout des valeurs de verification dans le fichier
        for valeur in list_verification[i] :
            fic.write(str(valeur)+",")
        fic.write("\n")
    # fermeture du fichier
    fic.close()

# restauration de la sauvegarde
def restauration() :
    initialisation()
    # accès au variables globales qui vont être reconfigurées par le rechargement
    global essai, code_random, list_essais, list_verification
    # les boutons et les saisies sont activés
    bouton_soumettre['state'] = NORMAL
    bouton_aide['state'] = NORMAL
    etat_saisie_couleur(NORMAL)
    # ouverture du fichier
    fic = open("sauvegarde", "r")
    # lecture de la première ligne : code à découvrir
    line = fic.readline()
    # supression du retour à la ligne
    line = line.replace(",\n",'')
    # conversion de la chaine de caractère avec séparateur ',' en liste
    for valeur in line.split(',') :
        code_random.extend([int(valeur)])
    print ("code_random : ", code_random)
    # boucle de lecture du reste du fichier
    for line in fic:
        list_tmp=[]
        line = line.replace(",\n",'')
        # implatation des valeurs
        for  valeur in line.split(',') :
            list_tmp.extend([int(valeur)])
        # affichage des essais
        if len(list_tmp) == lg_code :
            list_essais.append(list_tmp)
            for i in range (0, lg_code) :
                cercle_code(i*(taille_cercle+espace_cercle), taille_cercle+essai*(taille_cercle+espace_cercle), list_tmp[i])           
        # affichage des résultats des vérifications
        else :
            list_verification.append(list_tmp)
            for i in range (0, list_tmp[0]+list_tmp[1]) :
                if i < list_tmp[0] :
                    cercle_verif(i*(taille_cercle+espace_cercle), taille_cercle+essai*(taille_cercle+espace_cercle), "black")
                else :
                    cercle_verif(i*(taille_cercle+espace_cercle), taille_cercle+essai*(taille_cercle+espace_cercle), "white")
            essai += 1
    # si l'essai est superieur à 0 alors les boutons s'activent
    if essai > 0 :
        bouton_arriere['state'] = NORMAL
    bouton_sauv['state'] = NORMAL
    print("liste essais : ",list_essais)
    print("liste verification : ",list_verification)
    # fermeture du fichier
    fic.close()

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
bouton_sauv = Button(root, text = "sauvegarder", command=sauvegarde, state= DISABLED)
bouton_recharger = Button(root, text = "recharger", command=restauration)
bouton_arriere = Button(root, text = "revenir en arrière", command=defaire, state= DISABLED)
bouton_soumettre = Button(root, text='Soumettre', command=choisir_couleur, state= DISABLED)
bouton_aide = Button(root, text='aide', command=aide, state= DISABLED)

# la fonction entry vient d'internet ( zone de saisie)
saisie_couleur1 = Entry(root, textvariable=couleur1_var, width = 3, state= DISABLED)
saisie_couleur2 = Entry(root, textvariable=couleur2_var, width = 3, state= DISABLED)
saisie_couleur3 = Entry(root, textvariable=couleur3_var, width = 3, state= DISABLED)
saisie_couleur4 = Entry(root, textvariable=couleur4_var, width = 3, state= DISABLED)

# la fonction label vient d'internet ( zone de texte)
resultats = Label(textvariable = resultats_var)
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


 


