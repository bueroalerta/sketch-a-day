"""
sketch 66 180307 - Alexandre B A Villares
https://abav.lugaralgum.com/sketch-a-day
"""

import random as rnd
import copy as cp

SAVE_FRAMES, STOP = True, False

def setup():
    global d1, d2, d3
    size(500, 500)
    rectMode(CENTER)
    noFill()
    d1 = Drawing(
        45, 45, spacing=30, size_=150, range_=1, color_=color(0, 255, 0))
    d2 = Drawing(
        105, 105, spacing=60, size_=240, range_=1.5, color_=color(0, 0, 255))
    d3 = Drawing(
        225, 225, spacing=75, size_=225, range_=2, color_=color(255, 0, 0))

def draw():
    background(200)
    fc = frameCount % 300 - 150
    if fc < 0:
        fase = 0
    elif 0 <= fc < 149:
        fase = map(fc, 0, 149, 0, 1)
    elif fc == 149:
        if STOP:
            noLoop()
        fase = 0
        d1.randomize()
        d2.randomize()
        d3.randomize()

    d1.plot(fase)
    d2.plot(fase)
    d3.plot(fase)

    if SAVE_FRAMES and not fc % 10:
        saveFrame("####.tga")

def keyPressed():
    global STOP
    if key == 'b':
        d1.go_back()
        d2.go_back()
        d3.go_back()
        STOP = True

class Drawing():

    def __init__(self, x_=10, y_=10, spacing=10, size_=100, range_=1, color_=color(255, 0, 0)):
        """
        clears the list of nodes and creates a a new drawing appending a
        list of nodes/drawing elements: arrows, connecting lines and lonely nodes
        """
        self.single_color = color_
        self.drawing = list()
        self.spacing, self.size_, self.range_ = spacing, size_, range_
        for x in range(x_, x_ + size_ + 1, spacing):
            for y in range(y_, y_ + size_ + 1, spacing):
                self.drawing.append(
                    D_node(x, y, self.drawing, self.single_color))
        for node in self.drawing:  # para cada elemento do drawing
            node.randomize_target(0, range_ * spacing)  # set of random targets
            node.copy_target(0, -1)   # backup of original targets
            # secondary set of random targets
            node.randomize_target(1, range_ * spacing)

    def randomize(self):
        for node in self.drawing:
            node.copy_target(1, 0)
            node.randomize_target(1, self.range_ * self.spacing)

    def go_back(self):
        for node in self.drawing:
            node.copy_target(-1, 1)  # target back to the first points

    def plot(self, fase):
            # draws circles/'lines', non-arrows
        for node in (n for n in self.drawing if not n.is_arrow):
            node.plot(fase)
        # draws arrows
        for node in (n for n in self.drawing if n.is_arrow):
            node.plot(fase)


class D_node(object):

    """ Drawing elements,  arrows or circles that might point to another element """

    def __init__(self, x, y, drawing, s_color):
        self.x = x
        self.y = y
        self.t_size = rnd.choice([5, 10, 15])    # t_size
        self.s_weight = rnd.choice([1, 2, 3])    # s_weight
        self.is_arrow = rnd.choice([True, False])
        # current targets, next targets, initial targets
        self.points_to = [[], [], []]
        self.drawing = drawing
        self.single_color = s_color

    def plot(self, amt, other=None):
        strokeWeight(self.s_weight)
        stroke(self.s_color(amt))
        for other in self.points_now(amt):
            if self.is_arrow:
                seta(self.x, self.y, other.x, other.y,
                     # shorten amount, head size
                     self.t_size, self.s_weight * 5,
                     rect, self.t_size)  # tail func, tail size
            else:
                line(self.x, self.y, other.x, other.y)
                ellipse(self.x, self.y, self.t_size, self.t_size)
        if not other:
            if self.is_arrow:
                other = self
                seta(self.x, self.y, other.x, other.y,
                     self.t_size, self.s_weight * 5,
                     rect, self.t_size)
            else:
                ellipse(self.x, self.y, self.t_size, self.t_size)

    def randomize_target(self, index, range_times_spacing):
        self.points_to[index][:] = []
        for _ in range(3):
            rnd_node = rnd.choice(self.drawing)
            while dist(self.x, self.y, rnd_node.x, rnd_node.y) > range_times_spacing:
                rnd_node = rnd.choice(self.drawing)
            if (self.x, self.y) != (rnd_node.x, rnd_node.y) and random(10) < 5:
                self.points_to[index].append(PVector(rnd_node.x, rnd_node.y))

    def copy_target(self, origin, destination):
        self.points_to[destination] = cp.deepcopy(self.points_to[origin])

    def never_empty(self, points):
        if not points:
            return [PVector(self.x, self.y)]
        else:
            return points

    def points_now(self, amt=0):
        points = []
        if amt in [0, 1]:
            return self.points_to[int(amt)]
        else:
            # for p0 in self.never_empty(self.points_to[0]):
            # not all interpolated arrows are shown
            p0 = self.never_empty(self.points_to[0])[0]
            for p1 in self.never_empty(self.points_to[1]):
                points.append(PVector(lerp(p0.x, p1.x, amt),
                                      lerp(p0.y, p1.y, amt)))
        return points

    def s_color(self, amt):
        if amt in [0, 1]:
            if not self.points_to[int(amt)]:
                return self.single_color
            elif self.is_arrow:
                return color(0)
            else:
                return color(255)
        else:
            return lerpColor(self.s_color(0), self.s_color(1), amt)

def seta(x1, y1, x2, y2, shorter=0, head=None,
         tail_func=None, tail_size=None):
    """
    Seta means arrow in Portuguese
    """
    L = dist(x1, y1, x2, y2)
    if not head:
        head = max(L / 10, 10)
    with pushMatrix():
        translate(x1, y1)
        angle = atan2(x1 - x2, y2 - y1)
        rotate(angle)
        offset = shorter / 2
        strokeCap(ROUND)
        if L > head * 2:
            line(0, L - offset, -head / 3, L - offset - head)
            line(0, L - offset, head / 3, L - offset - head)
            strokeCap(SQUARE)
            line(0, offset, 0, L - offset)
        if tail_func and tail_size:
            tail_func(0, 0, tail_size, tail_size)
