import random
import pygame
from seg_array_class import *
import copy

class square():
    normal_img = pygame.image.load("graphics/open.png")
    impass_img = pygame.image.load("graphics/wall.png")
    
    def __init__(self, passable):
        
        self.passable = passable#Bool
        self.creture = None
        self.item = None

class map():
    map_img_base = pygame.image.load("graphics/map_base_image.png")#numbers and letters along side and top
    
    def __init__(self, size_x = 25, size_y = 25, player = None):
        self.size_x = size_x
        self.size_y = size_y
        self.scroll_x = 0
        self.scroll_y = 0
        
        self.player = player
        self.cretures = []#exquedes player and items
        
        if self.size_y < 25:
            self.size_y = 25
        if self.size_x < 25:
            self.size_x = 25##makes the map at least 25x25
        
        self.squares = seg_array(self.size_x, self.size_y)
        

    def gen_map(self, wall_prob, monster_list, monster_prob):
        ##wall prob int from 0 to 100
        
        for x in range(0, self.size_x):
            for y in range(0, self.size_y):
            
                if random.randint(0,100 ) <= wall_prob:
                    #if square is impassable
                    self.squares.set_val( x, y, square(False) )
                else:
                    #normal square
                    self.squares.set_val( x, y, square(True) )
                    
                    #monster spawning
                    if random.randint(0,100) <= monster_prob:
                        #if a monster spawns
                        monster_index = random.randint(0,len(monster_list)-1)
                        #choosing which monster to spawn, weight this some time soonish
                        spawn_square = self.squares.get_val( x, y)
                        spawn_square.creture = monster_list[monster_index](x,y)
                        
                
                
    def draw(self, player, screen):
        
        screen.blit(self.map_img_base, (0,0))
        

        for x in range(0,25):
            for y in range(0,25):
                
                
                current_square = self.squares.get_val(x+self.scroll_x, y+self.scroll_y)
                
                if not current_square.passable:
                    #wall
                    screen.blit(square.impass_img, (25 + 25 * x, 25 + 25 * y ))
        
                else:
                    #open
                    screen.blit(square.normal_img, (25 + 25 * x, 25 + 25 * y ))
                    
                if current_square.creture:
                    #if creture != None
                    screen.blit(current_square.creture.avatar, (25 + 25 * x, 25 + 25 * y ))

                
    
    def spawn_player(self, player):
            
            for x in range(1, self.size_x) :
                for y in range(1, self.size_y):
                    
                    current_square = self.squares.get_val(x,y)
                    
                    if current_square.passable:
                        current_square.creture = player
                    
                        player.pos_x = x
                        player.pos_y = y
                                  

                        self.scroll_x = x - 12
                        self.scroll_y =y - 12
                        
                        if self.scroll_x < 0:
                            self.scroll_x = 0
                        if self.scroll_y < 0:
                            self.scroll_y = 0
                        return "player spawned"
            
            return "no place for player"
                              
            
    def move_creture(self, creture, heading):
        ##creture and players use this function
        
        heading_to_displace = {"n":(0, -1), "ne":(1,-1), "e":(1,0), "se":(1,1),"s":(0,1),
                                "sw":(-1,1),"w":(-1,0),"nw":(-1,-1)}
        
        disp_x = heading_to_displace[heading][0]#x displacement
        disp_y = heading_to_displace[heading][1]#y displacement
        
        new_x = creture.pos_x + disp_x
        new_y = creture.pos_y + disp_y
        
        #################makes sure the creture does not move off the map 
        if (new_x < 0) or (new_x > self.size_x) or (new_y < 0) or (new_y > self.size_y):
            return "failed"
        #################   
        
        new_square = self.squares.get_val(new_x, new_y)
        
        
        if (new_square.passable) and (new_square.creture == None ):
            #if open and no creture on square
            
            new_square.creture = creture
            #places creture on new square
            
            old_square = self.squares.get_val(creture.pos_x, creture.pos_y)
            old_square.creture = None
            #removes creture from old square
            
            creture.pos_x += disp_x
            creture.pos_y += disp_y
            #changes the creture's pos x and y
            
            return "okay"
        
        else:
            #if blocked
            print(heading, " blocked")##replace with on screen pomt printout
            
            return "failed"
        
    
    def move_player(self, player, heading, distance = 1):
        
        if distance < 0:
            return "failed"
        
        
        while distance >= 1:
            return_val = self.move_creture( player, heading)
            distance -= 1
            
            if return_val == "failed":
                break
        
        self.scroll_x = player.pos_x -12##scroll still broken
        self.scroll_y = new_y = player.pos_y -12
        
        
        if self.scroll_x < 0:
            self.scroll_x = 0
        if self.scroll_y < 0:
            self.scroll_y = 0
        
        print "player pos is ",player.pos_x,", ",player.pos_y#debug
        print "scroll is ", self.scroll_x,", ",self.scroll_y#debug
    
    