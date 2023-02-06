# Direction

class Direction:
    
    def __init__(self, up = False, down = False, left = False, right = False):
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        
        self.__compas = ""
        self.__lateral = ""
        self.__direction_2D = True # right = False/left = True
    
    def get_direction_2D (self):
        return self.__direction_2D
    
    def update_direction_2D (self):
        if self.left:
            self.__direction_2D = True
        if self.right:
            self.__direction_2D = False
            
        return self.__direction_2D
            
    def get_lateral_int (self):
    
        if self.get_lateral() == "LEFT":
            return -1
        elif self.get_lateral() == "RIGHT":
            return 1
        else:
            return 0
    def get_lateral (self):
        old = self.__lateral[:]
        self.__lateral = ""        
        if self.left:
            self.__lateral = "LEFT"
        if self.right:
            self.__lateral = "RIGHT"
            
        if self.__lateral == "":
            self.__lateral = old
        
        return self.__lateral        
    
    def get_compas(self):
        old = self.__compas[:]
        self.__compas = ""
        if self.up ^ self.down:
            if self.up:
                self.__compas = "NORTH"
            if self.down:
                self.__compas = "SOUTH"
        if self.left ^ self.right:
            if self.left:
                self.__compas += "WEST"
            if self.right:
                self.__compas += "EAST"
            
        if self.__compas == "":
            self.__compas = old
        return self.__compas
    
    def integer_value(self):
        x = 0 
        y = 0
        
        if self.up:
            y += -1
        if self.down:
            y += 1
        if self.left:
            x += -1
        if self.right:
            x += 1
            
        return (x,y)
    def is_directionless(self):
        return not  any([self.up,self.down,self.left,self.right])
    def reset(self):
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        