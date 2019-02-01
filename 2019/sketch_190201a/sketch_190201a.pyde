def setup():
    size(500, 500)

def draw():
    background(200)
    strokeWeight(1)
    stroke(0)
    r1 = 75.
    r2 = 25.
    ri = r1 - r2
    p1 = PVector(200, 250)
    p2 = PVector(mouseX, mouseY)
    # ellipse(d, 0, r2 * 2, r2 * 2)
    # ellipse(0, 0, r1 * 2, r1 * 2)
    strokeWeight(3)
    noFill()
    new_bar(p1, p2, r1, r2)


def new_bar(p1p, p2p, r1, r2):
    d = dist(p1p.x, p1p.y, p2p.x, p2p.y)
    if d > 0:
        with pushMatrix():
            translate(p1p.x, p1p.y)
            angle = atan2(p1p.x - p2p.x, p2p.y - p1p.y)
            rotate(angle + HALF_PI)
            ri = r1 - r2
            beta = asin(ri / d) + HALF_PI
            x1 = cos(beta) * r1
            y1 = sin(beta) * r1
            x2 = cos(beta) * r2
            y2 = sin(beta) * r2
            line(-x1, -y1, d - x2, -y2)
            line(-x1, +y1, d - x2, +y2)
            arc(0, 0, r1 * 2, r1 * 2,
                -beta - PI, beta - PI) 
            arc(d, 0, r2 * 2, r2 * 2,
                beta - PI, PI - beta)
    
def keyPressed():
    saveFrame("sketch-190201a.png")
