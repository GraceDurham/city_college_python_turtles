import turtle


def drawTriangle(t, sz):
    """Make turtle t draw a triangle of sz."""

    for i in range(3):
        t.foward(sz)
        t.left(120)


tess = turtle.Turtle()
drawTriangle(tess, 70)