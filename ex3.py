from logging import log
import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import matplotlib.pyplot as plt


class Exercice3:

    def __init__(self):
        
  
        self.code_dispo=pd.read_csv("data/codes disponibles.csv")
        self.tous_code=pd.read_csv("data/tous les codes.csv")

           

    def pourcentage(self):
        """
        Le pourcentage des codes disponibles par rapport à tous les codes.
        """
        sum_code_dispo=np.sum(self.code_dispo.values.tolist())
        sum_tous_code=np.sum(self.tous_code.values.tolist())
        return (sum_code_dispo/sum_tous_code)*100
    

    def frequence(self,code):
        """
        la fréquence d’un code disponible donné.
        """
        occ_code=self.tous_code[self.tous_code["codes"]==code ].count()[0]
        total_code=self.tous_code.count()[0]
        return occ_code/total_code


    def graphe_frequence(self, list_code_dispo):
        """
        Afficher les code disponibles et leurs fréquence dans un graphe (barplot)
        """
        result=[]
        for code in list_code_dispo:
            result.append(self.frequence(code))
    
        fig = plt.figure()
        ax = fig.add_subplot()
        ax.bar([str(x) for x in list_code_dispo],result, log=True)
        plt.show()

    def graphe_describe(self):
        """
        Afficher dans un graphique le maximum, minimum, médiane, et la moyenne des fréquences des codes disponibles.
        """
        result=[]
        for code in self.code_dispo:
            result.append(self.frequence(code))
        result = pd.DataFrame(result)
        
        # describe(): afficher la moyenne, la médiane, le min et le max des fréquences des codes
        print(result.describe())

        fig1, ax1 = plt.subplots()
        ax1.boxplot(result)
        plt.show()
    






