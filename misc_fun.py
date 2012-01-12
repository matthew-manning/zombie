def get_until_space(string, start = 0):
    """returns part of string until first white space"""
    
    string = string[start:]#removes stuff before the start
    return_string = ""
    
    for i in string:
        if i == " ":
            #if a space
            return return_string
        else:
            return_string += i
    
    return return_string

#######################################3

def check_int(string):
    """takes a string and checks it is an intger, with no spaces"""
    for i in string:
        if i not in ("1","2","3","4","5","6","7","8","9","0",):
            
            return False
    
    if string == "":
        #if empty
        return False
    
    return True

#######################################
def check_letters(string):
    """takes a string and checks it is letters, with no spaces"""
    for i in string:
        if i not in ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t",
                       "u","v","w","x","y"):
            
            return False
    
    if string == "":
        #if empty
        return False
    
    return True