
import os
import cv2
import glob
import imageio
import numpy as np
from customer_class import Customer
from matplotlib import pyplot as plt



def save_predicted_state(Nb_customers):
    """"
    This function calculate and save all the trnsition states
    for a customer and save this as a png file.
    """

    for customer_id in range (Nb_customers):
        
        #Create new customer
        new_customer = Customer(customer_id)
        #Assign a random colour
        color = list(np.random.choice(range(256), size=3))


        new_customer.change_location()
        states = new_customer.result
        print(states)

        for s_nb,s in enumerate(states):

            #Read the market picture to plot the customer position at each state
            frame = cv2.imread('./images/market.png')

            if s == 'entrance':
                frame[550:640, 730:820] = color
            elif s == 'checkout':
                frame[590:680, 205:295] = color
            elif s == 'dairy':
                frame[220:310, 310:400] = color
            elif s == 'drinks':
                frame[220:310, 80:170] = color
            elif s == 'fruits':
                frame[220:310, 770:860] = color
            elif s == 'spices':
                frame[220:310, 540:630] = color
            else:
                print('This state is not there')

            plt.figure(figsize=(8,5))
            plt.imshow(frame)
            #Save all states to disk
            plt.savefig(f'./tmp/customer_{customer_id}_states_{s_nb}.png')
            plt.close()

def gif_from_states(Nb_customers):
    """
    This function collects all the states of each customer's png file
    and remove them after creating a gif file.
    """
    image_directory = './tmp'

    list_of_images=[]

    for customer_id in range (Nb_customers):
        path_to_read = os.path.join(image_directory,f'customer_{customer_id}_*.png')
        files = glob.glob(path_to_read)
        files.sort(key=os.path.getmtime)
        for f in files:
            im = imageio.imread(f)
            list_of_images.append(im)
            os.remove(f)

    imageio.mimsave(f'./tmp/customer_simulation.gif', list_of_images, duration = .75)


save_predicted_state(5)    
gif_from_states(5)