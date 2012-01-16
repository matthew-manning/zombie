import map_class
import pygame
import player_class

class game():
    
    def __init__(self):
        self.map_data = None
        self.screen = None
        self.player = None
        self.cretures = []
    
    def new_map(self, size_x, size_y, wall_prob, monster_list, monster_prob):
        self.map_data = map_class.map(size_x, size_y)
        
        self.map_data.gen_map(wall_prob, monster_list, monster_prob, self)
        
        ###############
        new_player = player_class.player()
        self.map_data.spawn_player(new_player)
        self.player = new_player
        ###############
        
        
    def new_screen(self, size_x, size_y):
        self.screen = pygame.display.set_mode((size_x, size_y))
        
    def draw(self):
        
        self.map_data.draw( self.player, self.screen )
        
    