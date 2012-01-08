

class seg_array():
    
    def __init__(self, size_x, size_y):
        
        #size x,y start at 0
        
        self.size_x = size_x
        self.size_y = size_y
        self.array = []#acuctal data in this

        i = size_x*size_y
        
        while i >= 1:
            self.array.append(None)
            i -=1
            
        
    def get_val(self, pos_x, pos_y):
        
        if (pos_x <= self.size_x) and (pos_y <= self.size_y):
            
            return self.array[pos_y * self.size_x + pos_x]
        else:
            return ("index out of range")
    
    def set_val(self, pos_x, pos_y, val):
        
        if (pos_x <= self.size_x) and (pos_y <= self.size_y):
            
            self.array[pos_y * self.size_x + pos_x] = val
        else:
            return ("index out of range")
        
        
        