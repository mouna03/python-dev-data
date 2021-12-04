import random
import numpy as np

def generer(num,min,max):
    """
    num: (int) nombre de numéros pour le billet de loterie
    min: (int) valeur minimale tirés par l'organisateur
    max: (int) valeur maximale tirés par l'organisateur
    retourne une liste de num compris entre min et max, sans doublons, dans l'ordre croissant
    """
    return np.sort(np.random.choice(np.arange(min,max+1),num,replace=False))

#print(generer(6,1,49))