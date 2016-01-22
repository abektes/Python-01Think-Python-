try:
    # see if Swampy is installed as a package
    from swampy.TurtleWorld import *
    from polygon import circle, arc

    import math

except ImportError:
    # otherwise see if the modules are on the PYTHONPATH
    from TurtleWorld import *

def TheodorusSpiral(myTurtle,n,d):

    for i in range(n-1):
        a = (i+2)
        c = math.fabs(math.sqrt(a))
        angle = math.degrees(math.atan(c/1))
        angle2 = math.degrees(math.atan(1/math.sqrt(a+1)))
        angle3 = math.degrees(math.atan(math.sqrt(a+1)/1))
        angle4 = 180 - (angle2 + angle3)
        angle5 = 180 -(angle + angle4)
        myTurtle.fd(d)
        myTurtle.lt(angle5)



# create the world and bob
world = TurtleWorld()
bob = Turtle()
bob.delay = 0
TheodorusSpiral(bob,6,10)

wait_for_user()

