"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and McKinley.
"""
########################################################################
# Done: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# done: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################


import rosegraphics as rg

window = rg.TurtleWindow()

marie = rg.SimpleTurtle('turtle')
marie.pen = rg.Pen('purple', 3)
marie.speed = 20

size = 200

for k in range(30):
    marie.draw_circle(size)
    marie.pen_up()
    marie.right(45)
    marie.forward(10)
    marie.left(45)

    marie.pen_down()
    size = size - 12

bowen = rg.SimpleTurtle('turtle')
bowen.pen = rg.Pen('dark green', 3)
bowen.speed = 20
size = 300

for k in range(30):
    bowen.draw_regular_polygon(11, 100)
    bowen.pen_up()
    bowen.right(45)
    bowen.forward(10)
    bowen.left(45)
    bowen.pen_down()
    size = size - 12

window.close_on_mouse_click()
