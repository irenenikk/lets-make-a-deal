import numpy as np
import random

class Agent:
    # learning rate
    alpha = 0.3

    def __init__(self):
        # there is only one state, so the table is one dimensional
        # 0 = don't switch, 1 = switch
        if (self.alpha > 1 or self.alpha <= 0):
            raise ValueError('The learning rate should be between zero and one')
        self.Q_table = np.zeros(2)
    
    def choose_initial_door(self):
        return random.randint(0, 2)
    
    def choose_if_switch(self):
        return np.argmax(self.Q_table)

    def update_Q_table(self, action, reward):
        old_q_value = self.Q_table[action]
        # there is only one state, so no need to consider the future states
        self.Q_table[action] = (1-self.alpha)*old_q_value + self.alpha*reward
