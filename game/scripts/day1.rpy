# label day1_intro:
#     $ day = 1
#     $ time_of_day = "morning"
#     $ persistent.inventory = []
#     $ persistent.tasks = ["Оформить документы у Кати", "Познакомиться с командой СТРАТЕГ"]
#     $ persistent.notes = []

#     scene bg_ploshad_day
#     with fade

#     play music "audio/ambience_wind.ogg" fadein 2.0

#     "Шум ветра, скрип плит под ногами, резкий свет..."
#     "Ты приходишь в сознание."

#     show ilya neutral at left
#     "???": "Ты в порядке?"
    
#     "Ты медленно поднимаешься, в голове пусто."

#     ilya "Я — Илья. Координатор проекта «СТРАТЕГ». Ты должен быть новенький лаборант."

#     menu:
#         "Кивнуть, не говоря ни слова":
#             "Ты молча киваешь. Илья, похоже, не удивлён."
#         "Спросить, кто он такой и что за проект":
#             $ persistent.notes.append("Проект СТРАТЕГ — загадка")
#             ilya "Об этом позже. Тебе нужно сначала пройти оформление."

#     ilya "Держи временный пропуск. Не потеряй."
#     $ persistent.inventory.append("Временный пропуск")

#     ilya "Пошли, всё покажу. Ты быстро втянешься."

#     jump day1_office_intro


# label day1_office_intro:
#     scene bg_1etazh
#     with dissolve
#     show ilya neutral at left

#     "Вы заходите в мраморное здание с высокими потолками."

#     ilya "Первым делом — к Кате. Без документов ты никто."

#     scene bg_buhgalteriya
#     with dissolve
#     show katya neutral at right

#     katya "Ты новенький? Я уже оформила тебя."
#     katya "Вот твой постоянный пропуск. Инструкции на обратной стороне."

#     $ persistent.inventory.remove("Временный пропуск")
#     $ persistent.inventory.append("Постоянный пропуск")
#     $ persistent.tasks.remove("Оформить документы у Кати")

#     menu:
#         "Поблагодарить":
#             "Ты: Спасибо... Я будто был здесь раньше."
#         "Спросить, откуда она узнала":
#             katya "Иногда я просто знаю."

#     scene bg_bufet
#     with fade
#     show ilya happy at left

#     ilya "Здесь кормят. Иногда даже вкусно."

#     menu:
#         "Купить булочку (если есть монета)":
#             if "Монета" in persistent.inventory:
#                 $ persistent.inventory.remove("Монета")
#                 $ persistent.inventory.append("Сырная булочка")
#                 "Ты покупаешь сырную булочку. Тёплая и ароматная."
#             else:
#                 "Ты ничего не покупаешь. Монет нет."
#         "Ничего не брать":
#             "Ты просто осматриваешься."

#     scene bg_kabinet_strateg
#     with fade

#     show polina neutral at left
#     show artem neutral at right
#     show nastya neutral at center

#     "Вы входите в кабинет. Шум принтеров, гудение вентиляторов, запах кофе."

#     polina "О, привет. Ты наш новый лаборант?"
#     artem "Рад, что кто-то ещё согласился на это."
#     nastya "Если умеешь паять — ты наш герой."

#     $ persistent.tasks.remove("Познакомиться с командой СТРАТЕГ")

#     "Ты ощущаешь странное чувство: как будто ты здесь уже бывал."

#     jump day1_exploration


# label day1_exploration:
#     $ time_of_day = "day"
#     call screen day1_map

# screen day1_map:
#     imagemap:
#         ground "images/map_day1_base.png"
#         idle "images/map_day1_idle.png"
#         hover "images/map_day1_hover.png"

#         hotspot (80,100,200,100) action Jump("day1_location_ploshad")
#         hotspot (300,150,200,100) action Jump("day1_location_dvor")
#         hotspot (500,250,200,100) action Jump("day1_location_bufet")
#         hotspot (700,300,200,100) action Jump("day1_location_kabinet")

# label day1_location_ploshad:
#     scene bg_ploshad_day
#     with dissolve

#     if not "Монета" in persistent.inventory:
#         "Ты замечаешь что-то блестящее между плит."
#         menu:
#             "Поднять предмет":
#                 $ persistent.inventory.append("Монета")
#                 "Старая монета с гербом... которого ты не узнаёшь."
#             "Оставить":
#                 "Ты проходишь мимо, что-то подсказывает — это важно."

#     "На скамейке кто-то курил недавно. Едва слышно доносится странный металлический шум из-за кустов."

#     call screen day1_map


# label day1_location_dvor:
#     scene bg_dvor
#     with dissolve

#     if not "Заметка: схема у фонтана" in persistent.notes:
#         "Под лавкой лежит бумажка, промокшая от капель."
#         $ persistent.notes.append("Заметка: схема у фонтана")
#         "На ней — фрагмент платы с непонятной формулой."

#     "Фонтан работает, но ритм капель сбивает дыхание. В кустах — обрывки старого отчёта."

#     call screen day1_map


# label day1_location_bufet:
#     scene bg_bufet
#     with dissolve

#     "Буфет полупуст. Старый телевизор в углу трещит от статики."

#     if not "Заметка: телевидение" in persistent.notes:
#         "Вдруг — картинка восстанавливается. Передача: «Новости науки». Год: 1997. Репортёр говорит твоё имя."
#         $ persistent.notes.append("Заметка: телевидение из прошлого")
#         "Ты чувствуешь озноб."

#     call screen day1_map


# label day1_location_kabinet:
#     scene bg_kabinet_strateg
#     with dissolve

#     menu:
#         "Поговорить с Полиной":
#             show polina neutral at center
#             polina "Будь осторожен с ЯСИМП. Она запоминает не только данные, но и... сны."
#         "Поговорить с Настей":
#             show nastya neutral at center
#             nastya "Если найдёшь обломки старой платы — принеси. Их нигде нет."
#         "Поговорить с Артёмом":
#             show artem neutral at center
#             artem "Мне показалось, что я видел лифт с этажом '-1'. Но это, наверное, от недосыпа."

#     call screen day1_map


# label day1_puzzle_light:
#     scene bg_lab_paper
#     "Ты раскладываешь найденные обрывки чертежей на столе."

#     "Они кажутся бессмысленными… пока не соединяешь их."

#     "Ты замечаешь повторяющийся символ. Это может быть простейший шифр."

#     "..."
#     "Ты вспоминаешь шифр Цезаря. Попробовать?"

#     menu:
#         "Да, попробовать расшифровать":
#             $ result = renpy.input("Введите предполагаемый сдвиг (1–9):", length=1)
#             if result == "3":
#                 "Шифр расшифрован! Получена фраза: «ЯСИМП готова. Не доверяй входу №4.»"
#                 $ persistent.notes.append("Шифр: не доверяй входу №4")
#             else:
#                 "Слишком много ошибок. Придётся попробовать позже."
#         "Нет, пока не трогать":
#             "Ты решаешь вернуться к этому позже."

#     jump day1_exploration


# label day1_evening_scene:
#     $ time_of_day = "evening"
#     scene bg_komnata_otdyha
#     with fade

#     "Ты возвращаешься в комнату отдыха. Тусклая лампа, старая мебель, шахматный стол."

#     show ilya tired at left
#     ilya "Непростой день, да? Ты молодец."

#     ilya "Если бы ты знал, сколько лаборантов приходило и исчезало..."

#     menu:
#         "Спросить, что он имеет в виду":
#             ilya "Они просто... уходили. Без следа. Без объяснений."
#         "Промолчать":
#             "Ты чувствуешь, как холод пробирается под кожу."

#     "Илья уходит, оставляя тебя одного. Лампа начинает мигать."

#     "На стене появляется надпись, которой не было: «СМОТРИ В СУТЬ»."

#     pause(2.0)
#     stop music fadeout 2.0

#     jump day1_end


# label day1_end:
#     scene bg_kabinet_strateg
#     with fade

#     "Ты возвращаешься в кабинет. Все разошлись."

#     "Ты ощущаешь, что это не просто работа."

#     "Слишком много совпадений. Слишком много неясностей."

#     "Словно что-то... смотрит на тебя через схемы, через экраны, через людей."

#     $ persistent.notes.append("День 1 завершён. Мир странный, но знакомый.")
#     $ persistent.tasks = []

#     show screen day_summary("День 1 завершён", persistent.notes, persistent.inventory)

#     return
