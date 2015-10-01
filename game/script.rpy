# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define g = Character('Girl', color="#c8ffc8")

image bg street = "images/darkstreet.jpg"


# image,density, speed, wind, angle
image normalrain = Snow("raindrop.png",5,400, 0,0)



# The game starts here.
label start:
    scene bg street
    show normalrain
    "Huh, it's raining"
