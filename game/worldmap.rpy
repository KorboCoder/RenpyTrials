screen defaultmap():
    tag map
    add "worldmap_background.jpg"

    imagebutton focus_mask True auto "button_scene1_%s.png" xpos 40 ypos 50 action Jump("scene1")
    
    imagebutton focus_mask True auto "button_scene2_%s.png" xpos 500 ypos 70 action Jump("scene2")

label defaultmap:
    call screen defaultmap

label scene1:
    "This is scene1"
    
    jump defaultmap
    
label scene2:
    "This is scene2"
    
    jump defaultmap