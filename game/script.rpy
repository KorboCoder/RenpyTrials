# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

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

image stuffInRoom:
    size (800, 600)
    xalign .5
    yalign .5
    "bg room"
    crop(150,330,200,150)
    
    #Show aircon
    easein 1.0 crop(200,330,200,150)
    
    #Show tableside
    easein 2.0 crop(470,325, 250, 200)
    
    #Show lamp
    easein 3.0 crop(710,515, 250, 200)

# The game starts here.
label start:
    scene bg street
    show g normal
    "Hello"
    show  g giggle with Dissolve(0.2)
    g "You're funny"
    show g normal with Dissolve(0.1)
    
    g "Now go away"
    
    show g normal:
        linear 2.0 zoom 2.0 yoffset 600
        
    g "No really, go away."
    
    show g giggle with Dissolve(0.2):
        zoom 2.0 yoffset 600
    
    g "..."
  
    play sound "sfx/punch.wav"
    "*THWACK*" with vpunch 
    
    scene bg room with Fade(0.1,2.0,3.0)
    "Uuugggghhh"
    show stuffInRoom with Dissolve(0.1)
    "What the hell"
    hide stuffInRoom with Fade(1.0, 1.0, 1.0)
    "I need to take a dump"