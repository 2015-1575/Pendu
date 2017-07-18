#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 13:46:32 2017

@author: aymeric
"""
from donnees import *
import os.path
import json
import pickle
from random import randrange

def chargerScores():
    if os.path.isfile(scores):
        with open(scores, 'rb') as f:
            scoresSauvegarde = json.load(f)
    else:
        scoresSauvegarde = {}
    return scoresSauvegarde

def chargerJoueur(nomJoueur):
    sauvegarde = chargerScores()
    if nomJoueur in sauvegarde:
        scoreJoueur = sauvegarde[nomJoueur]
    else:
        scoreJoueur = 0
    return scoreJoueur

def sauvegarder(nomJoueur, scoreJoueur):
    ancienneSauvegarde = chargerScores()
    ancienneSauvegarde[nomJoueur] = scoreJoueur
    with open(scores, 'wb') as f:
        f.write(json.dumps(ancienneSauvegarde))


def choixMot():
    # Extraction de la liste de mots
    with open(dictionnaire, 'r') as f:
        contenu = f.read()
        listeMots = contenu.split("\n")

    # Sélection au hasard d'un mot
    return listeMots[randrange(len(listeMots))]

def getLettre(lettresTestees):
    lettre = "1"
    while True:
        lettre = str(raw_input("Entrez la lettre que vous voulez proposer: "))
        # Test que l'utilisateur rentre bien une lettre:
        if not lettre.isalpha() or len(lettre) != 1:
            print("Veuillez entrer une lettre!")
        elif lettre in lettresTestees:
            print("Vous avez déjà tenté cette lettre!")
        else:
            lettreTestees.append(lettre)
            break
    return lettre

def afficheMot(lettreTestees, motMystere):
    mot = []
    for lettre in motMystere:
        if lettre in lettreTestees:
            mot.append(lettre)
        else:
            mot.append('*')
    return ''.join(mot)
