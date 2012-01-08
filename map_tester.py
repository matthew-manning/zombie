import pygame
import map_class
import player_class

map_1 = map_class.map(100,100)
map_1.gen_map(20)
screen = pygame.display.set_mode((625,625))
player_1 = player_class.player()

map_1.spawn_player(player_1)



while 1:
    screen.fill((255,255,255))
    map_1.draw(player_1 , screen)
    pygame.display.flip()
    
    command =  raw_input("<-->")
    
    if command in ("n","ne","e","se","nw","s","sw","w","sw"):
        
        map_1.move_player(player_1, command)
    
        