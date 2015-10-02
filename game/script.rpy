# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"


    

# The game starts here.
label start:
    # for more characters just char2_affection etc etc
    $ char1_affection = 0
    while True:
        $ renpy.say("", "Current Affection: "+ str(char1_affection))
        menu:
            "Add 10":
                $ char1_affection += 10
                "Added 10"
            "Sub 10":
                $ char1_affection -= 10
                "Subtracted 10"
                
            "Is it Higher than 50?":
                if char1_affection > 50:
                    "Yes"
                else:
                    "No"
            "Is it Higher less than 50?":
                if char1_affection < 50:
                    "Yes"
                else:
                    "No"
                    
            "Is it between 10 and 40?":
                if char1_affection > 10 and char1_affection < 40:
                    "Yes"
                else:
                    "No"


 