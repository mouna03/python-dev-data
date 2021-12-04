from logging import log
import numpy as np
from numpy.core import numeric
import pandas as pd

import matplotlib.pylab as plt
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
class Exercice3:

    def __init__(self):
        

        self.code_dispo=pd.read_csv("data/codes disponibles.csv")
        self.tous_code=pd.read_csv("data/tous les codes.csv")

    def pourcentage(self):
        sum_code_dispo=np.sum(self.code_dispo.values.tolist())
        sum_tous_code=np.sum(self.tous_code.values.tolist())
        return (sum_code_dispo/sum_tous_code)*100
    

    def frequence(self,code):
        """
        calcul occurrence du code
        """
        occ_code=self.code_dispo[self.code_dispo["codes"]==int(code) ].count()[0]
        total_code=self.code_dispo.shape[0]
        return occ_code/total_code


    def graph_frequence(self, list_code_dispo):
        """
        fréquence de chaque code dans la liste donnée
        """
        result=[]
        for code in list_code_dispo:
            result.append(self.frequence(code))
    
        """
        Afficher les code disponibles et leurs fréquence
        """
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.bar(list_code_dispo,result, log=True)
        plt.show()

obj = Exercice3()
print(obj.pourcentage())
print(obj.frequence("841460"))
print(obj.graph_frequence(["841460", "640520"]))