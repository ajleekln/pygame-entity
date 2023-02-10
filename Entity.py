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
        self.__surface = pygame.Surface((1,1)) # surface or image to be displayed
        self.__rect = self.__surface.get_rect(topleft = self.movement.get_pos())

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
        self.__rect.update(self.movement.get_pos(), self.__surface.get_size()) # updating position and size of surface or image
    
    def draw(self, screen): # DRAWING TO SCREEN
        """
        draws entity to a given screen 
        """
        #screen.blit(self.__surface, self.__rect)
        pass
