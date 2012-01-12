import pygame
import random


class player():
    avatar = pygame.image.load("graphics/player.png")
    
    
    def __init__(self):
        
        self.pos_x = None
        self.pos_y = None
        self.max_speed = 4
        self.move_left = self.max_speed
        
        self.rugg_points = 12
        
        self.cc = 3
        self.strength = 2
        
        self.armour = {"chest":False, "halmet":False, "legs":False, "shield":None}
        self.weapons = ["claws","claws"]#just the str, "pistol" or "axe" 
        
        
        

class zombie():
    avatar_list = [pygame.image.load("graphics/zombie_1.png")]
    max_speed = 3
    cc = 1
    
    def __init__(self,x,y):
        
        avatar_num = random.randint(0, len(self.avatar_list)-1)
        self.avatar = self.avatar_list[avatar_num]
        
        self.rugg_points = 4
        self.move_left = self.max_speed
        self.armour = {"chest":False, "halmet":False, "legs":False, "shield":None}
        self.weapons = []#just the str, "pistol" or "axe" 
        self.pos_x = x
        self.pos_y = y
        self.drop = None
        
    def take_damage(self, amount, map_on):
        self.rugg_points -= amount
        
        if self.rugg_points < 0:
            #if die
            
            
            square_occupied = map_on.squares.get_val(self.pos_x, self.pos_y)
           # print "square's creture is ",square_occupied.creture##debug line
            
           # print "self is ",self
            square_occupied.item = self.drop
            square_occupied.creture = None
            print "zombie dies!"
    
    
    
    
    