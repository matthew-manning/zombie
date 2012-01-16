import pygame

item_images = {"chest":pygame.image.load("graphics/chest_armour.png")}


def put_on_chest(creture):
    
    if creture.armour["chest"] == False:
        #if not already wearing chest armour
        
        creture.armour["chest"] = True
        creture.armour_val -= 1/8
        creture.rugg_points +=1
        
def remove_chest(creture):
    
    creture.armour["chest"] = False
    creture.armour_val += 1/8
    creture.take_damage(1)
    #^removing chest armour can be fatal


