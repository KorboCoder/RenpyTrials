# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

#setup 3d camera
#init python:
 #      register_3d_layer('background', 'middle', 'forward')

# Declare characters used by this game.
define g = Character('Girl', color="#c8ffc8")

transform move_jump:
    xalign 1.0 yalign 0.0
    pause 1.0
    linear 1.0 xalign 0.5
    pause 1.0
    repeat

# Declare images
image g giggle = "images/sylvie_giggle.png"
image g normal = "images/sylvie_normal.png"
image bg street = "images/darkstreet.jpg"
image bg room = "images/bedroom.jpg"
image dummyRoom1 = Image("images/bedroom.jpg")
image dummyRoom2 = Image("images/bedroom.jpg")

image snow = "snow.png"
image redsnow = "redsnow.png"
image snowblossom = Snow("snow.png",2000,800,0)



# The game starts here.
label start:
    scene bg street
    show snowblossom:
        rotate 0
        
    "Heavy Blizzard"