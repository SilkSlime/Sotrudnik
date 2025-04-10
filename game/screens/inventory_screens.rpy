define inventory.frame_borders = Borders(6, 6, 6, 6)
define inventory.frame_tile = False

## Кнопки в секции навигации главного и игрового меню.
define inventory.navigation_spacing = 6
## Местоположение левого края навигационных кнопок по отношению к левому краю
## экрана.
define inventory.navigation_xpos = 200

## Количество колонок и рядов в таблице инвентаря.
define inventory.items_slot_cols = 6
define inventory.items_slot_rows = 3
## Расстояние между ячейками инвентаря
define inventory.items_xspacing = 23
define inventory.items_yspacing = 50

style inventory_outer_frame is empty

style inventory_outer_frame:
    bottom_padding 45
    top_padding 180


style inventory_navigation_frame is empty
style inventory_navigation_frame:
    xsize 310
    yfill True

style inventory_content_frame:
    background Frame("gui/book.png", inventory.frame_borders, tile=inventory.frame_tile)
    left_padding 90
    right_margin 30
    top_margin 15

style inventory_content is empty
style inventory_content_text:
    color "#4b2206"
style inventory_content:
    xysize (1300, 720)
    padding (15, 15)


screen inventory_button():
    imagebutton:
        idle "gui/inventory/mark_inventory_inactive.png"
        hover "gui/inventory/mark_inventory_active.png"
        selected_idle "gui/inventory/mark_inventory_inactive.png"
        action Show("items")
        xalign 0.96


screen inventory_menu(title, scroll=None, yinitial=0.0, spacing=0):
    style_prefix "game_menu"

    frame:
        background "gui/fade.png"
        frame:
            style "inventory_outer_frame"
            hbox:
                ## Резервирует пространство для навигации.
                frame:
                    style "inventory_navigation_frame"
                frame:
                    style "inventory_content_frame"
                    if scroll == "viewport":
                        viewport:
                            yinitial yinitial
                            scrollbars "vertical"
                            mousewheel True
                            draggable True
                            pagekeys True

                            side_yfill True
                            vbox:
                                spacing spacing
                                transclude
                    elif scroll == "vpgrid":
                        vpgrid:
                            cols 1
                            yinitial yinitial
                            scrollbars "vertical"
                            mousewheel True
                            draggable True
                            pagekeys True
                            side_yfill True
                            spacing spacing
                            transclude
                    else:
                        transclude
        use inventory_navigation


screen inventory_navigation():
    # zorder 0
    vbox:
        xpos inventory.navigation_xpos
        yalign 0.52
        spacing inventory.navigation_spacing
        imagebutton:
            idle "gui/inventory/items_idle.png"
            hover "gui/inventory/items_hover.png"
            selected_idle "gui/inventory/items_active.png"
            selected_hover "gui/inventory/items_active.png"
            action Show("items")
            xalign 1.0
        imagebutton:
            idle "gui/inventory/quests_idle.png"
            hover "gui/inventory/quests_hover.png"
            selected_idle "gui/inventory/quests_active.png"
            selected_hover "gui/inventory/quests_active.png"
            action Show("quests")
            xalign 1.0
        imagebutton:
            idle "gui/inventory/notes_idle.png"
            hover "gui/inventory/notes_hover.png"
            selected_idle "gui/inventory/notes_active.png"
            selected_hover "gui/inventory/notes_active.png"
            action Show("notes")
            xalign 1.0
        text "" size 90
        imagebutton:
            idle "gui/inventory/close_idle.png"
            hover "gui/inventory/close_hover.png"
            selected_idle "gui/inventory/close_active.png"
            selected_hover "gui/inventory/close_active.png"
            action Hide()
            xalign 1.0


style items is empty
style items_card_text is empty
style items_card_text:
    color "#4b2206"

screen items():
    modal True
    tag menu

    use inventory_menu(_("Предметы")):
        frame:
            style_prefix "inventory_content"
            style "inventory_content"
            grid inventory.items_slot_cols inventory.items_slot_rows:
                xspacing inventory.items_xspacing
                yspacing inventory.items_yspacing

                for i in range(inventory.items_slot_cols * inventory.items_slot_rows):
                    frame:
                        xysize (180, 180)
                        padding (0, 0)

                        
                        # if len(items) > i:
                        #     background "gui/tile.png"
                        # else:
                        # background im.Scale("gui/nobg.png", 180, 180)
                        # DEBUG
                        background im.Scale("gui/card.png", 180, 180)
                        
                        if len(items) > i:
                            vbox:
                                $ item = items[i]
                                # TODO: Описание как-нибудь по другому сделать
                                # imagebutton:
                                #     auto item.image
                                #     action Show("item_description", item=item)
                                #     xalign 0.5 yalign 0.5
                                # text "[item.name]" size 18 xalign 0.5
                                imagebutton:
                                    auto item.image
                                    xalign 0.5 yalign 0.5
                                    action [SetVariable("dragged_item", item), Hide("items")]

                                text "[item.name]" size 18 xalign 0.5



screen quests():
    modal True
    tag menu

    use inventory_menu(_("Поручения")):
        frame:
            style_prefix "inventory_content"
            style "inventory_content"
            vbox:
                text "Поручения" size 32
                for quest in quests:
                    hbox:
                        text "[quest.name]" size 24
                        text "[quest.description]" size 20

screen notes():
    modal True
    tag menu

    use inventory_menu(_("Записки")):
        frame:
            style_prefix "inventory_content"
            style "inventory_content"
            text "TODO: Записки"

style item_description_text:
    color "#4b2206"


# TODO: Сделать похожим на лист из блокнота
screen item_description(item):
    modal True
    tag item_description
    frame:
        background "gui/fade.png"
        xfill True
        yfill True
        frame:
            style_prefix "inventory_content"
            style "inventory_content_frame"
            padding (10, 10)
            background Frame("gui/card.png", inventory.frame_borders, tile=inventory.frame_tile)
            xysize (500, 400)
            xalign 0.5
            yalign 0.5
            fixed:
                # TODO: Крестик заменить на клик вне фрейма
                imagebutton:
                    auto "gui/close_%s.png"
                    xalign 1.0
                    action Hide()
            vbox:
                xfill True
                text "[item.name]" xalign 0.5 
                # $ image_url = 
                add item.image % "idle" xalign 0.5
                text item.description size 24 xalign 0.5

# TODO: Механика перемещения - либо через карту, либо через интегрированное перемещение (навестись на дверь и кликнуть)
# TODO: Механика применения предмета - либо выбор в инвентаре, либо открытие инвентаря при взаимодействии с объектом
# TODO: Система статусов - например если выпить пива - буквы будут плясать, либо можно что-то забыть