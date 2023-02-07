import Direction as dr
import Movement as mv
import pygame 



class Entity:
    """
    A class to be used by PyPage in order to record propeties of events in a single location  
    """
    def __init__(self):
        self.__events = []
        self.__mouse = None
        self.movement = mv.Movement()
        self.direction = dr.Direction()
        
        
        self.__surface = pygame.Rect(self.movement.get_pos(), (1, 1)) # surface or image to be displayed
        """
        ENTITY PROPERTIES THAT MUST BE CARRIED THROUGHOUT FOR PYPAGE CONSISTENCY
        - position
        - size 
        """
        
        """
        ENNTITY FUNCTIONS TO FULFILL SIMPLICITY AMONGST INTERACTION 
        - scale size  (percentage based increase of size)
        - move 
        """
    def get_mouse(self, mouse = None):
        """
        Updates mouse properties if given a value
        Returns mouse properties 
        """
        if mouse != None:
            self.__mouse = mouse
        return self.__mouse
        
    def get_events(self, events = None): # GETTING EVENTS 
        """
        Updates events if given a value. 
        Returns events
        """
        if events != None :
            self.__events = events
        return self.__events
    
    def update(self): # UPDATE BASED ON SELF AND EVENTS
        """
        Updates entity 
        """
        self.movement.update()
        self.__surface.update(self.movement.get_pos(), (1,1)) # updating position and size of surface or image
    
    def draw(self, screen): # DRAWING TO SCREEN
        """
        draws entity to a given screen 
        """
        #screen.blit(self.__surface, imagerect)
        pass
