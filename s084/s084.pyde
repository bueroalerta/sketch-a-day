# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s084" # 180325

add_library('gifAnimation')
from gif_exporter import gif_export
from slider import Slider

A = Slider(1, 40, 10, 'q', 'a')
B = Slider(1, 40, 10, 'w', 's')
C = Slider(1, 40, 10, 'e', 'd')
D = Slider(1, 40, 10, 'r', 'f')
# I need these globals because I want to call the sliders after drawing
a, b, c, d = 1, 1, 1, 1

def exes(x, y, c, _):
    with pushMatrix():
        translate(x, y)
        line(-c/2,-c/2, c/2, c/2)
        line(c/2,-c/2, -c/2, c/2)

def losang(x, y, c, _):
    with pushMatrix():
        translate(x, y)
        rotate(radians(45))
        rect(0, 0, c, c)
                
SHAPES = [ellipse,
          rect,
          exes,
          losang ]

def setup():
    size(600, 600, P2D)
    colorMode(HSB)
    rectMode(CENTER)
    noFill()

    A.position(40, height - 70)
    B.position(40, height - 30)
    C.position(width - 140, height - 70)
    D.position(width - 140, height - 30)
    # noLoop()

def draw():
    global a, b, c, d
    background(200)
    randomSeed(int(d * 100))

    for i in range(d):
        tam = a * c
        x = int(random(width - tam)/c)*c
        y = int(random(height - tam)/c)*c
        if i % 2:
            stroke(0)
        else:
            stroke(255)
        grid(x, y, a, b, c, rnd_choice(SHAPES))  # , ellipse, (a, a))
        
    a = int(A.value())  # elem num
    b = int(B.value())  # size
    c = int(C.value())  # space
    d = int(D.value())  # grid num

    # uncomment next lines to export GIF
    # if not frameCount % 12:
    #     gif_export(GifMaker,
    #                frames=2000,
    #                delay=340,
    #                filename=SKETCH_NAME)

def grid(x, y, num, size_, space, func):  
    for i in range(x, x + num * space, space):
        for j in range(y, y + num * space, space):
            func(i, j, size_, size_)
            
def rnd_choice(collection):
    i = int(random(len(collection)))
    return collection[i]
    
# def keyPressed():
#     saveFrame(SKETCH_NAME + '_###.gif')
