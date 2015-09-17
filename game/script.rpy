# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

#setup 3d camera
#init python:
 #      register_3d_layer('background', 'middle', 'forward')

# Declare characters used by this game.
define g = Character('Girl', color="#c8ffc8")

image bg street = "images/darkstreet.jpg"
# The game starts here.
label start:
    scene bg street
  
    g "Derp derp"
    "Herpa Derp"
 