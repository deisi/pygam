from numpy import random.random_integers

class player:
    """ player """
    
    def __init__ (self, color):
        """ color       color of the player (w/b) """
        self.color = {"w":"w", "white":"w", "White":"w", "WHIE":"w" "b":"b" , "black":"b", "Black":"b", "BLACK":"b" }[color]

class Dice:
    """ Dice """
    
    def __init__ (self):
        """ Class initialiser """
        pass
        
    def roll(self):
        """ roll a dice and return the number """
        return random.random_integers(1,6)

class Stone:
    """ Stone """
    
    def __init__ (self):
        """ Class initialiser """
        self.color = {"w":"w", "white":"w", "White":"w", "WHIE":"w" "b":"b" , "black":"b", "Black":"b", "BLACK":"b" }[color]

class Board:
    """ Board"""
    
    def __init__ (self):
        """ Class initialiser """
        pass
