import numpy as np
import random

class Exercice2:

    def DPMR(self,val,debut,fin):
        '''
        Cette fonction retourne l'indice (int) ou le nombre aléatoire va être insérer
        La condition d'arrêt est lorsque l'indice debut > l'indice fin
        val: (int) la valeur à insérer
        tab: (ndarray) le tableau d'entier trié dans l'ordre croissant
        debut: (int) indice indiquant le début du tableau
        fin: (int) indice indiquant la fin du tableau
        '''
        if debut <= fin:
            milieu=(debut+fin)//2
            if self.tab[milieu] == val:
                return milieu
            elif self.tab[milieu] < val:
                debut= milieu + 1
            else:
                fin= milieu -1  
            return self.DPMR(val,debut,fin)
        else: 
            return debut
    
    def insert_tab(self,tab):
        '''
        cette fonction permet d'inserer un tableau passer en parametre
        '''
        self.tab = tab

     
    def generer_tab_trie_aleatoire(self,longueur,min,max):
        '''
        Cette fonction retourne un tableau (ndarray) trié après avoir insérer une valeur aléatoire générée
        longueur: (int) taille du tableau
        min: (int) valeur minimale que peut prendre les élments du tableau ou la valeur aléatoire générée
        max: (int) valeur maximale que peut prendre les élments du tableau ou la valeur aléatoire générée
        ''' 
        self.tab = np.sort(np.random.choice(np.arange(min,max+1),longueur))

    def insertion(self,random_val):
        '''
        Cette fonction insére une valeur aléatoire générée ou passer en parametre et retoune un tableau 
        random_val: (int) valeur aléatoire
        ''' 
        if not random_val:
            random_val= random.randint(min,max)
        indice= self.DPMR(random_val,0,len(self.tab)-1)
        sorted_random_tab=np.insert(self.tab,indice,random_val)
        return sorted_random_tab


