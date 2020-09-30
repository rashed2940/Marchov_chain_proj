import numpy as np
import pandas as pd

# states of chain
STATES = ['spices', 'drinks', 'fruits', 'dairy', 'checkout']

# Transition matrix
p = {
    'checkout': [0.0, 0.0, 0.0, 0.0, 0.0],
    'dairy': [0.246056,	0.736919, 0.107341, 0.070119, 0.145906],
    'drinks': [0.282594, 0.005964, 0.598602, 0.067364, 0.134756],
    'fruit': [0.344479, 0.068696, 0.071869, 0.597072, 0.102899],
    'spices': [0.126871, 0.068246, 0.105285, 0.045251, 0.402198]
}

class Customer: 
    '''
    Customer for supermarket simulation.
    
    Parameters:
    -----------
    
    '''
    
    def __init__(self,customer_no):

        self.customer_no = customer_no
        self.state = 'dairy' 
        self.state_history = ['dairy']


    def change_location(self):
        '''
        Method of the Customer class to change the current_location.
        '''
        self.current_location = np.random.choice(STATES,1, p)[0]
    
    def __repr__(self):
        return f"The customer number {self.customer_no} is at {self.state}"


