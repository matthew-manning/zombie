import map_class
import player_class
import weapons_and_combat
import misc_fun

recognized_command_ids = ("n","ne","e","se","nw","s","sw","w","sw","atk")

    
def commands(map_in, player_in, command):
    #command is str
    
    command_id = misc_fun.get_until_space(command)
    #the first part ie sw,attack,swap, etc
    
    if command_id in recognized_command_ids:
        #if command exists
        
        ####################################################################movement
        if command_id in ("nw","n","ne","e","se","s","sw","w"):
            #if command is movement
            
            distance = misc_fun.get_until_space(command, len(command_id)+1)
            
            if distance == "":
                    distance = "1"
            
            if misc_fun.check_int(distance):
                
                    #distance defualts to 1
                    
                distance = int(distance)
                #if the distance is int not float or char
                map_in.move_player(player_in, command_id, distance)
                
        ###################################################################attacking
        elif command_id == "atk":
            ###
            print 'inside if command_id == "attack" '##debug
            
            weapon_used = command[4]
            target_square = misc_fun.get_until_space(command,6)
            
            if ( weapon_used in ("1", "2") ) and (misc_fun.check_letters(target_square[0])) and (misc_fun.check_int(target_square[1:])):
                
                print "inside if weapon used == 1 or 2 , etc"#debug
                weapon_used = int(weapon_used)-1
                #-1 convets to indexing int
                
                weapons_and_combat.attack(player_in, target_square, weapon_used, map_in)   

        ########################################################################################  
    else:
        print"???unrecognized command!"
    