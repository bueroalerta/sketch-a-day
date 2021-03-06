# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s126b"  # 180506

add_library('serial')  # import processing.serial.*;
add_library('arduino')  # import cc.arduino.*;
add_library('gifAnimation')

from gif_exporter import *
from inputs import *

def setup():
    global input, GIF_EXPORT
    size(600, 600, P2D)
    noFill() 
    Cell.CELLS = []
    GIF_EXPORT = False
    # Ask user for Arduino port, uses slider if none is selected`
    input = Input(Arduino, slider_pins=[1, 2])
    create_grid()

def draw():
    fill(64, 64, 127, 128) 
    rect(0, 0, width, height)

    for cell in Cell.CELLS:
        cell.draw_()
    # uncomment next lines to export GIF
    global GIF_EXPORT
    if GIF_EXPORT:
        GIF_EXPORT = gif_export(GifMaker,
                                frames=50,
                                delay=200,
                                filename=SKETCH_NAME)

    # Updates reading or draws sliders and checks mouse dragging / keystrokes
    input.update()
    Cell.update()


def keyPressed():
    global GIF_EXPORT
    if key == 'p':  # save PNG
        saveFrame("####.png")
    if key == 'g':  # save GIF
        GIF_EXPORT = True
    if key == 'h':
        input.help()
    if key == 'r':
        create_grid()
    input.keyPressed()

def keyReleased():
    input.keyReleased()

def pointy_hexagon(x, y, r):
    with pushMatrix():
        translate(x, y)
        rotate(radians(30))  # pointy, comment out for "flat_hexagon()"
        beginShape()
        for i in range(6):
            sx = cos(i * TWO_PI / 6) * r
            sy = sin(i * TWO_PI / 6) * r
            vertex(sx, sy)
        endShape(CLOSE)

def create_grid():
    global GRID_SIDE, RAND_SIZE, SPAC_SIZE
    # seize inputs
    GRID_SIDE = int(input.analog(1) / 16)  # 0 a 63 linhas e colunas na grade
    randomSeed(int(input.analog(2)) / 4)
    # espaçamento entre os elementos
    SPAC_SIZE = int(width / (GRID_SIDE + 0.01))

    # empty list
    Cell.CELLS[:] = []
    v = SPAC_SIZE * 1.5
    h = SPAC_SIZE * sqrt(3)
    for _ in range(1):
        for ix in range(GRID_SIDE):  # um x p/ cada coluna
            # um y p/ cada linha
            for iy in range(GRID_SIDE):
                if iy % 2:
                    x = ix * h + h / 4
                else:
                    x = ix * h - h / 4
                y = iy * v
                Cell.CELLS.append(Cell(x, y))

class Cell():
    CELLS = []

    def __init__(self, x, y):

        self.x = x
        self.y = y
        self.status = int(random(10)<8)

    def update_nc(self):
        self.nc = self.neighbours()
        if self.nc < 2:
            self.next = 0
        elif self.nc > 3:
            self.next = 0
        else:
            self.next = 1
            
    @classmethod        
    def update(cls):
        for cell in cls.CELLS:
            cell.status = cell.next
        
    def get_color(self):
        return map(self.nc, 0, 6, 0, 255)

    def get_size(self):
        return (SPAC_SIZE / 6) * (1 + self.nc)

    def draw_(self):
        self.update_nc()
        if self.status:
            stroke(self.get_color())
            noFill()
            pointy_hexagon(self.x, self.y, self.get_size())

    def neighbours(self):
        count = 0
        for cell in Cell.CELLS:
            if cell is not self and cell.status:
                if dist(self.x, self.y, cell.x, cell.y) < SPAC_SIZE * 2:
                    count += 1
        return count
