
import numpy as np
import cv2


TILE_SIZE = 32
OFS = 50

MARKET = """
##################
##..............##
##..##..##..##..##
##..B#..B#..B#..##
##..##..##..##..##
##..##..##..##..##
##..##..##..##..##
##...............#
##..C#..C#..C#...#
##..##..##..##...#
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
        self.image = np.zeros((self.ysize * TILE_SIZE, self.xsize * TILE_SIZE, 3), dtype=np.uint8)
        self.prepare_map()

    def get_tile(self, char):
        """returns the array for a given tile character"""
        if char == '#':
            return self.tiles[0:32, 0:32]
        elif char == 'G':
            return self.tiles[7*32:8*32, 3*32:4*32]
        elif char == 'C':
            return self.tiles[2*32:3*32, 8*32:9*32]
        elif char == 'B':
            return self.tiles[0:32, 4*32:5*32]
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

class Customer:

    def __init__(self, tmap, image, x, y):
         self.x = x
         self.y = y
         self.image = np.zeros((self.y , self.x, 3), dtype=np.uint8)
         self.tmap = tmap

    def draw(self, frame):
        xpos = OFS + self.x * TILE_SIZE
        ypos = OFS + self.y * TILE_SIZE
        frame[ypos:ypos, xpos:xpos] = self.image



background = np.zeros((700, 1000, 3), np.uint8)
tiles = cv2.imread('tiles.png')

market = SupermarketMap(MARKET, tiles)
c = Customer(market, image, 10, 12 )

while True:
    frame = background.copy()
    market.draw(frame)

    cv2.imshow('frame', frame)

    key = chr(cv2.waitKey(1) & 0xFF)
    if key == 'q':
        break

cv2.destroyAllWindows()

market.write_image("market1.png")
