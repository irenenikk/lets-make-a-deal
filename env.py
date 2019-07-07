import numpy as np
import random

class Env:

    def __init__(self):
        # place the car
        self.car_index = random.randint(0, 2)
    
    def open_door(self, initial_index, switch):
        # if the player switches, then they win if the original index was a goat
        # since Monty has opened a door with a goat in between
        if switch:
            return 0 if initial_index == self.car_index else 100
        else:
            return 100 if initial_index == self.car_index else 0


