# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

image bg street = "images/darkstreet.jpg"
image bg bedroom = "images/bedroom.jpg"

define CircleIn = ImageDissolve("circle_dissolve.png",2.0, reverse = False)
define CircleOut = ImageDissolve("circle_dissolve.png", 2.0, reverse = True)

# The game starts here.
label start:
    scene bg bedroom with CircleOut
    scene black with CircleIn
    scene bg street with CircleOut
	


 