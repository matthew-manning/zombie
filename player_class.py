import pygame


class player():
    avatar = pygame.image.load("graphics/player.png")
    
    
    def __init__(self):
        
        self.pos_x = None
        self.pos_y = None
        self.max_speed = 4
        self.move_left = self.max_speed
        
        
        

class zombie():
    avatar_list = pygame.image.load("graphics/zombie_1.png")
    max_speed = 3
    
    def __init__():
        
        avatar_num = random.randint(0, len(self.avatar_list))
        self.avatar = [avatar_num]
        
        self.rugg_points = 4
        self.move_left = self.max_speed
        self.pos_x = 0
        self.pos_y = 0
    
    
    
    
    