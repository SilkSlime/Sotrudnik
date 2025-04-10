init python:
    class Quest:
        def __init__(self, name, description):
            self.name = name
            self.description = description
    class Item:
        def __init__(self, name, image, description):
            self.name = name
            self.image = image
            self.description = description
    class Note:
        def __init__(self, name, description):
            self.description = description

    # Define available items
    oscilloscope = Item("Осциллограф", "items/oscilloscope_%s.webp", "Я украл его из лабы, когда только устроился в институт")
    potion = Item("Бутылка Росинки", "items/rosinka_%s.webp", "Чистая и освежающая. Всеми горячо любимая!")
    key = Item("Старый ключ", "items/key_%s.webp", "Старый ржавый ключ. Может он что-то открывает?")
    upass = Item("Пропуск", "items/key_%s.webp", "Пропуск в институт. Хотя он новый, на нем уже появились потертости и грязь.")
    cheese_bun = Item("Булочка с сыром", "items/key_%s.webp", "Сырная булочка из буфета. Теплая и ароматная!")

    quest1 = Quest("Чесальня", "Почесать за ухом")
    quest2 = Quest("Выпить пива", "Попить пивка у фонтана")
    quest3 = Quest("Закон Архимеда", "Поесть и покурить после")


    def add_item(item):
        # if item not in items:
        renpy.notify(f"Добавлен предмет: {item.name}")
        items.append(item)

    def remove_item(item):
        if item in items:
            items.remove(item)
