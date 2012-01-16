import random
import map_class
import seg_array_class

def d12():
    return random.randint(1,12)

weapon_dict = {
    "pickaxe":{"range":'touch', "power":lambda: random.randint(0,6)-1,"accuracy":2, "shots":1,"AP":2/8, "special":[]}
    ,"claws":{"range":'touch', "power":lambda: random.randint(0,4)-1,"accuracy":1, "shots":1,"AP":0, "special":[]}
    ,"tester melee":{"range":'touch', "power":lambda: 30,"accuracy":9, "shots":1,"AP":2/8, "special":[]}
    #tester is not game weapon JUST for testing
}

letter_to_x = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,
               "m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25}

def attack(attacker, target_square, weapon, map_in):
    #target square is str<"d5">, weapon is int 0 or 1
    
    
    if weapon_dict[ attacker.weapons[weapon] ]["range"] == "touch":
        #if cc weapon
        
        disp_x = letter_to_x[ target_square[0:1] ]
        #slices off the letter and indexs letter_to_x
        disp_y = int(target_square[1:])
        #remove the letter and converts to intger
        
        target_x = disp_x + map_in.scroll_x - 1
        target_y = disp_y + map_in.scroll_y - 1
        
        target_creture = map_in.squares.get_val(target_x,target_y).creture
        
        if target_creture == None:
            print "target square empty!"
            return 0
        
        
        
        if target_x - attacker.pos_x in (1, -1, 0) and target_y - attacker.pos_y in (1, -1, 0):
            #if within one
            shots_left = weapon_dict[ attacker.weapons[weapon] ]["shots"]
            
            while shots_left > 0:
                attack_melee(attacker, attacker.weapons[weapon] ,target_creture, map_in)
                shots_left -= 1
        else:
            print "out of range"
        

def attack_melee(attacker, weapon ,target, map_in):
    ##just resovles the attack does not check it's validility
    
    print "swinging ",weapon,"...."
    
    modifier = 0
    
    if target.cc/2 >= attacker.cc:
        modifier -=1
    #if target's cc is twice that of attacker
    
    if target.armour["shield"] == ("shield" or "buckler"):
        modifier -= 1
    #if target has a sheild
    
    roll = d12()
    
    if roll <= attacker.cc+modifier +weapon_dict[weapon]["accuracy"]:
        #if attack hit
        
        hit_type = "normal"
        
        if roll == 1:
            hit_type = "critcal hit"
        
        target_effective_armour = target.armour_val+ weapon_dict[weapon]["AP"]
        
        if target.armour["shield"]:
            target_effective_armour -= 1/8
        
        damage = (attacker.strength + weapon_dict[weapon]["power"]() )*target_effective_armour
        #(str + power)*armour
        
        if hit_type == "critcal hit":
            damage_2 = (attacker.strength + weapon_dict[weapon]["power"]() )*target_effective_armour
        
            print "critcal hit!"
            if damage_2 > damage:
                damage = damage_2
            
        print int(damage)," damage!"
        target.take_damage(damage, map_in)
    else:
        print "miss!"