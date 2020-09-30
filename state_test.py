from customer_class import Customer
import numpy as np

def test(Nb_customers):
    """"
    This function test the trnsition matrix working steps.
    """
    

    for customer_id in range (Nb_customers):
        #Create new customer
        new_customer = Customer(customer_id)
        

        new_customer.change_location()
        states = new_customer.result
        
        print(states)

test(5)