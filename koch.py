from turtle import *
try :
    reset()
except Terminator:
    pass
def koch(L, n):

    if n == 0:
        forward(L)
    else:
        koch(L/3, n-1)
        left(60)
        koch(L/3, n-1)
        right(120)
        koch(L/3, n-1)
        left(60)
        koch(L/3, n-1)

def flocon(T, etape):
    koch(T, etape)
    right(120)
    koch(T, etape)
    right(120)
    koch(T, etape)


up()
goto(-280, 100)
down()
speed(50)

flocon(100, 3)

done()