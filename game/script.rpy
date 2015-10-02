# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"


    

# The game starts here.
label start:
    # Initialize affection points, which right now is zero.
    $ char1_affection = 0
    while True:
        # Print out current affection point for char1
        $ renpy.say("", "Current Affection: "+ str(char1_affection))
        menu:
            "Add 10":
                # Add 10 to affeciton point
                $ char1_affection += 10
                "Added 10"
            "Sub 10":
                # Deduct 10 to affeciton point
                $ char1_affection -= 10
                "Subtracted 10"
                
            "Is it Higher than 50?":
                # Say yes if affection point is higher than 50, else say no
                if char1_affection > 50:
                    "Yes"
                else:
                    "No"
                
            "Is it less than 50?":
                # Say yes if affection point is less than 50, else say no
                if char1_affection < 50:
                    "Yes"
                else:
                    "No"
           
            "Is it between 10 and 40?":
                # Say yes if affection point is more than 10 and less than 40, else say no
                if char1_affection > 10 and char1_affection < 40:
                    "Yes"
                else:
                    "No"


 