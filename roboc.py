# -*-coding:Utf-8 -*

"""This file contains the Main Code."""

import os
from labyrinthe import *

Game_information = '''\nWelcome to Maze game.
To win, the player must reach the letter "U".
He can cross the dot "." and the empty space, but cannot cross the letter "O" which here represents a wall\n. 
The commands are as follows:\n
ni -> we move North
si -> we move South
wi -> we move West
ei -> we move East\n
i represents the number of moves.\n
Examples:\n
n1 we move one square north
s2 we move two squares south
w5 we move five squares west
e4 we move four squares east\n
The maze is only saved if you haven't won. You can continue next time.
You must choose a maze at the first start or after a victory.\n'''

print(Game_information)

Object_maze = Labyrinthe()
personnage = "X"
continue_game = 'y'
game_active = Object_maze.open_notfinishedgame()

while continue_game != 'n':
# we open a recorded maze if exist, if not we choose new one or exit the game.
  if game_active:
    chosen_maze = game_active.get(0)
    print("Recorded Maze was loaded.\n")
  else:
    osdirs = os.listdir (os.chdir('cartes')) 
    Object_maze.file = osdirs
    maze_list = (Object_maze.__repr__())
    print("Existing Maze :\n")
    print (maze_list)
    while True:
      try:
        maze_number = (input("choose a maze by tipping his number or Q to exit:"))
        if maze_number == "q":
          continue_game = "n"
          chosen_maze = ""
          break
        else:
          chosen_maze = Object_maze.read_maze(int(maze_number))
          os.chdir("..")
          break
      except IndexError:
        print("It's not a valid number")
      except ValueError:
        print("It's not an integer value")
      except Exception as e:
        print(f"An unexpected error occurred: {e}")

# The Maze is chosen
  if chosen_maze:        
    print (f"\n{chosen_maze}")
    command = ""
    while command == "" or (command[0] != "n" and command[0] != "s" and command[0] != "w" and command[0] != "e"):
      if command == "q":
        continue_game = "n"
        break
      else:
        command = str(input("\nEnter a valid command or Q to exit: "))      
        step = command[1:]
        if step == "":
          step = 1
        else:
          step = int(command[1:])
        coordinate_X, coordinate_Y = Object_maze.find_player_position(chosen_maze) 
        if command[0] == "n":
          new_player_position = Object_maze.move_player_north(step,coordinate_X,coordinate_Y,chosen_maze)           
        elif command[0] == "s":
          new_player_position = Object_maze.move_player_south(step,coordinate_X,coordinate_Y,chosen_maze)           
        elif command[0] == "w":
          new_player_position = Object_maze.move_player_west(step,coordinate_X,coordinate_Y,chosen_maze)           
        elif command[0] == "e":
          new_player_position = Object_maze.move_player_east(step,coordinate_X,coordinate_Y,chosen_maze)         
        else:
          new_player_position = chosen_maze

        print(f"\n{new_player_position}")                
        index_victory = Object_maze.verify_game_done(new_player_position)
        
        if index_victory != None:
          game_active[0] = new_player_position
          Object_maze.save_notfinishedgame(game_active)
          print("Maze is Recorded.\n")
        else:
          game_active = {}
          Object_maze.save_notfinishedgame(game_active)

        if command != "q":
          continue_game = input("\nDo you want to continue the game (Y/N) ?").lower()

print("\nGoodbye and see you next time\n")  