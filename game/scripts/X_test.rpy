default dragged_item = None


init python:
    def check_door_use():
        global dragged_item
        if dragged_item == upass:
            dragged_item = None
            renpy.jump("aboba")
        else:
            renpy.notify("Нужен пропуск.")
            dragged_item = None

style empty:
    background None

screen drag_clear_catcher():
    if dragged_item != None:
        button:
            focus "space"
            action SetVariable("dragged_item", None)
            xpos 0 ypos 0
            xsize config.screen_width
            ysize config.screen_height
            style "empty"


label test:
    scene bg university_entrance with dissolve
    show ilya panic at left
    il "В этот день - ничего не произошло! Все просто наслаждаются жизнью!"
    show ilya normal at left
    il "Пупупу..."
    
    $ add_item(oscilloscope)
    $ add_item(potion)
    $ add_item(key)
    $ add_item(upass)
    $ add_item(cheese_bun)

    
    il "Парапарапа..."
    il "Тутутутуу..."
    scene bg university_entrance with dissolve

    call screen explore_room
    return

screen explore_room:
    # Сбрасыватель предмета
    use drag_clear_catcher
    imagebutton:
        focus "entrance"
        auto "locations/university_entrance/entrance/entrance_%s.png"
        focus_mask True
        action [Function(check_door_use)]

    add DraggedItem(dragged_item)
    use inventory_button
    
    
label aboba:
    scene bg first_floor with dissolve
    show ilya normal at left
    il "Ты в АБОБЕ!"
    return