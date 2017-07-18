#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 13:46:33 2017

@author: aymeric
"""
from fonctions import *
from donnees import *


print("********** Jeu du Pendu **********")
continuerJeu = True
while continuerJeu == True:
    # Chargement du joueur
    nomJoueur = raw_input("Nom du joueur: ")
    scoreJoueur = chargerJoueur(nomJoueur);
    
    # Choix du mot à deviner
    motMystere = choixMot()
    motIncomplet = afficheMot(lettreTestees, motMystere)
    # Début de la partie
    score = 8  # Initialisation du score à 8
        
    while score > 0 or motIncomplet != motMystere:
        # Affichage du score
        print("Score = " + str(score))
        print(motIncomplet)
        # Choix d'une lettre
        essai = getLettre(lettreTestees)
        # Comparaison de la lettre avec le mot à deviner
        if essai in motMystere:
            motIncomplet = afficheMot(lettreTestees, motMystere)
            if motIncomplet == motMystere:
                print("Vous avez gagné")
                break
        else:
            score -= 1
            if score == 0:
                print("Vous avez perdu!")
                break
    # Fin de la partie ?
    continuerJeu = False
# Enregistrement des scores du joueur
scoreJoueur += score
sauvegarder(nomJoueur, scoreJoueur)
