# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

#setup 3d camera
#init python:
 #      register_3d_layer('background', 'middle', 'forward')

# Declare characters used by this game.
define g = Character('Girl', color="#c8ffc8")

transform left_to_right:
    xalign 0.0
    xoffset -20
    alpha 0
    parallel:
        easein 0.2 xoffset 0.0
    parallel:
        easein 0.2 alpha 1.0
# Declare images
image g giggle = "images/sylvie_giggle.png"
image g normal = "images/sylvie_normal.png"
image bg street = "images/darkstreet.jpg"
image bg room = "images/bedroom.jpg"
image dummyRoom1 = Image("images/bedroom.jpg")
image dummyRoom2 = Image("images/bedroom.jpg")

image snow = "snow.png"
# image,density, speed, wind, angle
image normalsnow = Snow("raindrop.png",5,400, 0,0)
image blizzard = Snow("raindrop.png",10,900,100,45)



# The game starts here.
label start:
    scene bg street
    show normalsnow 
    "Huh, it's snowing"
    hide normalsnow with Dissolve (0.2)
    show blizzard with Dissolve (0.2)
    show g normal at left:
        left_to_right
  
    "This is bad"
 