import turtle

def drawOctagon(t, sz):
    """Make turtle t draw an octagon of sz"""

    for i in range(8):
        t.forward(sz)
        t.left(45)


tess = turtle.Turtle()
drawOctagon(tess, 50) 