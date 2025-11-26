# -*-coding:Utf-8 -*

"""This module contains Class Labyrinthe."""

import os
import pickle

from cartes import *

class Labyrinthe (Carte):
    def __init__(self, gateway = ".", wall = "O",victory = "U",player = "X",empty = " "):
        Carte.__init__(self, my_liste = [])
        self.gateway = gateway
        self.wall = wall
        self.victory = victory
        self.player = player
        self.empty = empty
        self.index_pos_element = []
        self.NotFinishedGame_game_file = {}

    """check if the symbol "U" is always available in the Maze."""

    def verify_game_done(self, chaine):
       labyrinthe_en_liste = chaine.split("\n")
       for ligne in labyrinthe_en_liste:
          for index_case, case in enumerate(ligne):
             if case == "U":
               return index_case

    def find_player_position(self,chaine):
      labyrinthe_en_liste = chaine.split("\n")
      for index_ligne, ligne in enumerate(labyrinthe_en_liste):
        for index_case, case in enumerate(ligne):
            if case == self.player:
              return index_ligne, index_case
    
    """Update new player position after moving in North/South direction."""
            
    def update_new_player_position_NS(self,chaine,index_j, index_i):
      chaine = list(chaine)
      if chaine[index_j] == self.gateway:
        self.index_pos_element.append(index_i)
      chaine[index_j] = self.player
      return self.index_pos_element, "".join(chaine)
    
    """Update old player position after moving in North/South direction."""
      
    def update_old_player_position_NS(self,chaine,index,index_pos_element,index_i):
      chaine = list(chaine)
      if index_i not in index_pos_element:
        chaine[index] = self.empty
      else:
        chaine[index] = self.gateway
      return "".join(chaine)
    
    """Update new player position after moving in West/East direction."""
    
    def update_new_player_position_WE(self,chaine,index_j):
      chaine = list(chaine)
      if chaine[index_j] == self.gateway:
        self.index_pos_element.append(index_j)
      chaine[index_j] = self.player
      return self.index_pos_element, "".join(chaine)
    
    """Update old player position after moving in West/East direction."""
      
    def update_old_player_position_WE(self,chaine,index_j,index_pos_element):
      chaine = list(chaine)
      if index_j not in index_pos_element:
        chaine[index_j] = self.empty
      else:
        chaine[index_j] = self.gateway
      return "".join(chaine)
    
    """Move in the North direction."""
                
    def move_player_north(self,step,i,j,chaine):
       index = i - step
       labyrinthe_en_liste = chaine.split("\n")
       if (index <0):
          print("Invalid command.\n")
       else:
        while i > index:
          i -= 1
          if labyrinthe_en_liste[i][j] != self.wall:
            if labyrinthe_en_liste[i][j] == self.victory:
              index_pos_element,labyrinthe_en_liste[i] = self.update_new_player_position_NS(labyrinthe_en_liste[i],j,i)
              labyrinthe_en_liste[i+1] = self.update_old_player_position_NS(labyrinthe_en_liste[i+1],j,index_pos_element,i+1)
              print("Congratulation ! you won the game !\n")
              break
            if labyrinthe_en_liste[i][j] == self.gateway or labyrinthe_en_liste[i][j] == self.empty:
              index_pos_element,labyrinthe_en_liste[i] = self.update_new_player_position_NS(labyrinthe_en_liste[i],j,i)
              labyrinthe_en_liste[i+1] = self.update_old_player_position_NS(labyrinthe_en_liste[i+1],j,index_pos_element,i+1)
          else:
            print("Moving not possible due to a wall.\n")
            break
       return "\n".join(labyrinthe_en_liste)

    """Move in the South direction."""
    
    def move_player_south(self,step,i,j,chaine):
       index = i + step
       labyrinthe_en_liste = chaine.split("\n")
       if (index >= len(labyrinthe_en_liste)):
          print("Invalid command.\n")
       else:
        while i < index:
          i +=1        
          if labyrinthe_en_liste[i][j] != self.wall:
            if labyrinthe_en_liste[i][j] == self.victory:
              index_pos_element,labyrinthe_en_liste[i] = self.update_new_player_position_NS(labyrinthe_en_liste[i],j,i)
              labyrinthe_en_liste[i-1] = self.update_old_player_position_NS(labyrinthe_en_liste[i-1],j,index_pos_element,i-1)
              print("Congratulation ! you won the game !\n")
              break
            if labyrinthe_en_liste[i][j] == self.gateway or labyrinthe_en_liste[i][j] == self.empty:
              index_pos_element,labyrinthe_en_liste[i] = self.update_new_player_position_NS(labyrinthe_en_liste[i],j,i)
              labyrinthe_en_liste[i-1] = self.update_old_player_position_NS(labyrinthe_en_liste[i-1],j,index_pos_element,i-1)
          else:
            print("Moving not possible due to a wall.\n")
            break
       return "\n".join(labyrinthe_en_liste)
    
    """Move in the West direction."""
    
    def move_player_west(self,step,i,j,chaine):
       index = j - step
       labyrinthe_en_liste = chaine.split("\n")
       if (index <0):
          print("Invalid command.\n")
       else:
        while j > index:
          j -=1
          if labyrinthe_en_liste[i][j] != self.wall:
            if labyrinthe_en_liste[i][j] == self.victory:
              index_pos_element,labyrinthe_en_liste[i] = self.update_new_player_position_WE(labyrinthe_en_liste[i],j)
              labyrinthe_en_liste[i] = self.update_old_player_position_WE(labyrinthe_en_liste[i],j+1,index_pos_element)
              print("Congratulation ! you won the game !\n")
              break
            if labyrinthe_en_liste[i][j] == self.gateway or labyrinthe_en_liste[i][j] == self.empty:
              index_pos_element,labyrinthe_en_liste[i] = self.update_new_player_position_WE(labyrinthe_en_liste[i],j)
              labyrinthe_en_liste[i] = self.update_old_player_position_WE(labyrinthe_en_liste[i],j+1,index_pos_element)
          else:
            print("Moving not possible due to a wall.\n")
            break
       return "\n".join(labyrinthe_en_liste)
    
    """Move in the East direction."""
    
    def move_player_east(self,step,i,j,chaine):
       index = j + step
       labyrinthe_en_liste = chaine.split("\n")
       if (index >= len(labyrinthe_en_liste[i])):
          print("Invalid command.\n")
       else:
        while j < index:
          j +=1
          if labyrinthe_en_liste[i][j] != self.wall:
            if labyrinthe_en_liste[i][j] == self.victory:
              index_pos_element,labyrinthe_en_liste[i] = self.update_new_player_position_WE(labyrinthe_en_liste[i],j)
              labyrinthe_en_liste[i] = self.update_old_player_position_WE(labyrinthe_en_liste[i],j-1,index_pos_element)
              print("Congratulation ! you won the game !\n")
              break
            if labyrinthe_en_liste[i][j] == self.gateway or labyrinthe_en_liste[i][j] == self.empty:
              index_pos_element,labyrinthe_en_liste[i] = self.update_new_player_position_WE(labyrinthe_en_liste[i],j)
              labyrinthe_en_liste[i] = self.update_old_player_position_WE(labyrinthe_en_liste[i],j-1,index_pos_element)
          else:
            print("Moving not possible due to a wall.\n")
            break
       return "\n".join(labyrinthe_en_liste)     

    """create new or open existing file for not finished game

      Returns:
          list: NotFinishedGame_game_file
    """
    def open_notfinishedgame(self):
       try:
           with open('NotFinishedGame', 'rb') as NotFinishedGame:
               NotFinishedGame.read()
       except IOError:               
                      with open('NotFinishedGame', 'wb') as NotFinishedGame:
                          my_pickler = pickle.Pickler(NotFinishedGame)
                          my_pickler.dump(self.NotFinishedGame_game_file)
       else:
            if os.path.getsize("./NotFinishedGame") > 0: 
              with open('NotFinishedGame', 'rb') as NotFinishedGame:
                  my_depickler = pickle.Unpickler(NotFinishedGame)
                  self.NotFinishedGame_game_file = my_depickler.load()
       return self.NotFinishedGame_game_file

    """save not finished game in the file."""
    
    def save_notfinishedgame(self, NotFinishedGame_game_file):        
       if os.path.getsize("./NotFinishedGame") > 0: 
         with open('NotFinishedGame', 'wb') as NotFinishedGame:
             my_pickler = pickle.Pickler(NotFinishedGame)
             my_pickler.dump(NotFinishedGame_game_file)
