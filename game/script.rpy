# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
init python:
    def randomfloat(min,max):
        randNum = renpy.random.random()
        randNum*=(max-min)
        randNum+=min
        return randNum
        
image snow = "snow.png"
# image,density, speed, wind, angle

image smokeblur  = "smokeblur.png"
image steamblur  = "steamblur.png"
image onsen = "onsen.jpg"
image room = "images/bedroom.jpg"

image black = Solid("#000")
transform steamTransform:
    truecenter
    additive 0.7
    xpos randomfloat(0.0,1.0)
    alpha 1.0
    ypos 1.4
    pause randomfloat(0.2,1.0)
    easeout randomfloat(1.7, 2.5) ypos randomfloat(0.1,0.2)  alpha 0.0
    repeat
    
transform smokeTransform:
    truecenter
    additive -0.5
    xpos randomfloat(0.0,1.0)
    alpha 1.0
    ypos 1.4
    pause randomfloat(0.2,1.0)
    easein randomfloat(1.2, 2.0) ypos randomfloat(0.1,0.2) alpha 0.0
    repeat

image steam:
    parallel:
        steamTransform
        repeat
    parallel:
        steamTransform
        repeat
    parallel:
        steamTransform
        repeat
    parallel:
        steamTransform
        repeat
    parallel:
        steamTransform
        repeat
        

    

# The game starts here.
label start:
    scene onsen
    #show steam
    show steamblur as twin1:
        steamTransform
    show steamblur as twin2:
        steamTransform
    show steamblur as twin3:
        steamTransform
    show steamblur as twin4:
        steamTransform
    show steamblur as twin5:
        steamTransform
    show steamblur as twin6:
        steamTransform
    show steamblur as twin7:
        steamTransform
    show steamblur as twin8:
        steamTransform
    show steamblur as twin9:
        steamTransform
    "onsen time!"
    scene room
    show smokeblur as twin1:
        smokeTransform
    show smokeblur as twin2:
        smokeTransform
    show smokeblur as twin3:
        smokeTransform
    show smokeblur as twin4:
        smokeTransform
    show smokeblur as twin5:
        smokeTransform
    show smokeblur as twin6:
        smokeTransform
    show smokeblur as twin7:
        smokeTransform
    show smokeblur as twin8:
        smokeTransform
    show smokeblur as twin9:
        smokeTransform
    
    "BURN!"
 