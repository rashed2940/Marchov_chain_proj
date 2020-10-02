import numpy as np
import pandas as pd
import random

# states of chain
STATES = ['spices', 'drinks', 'fruits', 'dairy', 'checkout']

# Transition matrix
p = {
    'entrance': [0.25, 0.25, 0.25, 0.25 , 0.0],
    'dairy':  [0.102678, 0.736919, 0.058737, 0.050129, 0.051536],
    'drinks': [0.215505, 0.010899, 0.598602, 0.088012, 0.086983],
    'fruits':  [0.201054, 0.096081, 0.055005, 0.597025, 0.050834],
    'spices': [0.149888, 0.193214, 0.163109, 0.091590, 0.402198]
}

class Customer: 
    '''
    Customer for supermarket simulation.
    
    Parameters:
    -----------
    
    '''
    
    def __init__(self,customer_id):
        self.customer_id = customer_id
        self.current_location = 'entrance' 
        self.result = ['entrance']


    def change_location(self):

        '''
        Method of the Customer class to change the current_location.
        '''

        while self.current_location != 'checkout':

            # predict the next move
            
            # self.current_location = random.choices(STATES,1, p[self.current_location])[0]
            self.current_location = random.choices(STATES,k=1, weights=p[self.current_location])[0]
            self.result.append(self.current_location)
                

    # print(self.result)
    
    def __repr__(self):
        return f"The customer number {self.customer_id} is at {self.current_location}"


