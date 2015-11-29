# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define e = Character('Eileen', color="#c8ffc8")
define test1 = "images/test1.jpg"
define test2 = "images/test2.jpg"
define test3 = "images/test3.jpg"


# The game starts here.
label start:
    "Start of the VN"
label scene_1:
    scene 
    show test1
    "This is scene 1 I think"
    
    $renpy.end_replay()
"The next scene should be..."

label scene_2:
    scene 
    show test2
    "Scene 2"
    "This is definitly what scene 2 should be like."
    
    $renpy.end_replay()
"And finally we end everything with..."
label scene_3:
    scene 
    show test3
    "The finale, SCENE 3!"
    $renpy.end_replay()
  

    return
