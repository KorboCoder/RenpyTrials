#Reference Documentation: http://www.renpy.org/doc/html/rooms.html
#http://lemmasoft.renai.us/forums/viewtopic.php?f=8&t=11757
init python:
    g = Gallery()

    g.button("Image1")
    g.unlock_image("test1")
    
    g.button("Image2")
    g.unlock_image("test2")
    
    g.button("Image3")
    g.unlock_image("test3")
    
    g.button("Image4")
    g.image("test4")
    
    g.button("Image5")
    g.image("test1")
    g.image("test2")
    g.image("test3")
    g.image("test4")
    
    extra_screen = "cg"




screen extras():
    
    # This ensures that any other menu screen is replaced.
    tag menu

    # The background of the main menu.
    window:
        style "mm_root"
    
    #render cg screen
    if extra_screen == "cg":
        frame:
            
            style_group "mm"
            xalign 0.5
            yalign .2

            xmargin 10
            ymargin 70
             # A grid of buttons.
            grid 3 3:
                xfill True
                yfill True

                # Call make_button to show a particular button.
                add g.make_button("Image1", im.Scale("images/test1.jpg", 200,120), locked = Solid("#000000"),xalign=0.5, yalign=0.5)
                add g.make_button("Image2", im.Scale("images/test2.jpg", 200,120), locked = Solid("#000000"), xalign=0.5, yalign=0.5)
                add g.make_button("Image3", im.Scale("images/test3.jpg", 200,120), locked = Solid("#000000"), xalign=0.5, yalign=0.5)
                
               
                add g.make_button("Image4", im.Scale("images/test4.jpg", 200,120), xalign=0.5, yalign=0.5)
                add g.make_button("Image5", im.Scale("images/test1.jpg", 200,120), xalign=0.5, yalign=0.5)
                null height 100
                #null buffers so the layout looks good
                null height 100
                null height 100
                null height 100
                
    #render scene screen
    elif extra_screen == "scene":
        frame: 
            style_group "mm"
            xalign 0.5
            yalign .2

            xmargin 10
            ymargin 70
            has vbox:
                xfill True
                yfill True
                textbutton "Scene1" action Replay("scene_1")
                textbutton "Scene2" action Replay("scene_2")
                textbutton "Scene3" action Replay("scene_3")
    elif extra_screen == "music":
        frame:
            style_group "mm"
            xalign 0.5
            yalign .2

            xmargin 10
            ymargin 70
            has vbox:
                xfill True
                yfill True
                text "WIP"

            
    #the label at the upper left
    frame:
        style_group "mm"
        xalign 0.0
        yalign .02

        has hbox

        text("EXTRAS")
        
    # The main menu buttons.
    frame:
        style_group "mm"
        xalign 0.5
        yalign .02

        has hbox

        textbutton ("CG Gallery") action SetVariable("extra_screen", "cg")
        textbutton ("Scene Gallery") action SetVariable("extra_screen", "scene")
        textbutton ("Music Gallery") action SetVariable("extra_screen", "music")

    #button to go back to the main menu
    frame:
        style_group "mm"
        xalign .98
        yalign .98

        has hbox

        textbutton ("Return") action Return()