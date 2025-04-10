# label day2_intro:
#     $ day = 2
#     $ time_of_day = "morning"
#     $ persistent.tasks = ["Найти архивный отчёт для Полины", "Вернуться с результатами"]
#     $ persistent.notes.append("Илья хочет, чтобы ты нашёл старый отчёт для Полины")

#     scene bg_komnata_otdyha_morning
#     with fade

#     play music "audio/ambience_room_morning.ogg" fadein 1.5

#     "Ты просыпаешься... но не на том диване, что вчера."

#     "Ты не помнишь, как заснул. Подушка пахнет табаком. Стоп... это же место, где спал Артём."

#     "Ты садишься. Свет тусклый, за окном — утро, но часы показывают 4:12."

#     show ilya neutral at center with dissolve

#     ilya "Доброе утро. Или всё ещё ночь — я сам уже не уверен."

#     menu:
#         "Спросить, который час на самом деле":
#             ilya "У нас тут время иногда не совпадает. Но ты привыкай."
#         "Промолчать":
#             "Ты киваешь. Голова гудит."

#     ilya "Слушай, Полине нужно кое-что из архива. Древний отчёт по ССЛ. Без него она не сможет доделать алгоритм."

#     $ persistent.notes.append("Архив содержит данные по ССЛ, нужные Полине")

#     ilya "Тебе нужен ключ. Вот он. Не теряй — его нет в учёте."

#     $ persistent.inventory.append("Ключ от архивного шкафа")

#     menu:
#         "Взять задание":
#             "Ты берёшь ключ. Почему-то рука дрожит."
#         "Спросить, что такое ССЛ":
#             $ persistent.notes.append("ССЛ — Система Самостоятельной Логики")
#             ilya "Самая странная штука, с которой мы работали. Она думает лучше, чем мы. Или… глубже."

#     jump day2_task_archive


# label day2_task_archive:
#     scene bg_koridor_3etazh
#     with fade

#     play music "audio/ambience_corridor.ogg" fadein 2.0

#     "Коридор третьего этажа кажется длиннее, чем должен быть. Шаги гулко отдаются от стен."

#     "Ты проходишь мимо табличек: «Методический фонд», «Брошюры 70-х», «ССЛ — архив»."

#     scene bg_arhiv
#     with dissolve

#     "В архиве прохладно. Запах пыли, старой бумаги и... озона?"

#     if "Ключ от архивного шкафа" in persistent.inventory:
#         "Ты находишь нужный шкаф. Замок ржавый, но ключ поворачивается."

#         $ persistent.inventory.remove("Ключ от архивного шкафа")

#         "Шкаф со скрипом открывается. Внутри — пачка отчётов. Один выделяется: обгоревший край, штамп «СТРАТЕГ 1987», надпись от руки: «Не передавать Мурашову»."

#         $ persistent.inventory.append("Обгоревший отчёт")
#         $ persistent.notes.append("Отчёт 1987 года из СТРАТЕГ, скрыт от Мурашова")

#         "На внутренней стороне — сложный узор, напоминающий шифр. Некоторые буквы подчёркнуты."

#         show polina neutral at right with dissolve

#         polina "Ты уже здесь? Я как раз хотела помочь."

#         menu:
#             "Показать отчёт":
#                 polina "Стоп. Это... настоящий отчёт по первой версии ССЛ?"
#                 polina "Значит, они действительно пытались активировать «альфа-модель» ещё до 90-х..."
#                 $ persistent.notes.append("ССЛ-α существовала задолго до текущего проекта")

#             "Спрятать отчёт":
#                 "Ты решаешь пока не говорить ей. Что-то подсказывает — нужно быть осторожным."

#         polina "Ладно. Давай разберёмся с шифром. Там, кажется, комбинация Цезаря и Виженера. Справишься?"

#     else:
#         "Шкаф закрыт. Без ключа ты ничего не сделаешь."
#         return

#     jump day2_puzzle_document


# label day2_puzzle_document:
#     scene bg_lab_desk_papers
#     with dissolve

#     "Ты раскладываешь отчёт на столе. На обороте страницы — зашифрованный текст."

#     show text "F DSRJWSI XLMW JVSQ EWZMI. QEWI 'FVWXSV' 197. RIXIVMQI." at center with fade

#     "Некоторые буквы подчёркнуты, рядом приписка: «Ключ: ПРЕДЕЛ»."

#     $ puzzle_attempts = 0

# label puzzle_attempt_loop:

#     $ cipher_input = renpy.input("Попробуй расшифровать. Введи расшифрованную фразу или 'подсказка':", length=80)
#     $ cipher_input = cipher_input.strip().lower()
#     $ puzzle_attempts += 1

#     if "помни это имя" in cipher_input or "помни имя мазви" in cipher_input:
#         "Ты чувствуешь, как строчка оживает у тебя в голове."

#         $ persistent.notes.append("Фраза: Помни это имя. Мазви. Место 'Первый' — 197.")
#         $ persistent.inventory.append("Зашифрованный фрагмент")

#         show polina smile at right
#         polina "Ты справился! Это фраза из легенды ССЛ-альфа. Никто не знал, откуда она появилась."

#         polina "Ты даже не представляешь, насколько это важно..."

#         jump day2_free_roam

#     elif cipher_input == "подсказка" and puzzle_attempts <= 2:
#         "Подсказка: попробуй сначала сдвиг Цезаря на 4, а потом применить ключевое слово ПРЕДЕЛ."

#         jump puzzle_attempt_loop

#     elif puzzle_attempts >= 3:
#         "Полина берёт бумагу."

#         show polina sad at right
#         polina "Сложно? Давай я помогу... хотя лучше бы ты сам..."

#         "Она что-то быстро шепчет себе под нос и пишет расшифрованную строчку:"

#         show text "Помни это имя. Мазви. Место 'Первый' — 197." at center

#         $ persistent.notes.append("Фраза: Помни это имя. Мазви. Место 'Первый' — 197.")
#         $ persistent.inventory.append("Зашифрованный фрагмент")

#         jump day2_free_roam

#     else:
#         "Неверно. Попробуй ещё раз."
#         jump puzzle_attempt_loop

# label day2_end:
#     $ time_of_day = "night"

#     scene black
#     with fade

#     play sound "audio/page_flip.ogg"
#     pause 1.0

#     "Ты просыпаешься среди ночи от чувства, что кто-то стоит рядом."

#     "Но никого нет."

#     scene bg_notebook_dark
#     with slow_dissolve

#     "Ты открываешь блокнот. На последней странице — строчка, написанная твоим почерком."

#     show text "Я снова здесь." with dissolve

#     menu:
#         "Закрыть блокнот":
#             "Ты медленно закрываешь его. Сердце стучит громче обычного."

#     $ persistent.tasks = []
#     $ persistent.notes.append("В конце второго дня надпись в блокноте появилась сама")
#     $ persistent.completed_days.append(2)

#     stop music fadeout 2.0

#     show screen day_summary("День 2 завершён", persistent.notes, persistent.inventory)

#     "Завтра ты продолжишь поиски ответов. Или они найдут тебя."

#     return
