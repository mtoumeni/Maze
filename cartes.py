# -*-coding:Utf-8 -*

"""This module contains the Class Carte."""

import os 

class Carte:

    """Object transition between a file and a maze."""

    def __init__(self, my_liste = [] ):

        if type(my_liste) not in (list, Carte):
            raise TypeError( \
                " The Typ is not a list ")
        self.file = my_liste
        

    def __repr__(self):
        chaine = ""
        for i, elt in enumerate(self.file):
           chaine += "{} - {} \n".format(i+1,elt)
           chaine = chaine.replace("txt","")
        return chaine

    def read_maze(self,index):
       for elt in(self.file):
          with open(self.file[index-1], 'r') as self.file[index-1]:
              maze = self.file[index-1].read()
              return maze