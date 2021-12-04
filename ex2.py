import numpy as np
import random
'''
Cette fonction retourne l'indice ou le nombre aléatoire va être insérer
La condition d'arrêt est lorsque l'indice debut > l'indice fin
'''
def DPMR(val,debut,fin,tab):
    if debut <= fin:
        milieu=(debut+fin)//2
        if tab[milieu] == val:
            return milieu
        elif tab[milieu] < val:
            debut= milieu + 1
        else:
            fin= milieu -1  
        return DPMR(val,debut,fin,tab)
    else: 
        return debut

'''
Cette fonction va inserer le nombre aléatoire dans l'indice retourné par la fonction DPMR
'''
def insertion(longueur,min,max):
    sorted_random_list= np.sort(np.random.choice(np.arange(min,max+1),longueur))
    random_val= random.randint(min,max)
    indice= DPMR(random_val,0,longueur-1,sorted_random_list)
    sorted_random_list=np.insert(sorted_random_list,indice,random_val)

    return sorted_random_list

