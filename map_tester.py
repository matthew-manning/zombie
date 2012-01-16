import pygame
import map_class
import player_class
import commands

map_1 = map_class.map(100,100)

monster_list = {21:player_class.zombie, 25:player_class.chest_armour_zombie}
map_1.gen_map(1, monster_list, 3)

screen = pygame.display.set_mode((625,625))
player_1 = player_class.player()

map_1.spawn_player(player_1)
player_1.weapons = ["claws","tester melee"]


while 1:
    screen.fill((255,255,255))
    map_1.draw(player_1 , screen)
    pygame.display.flip()
    
    command =  raw_input("<-->")
    
    if command == "quit":
        print "quiting...."
        break
    
    commands.commands(map_1, player_1, command)
    
        