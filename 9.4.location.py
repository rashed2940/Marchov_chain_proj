import numpy as np
import pandas as pd
import cv2

OFS = 32
TILE_SIZE = 32

class Location:

    def __init__(self, name, x, y, n_customers=0):
        # set attributes of the class
        # name : string, for debugging
        # x : x-position of the location
        # y : y-position of the location
        # n_customers currently in that location
        self.name = name
        self.x = x
        self.y = y
        self.n_customers = n_customers
        self.image = np.zeros((32 , 32 , 3), dtype=np.uint8)


    def __repr__(self):
        """return a string, good for debugging."""
        ...

    def draw(self, frame, offset=OFS):
        """
        draws the image into a frame
        offset pixels from the top left corner
        """

        # for n in range(1,5,1):
        for customer in range(self.n_customers):
            # frame[OFS:OFS+self.y, OFS:OFS+self.x] = self.image
            frame[self.y:OFS+self.y, self.x:OFS+self.x] = self.image
        return frame


img = cv2.imread('supermarket.png')
spices = Location('spices', 3*32, 3*32)
dairy = Location('dairy', 5*32, 6*32)

while True:
    frame = img.copy()
    spices.n_customers = 1
    dairy.n_customers =1
    frame = spices.draw(frame)
    frame = dairy.draw(frame)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()