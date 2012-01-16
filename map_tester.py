import pygame
import map_class
import player_class
import game_class 
import commands

game_1 = game_class.game()

monster_list = {21:player_class.zombie, 25:player_class.chest_armour_zombie}

game_1.new_map(100, 100, 16, monster_list, 7)

game_1.new_screen(625,625)

game_1.player.weapons = ["claws","tester melee"]


while 1:
    game_1.screen.fill((255,255,255))
    game_1.draw()
    pygame.display.flip()
    
    command =  raw_input("<-->")
    
    if command == "quit":
        print "quiting...."
        break
    
    commands.commands(game_1, command)
    
        