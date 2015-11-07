transform pulse:
    alpha 0.0
    linear 0.4 alpha 1.0
    linear 0.4 alpha 0.0
    repeat
    

image button_scene1_hover:
    "button_scene1_hover.png"
    pulse

image button_scene2_hover:
    "button_scene2_hover.png"
    pulse


screen defaultmap():
    tag map
    add "worldmap_background.jpg"

    add "button_scene1_idle.png" xpos 40 ypos 50 
    imagebutton focus_mask True idle "button_scene1_idle.png" hover  "button_scene1_hover" xpos 40 ypos 50 action Jump("scene1")
    
    add "button_scene2_idle.png" xpos 500 ypos 70
    imagebutton focus_mask True idle "button_scene2_idle.png" hover  "button_scene2_hover" xpos 500 ypos 70 action Jump("scene2")

label defaultmap:
    call screen defaultmap

label scene1:
    "This is scene1"
    
    jump defaultmap
    
label scene2:
    "This is scene2"
    
    jump defaultmap