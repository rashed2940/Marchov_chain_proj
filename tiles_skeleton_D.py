
import numpy as np
import cv2


TILE_SIZE = 32
OFS = 50

MARKET = """
##################
##..............##
##..ss..ss..ss..##
##..##..#o..##..##
##..e#..#r..#d..##
##..e#..#r..#d..##
##..e#..#b..#d..##
##...............#
##..C#..C#..C#...#
##..##..##..#h...#
##...............#
##############GG##
""".strip()


class SupermarketMap:
    """Visualizes the supermarket background"""

    def __init__(self, layout, tiles):
        """
        layout : a string with each character representing a tile
        tile   : a numpy array containing the tile image
        """
        self.tiles = tiles
        self.contents = [list(row) for row in layout.split('\n')]
        self.xsize =  len(self.contents[0])
        self.ysize = len(self.contents)
        self.image = np.zeros((self.ysize * TILE_SIZE, self.xsize * TILE_SIZE,3), dtype=np.uint8)
        self.prepare_map()

    def get_tile(self, char):
        """returns the array for a given tile character"""
        if char == '#':
            return self.tiles[0:32, 0:32]
        elif char == 'G':
            return self.tiles[7*32:8*32, 3*32:4*32]
        elif char == 'C':
            return self.tiles[2*32:3*32, 8*32:9*32]
        elif char == 'd':
            return self.tiles[3*32:4*32, 13*32:14*32]
        elif char == 'b':
            return self.tiles[0*32:1*32, 4*32:5*32]
        elif char == 'o':
            return self.tiles[1*32:2*32, 4*32:5*32]
        elif char == 'r':
            return self.tiles[4*32:5*32, 4*32:5*32]
        elif char == 's':
            return self.tiles[5*32:6*32, 9*32:10*32]
        elif char == 'e':
            return self.tiles[7*32:8*32, 11*32:12*32]
        else:
            return self.tiles[32:64, 64:96]

    def prepare_map(self):
        """prepares the entire image as a big numpy array"""
        for y, row in enumerate(self.contents):
            for x, tile in enumerate(row):
                bm = self.get_tile(tile)
                self.image[y * TILE_SIZE:(y+1)*TILE_SIZE,
                      x * TILE_SIZE:(x+1)*TILE_SIZE] = bm

    def draw(self, frame, offset=OFS):
        """
        draws the image into a frame
        offset pixels from the top left corner
        """
        frame[OFS:OFS+self.image.shape[0], OFS:OFS+self.image.shape[1]] = self.image
       

    def write_image(self, filename):
        """writes the image into a file"""
        cv2.imwrite(filename, self.image)


background = np.zeros((700, 1000, 3), np.uint8)
tiles = cv2.imread('/home/skywalker/Marchov_chain_proj/tiles.png')

market = SupermarketMap(MARKET, tiles)
#market.draw(market)

#tmap = SupermarketMap('f',tiles)

class Customer:

    def __init__(self, frame,  x, y):
         self.x = x
         self.y = y
         self.image = np.zeros((32, 32,3), dtype=np.uint8)
         self.frame = frame
         
    def draw(self,frame):
        
        xpos = OFS + self.x * TILE_SIZE
        ypos = OFS + self.y * TILE_SIZE
        self.frame[ ypos : ypos+ TILE_SIZE ,  xpos: xpos+ TILE_SIZE] = self.image
        
        
    def __repr__(self):
        return f'This is a customer that went in a store with the sections: {self.init_state_space} and they went like this: {self.journey}.'


c1 = Customer(market, 3, 7)


#market_background = market.draw()

while True:
    frame = background.copy()
    #frame = c1.draw()
    c1.draw(frame)
    #market_background = market.draw()
    

    cv2.imshow('frame', frame)

    key = chr(cv2.waitKey(1) & 0xFF)
    if key == 'q':
        break

cv2.destroyAllWindows()

frame.write_image("supermarket.png")


