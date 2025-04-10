# label day3_intro:
#     $ day = 3
#     $ time_of_day = "morning"
#     $ persistent.tasks = ["Получить задание у Насти", "Разобраться с пультом", "Проверить сигналы"]
#     $ persistent.notes.append("Начался третий день. Что-то не так: всё кажется... знакомым")

#     scene bg_komnata_otdyha_morning
#     with slow_dissolve

#     play music "audio/ambience_room_repeat.ogg" fadein 2.0

#     "Ты открываешь глаза."

#     "Солнце светит под тем же углом, что и вчера. Пахнет кофе. Столик стоит также. Газета на полу... та же самая?"

#     "Ты поднимаешь газету."

#     if not "Газета с вчерашней датой" in persistent.notes:
#         $ persistent.notes.append("Газета с датой: вчера. Хотя был следующий день")
#         "Дата на ней — [date!r]... та, что была вчера."

#     "На стене висит жетон. Ты уверен — ты убирал его в карман. Он снова тут."

#     show ilya neutral at right with dissolve

#     ilya "Ты чего? Выглядишь так, как будто только что увидел привидение."

#     menu:
#         "Спросить, какой сегодня день":
#             ilya "Третий, вроде бы. Или... подожди. Полина говорила, что вчера был первый?"
#             $ persistent.notes.append("Илья не уверен, какой сегодня день")
#         "Спросить, был ли вчера разговор про архив":
#             ilya "Архив? Мы вроде пока не касались его. Почему спрашиваешь?"

#     "Ты чувствуешь, как разум буквально 'проскакивает' моментами — как будто кто-то вырезал куски из твоей памяти."

#     show polina neutral at left with dissolve

#     polina "Ты слышал вчера сигнал из пульта?"

#     "Ты молчишь. Она смотрит внимательнее."

#     polina "Иногда система откатывает события. Я не должна тебе этого говорить, но... если ты это замечаешь — ты уже часть."

#     menu:
#         "Что ты имеешь в виду?":
#             polina "Ты как... маяк. Ты резонируешь с событиями, как будто был здесь раньше."
#             $ persistent.notes.append("Полина называет игрока 'маяком'")
#         "Промолчать":
#             "Ты чувствуешь, что знаешь ответ. Но не можешь его сформулировать."

#     scene bg_kabinet_strateg
#     with dissolve

#     "Полина и Илья уходят. Настя копается в ящике с проводами."

#     show nastya smile at center with dissolve

#     nastya "О, ты вовремя. Этот пульт снова глючит. Поможешь проверить?"

#     "Она протягивает тебе старый серый блок с мигающей лампой. Метка на нём: **Р-107**."

#     $ persistent.inventory.append("Пульт Р-107")
#     $ persistent.notes.append("Получен пульт Р-107 от Насти")

#     nastya "Когда включаешь — он издаёт звуки. Как будто кто-то что-то шифрует."

#     nastya "Полина думает, это DTMF-код. Или просто глюк."

#     menu:
#         "Согласиться помочь":
#             "Ты берёшь пульт. Он тёплый. Слишком тёплый."
#         "Спросить, откуда он":
#             nastya "Нашли на складе. На нём был ярлык: «Не включать без внешнего фильтра». Конечно, Артём уже включал."

#     jump day3_task_pult

# label day3_task_pult:
#     scene bg_lab_desk_pult
#     with dissolve

#     play music "audio/ambience_signal_loop.ogg" fadein 1.0

#     "Ты включаешь пульт Р-107. Он щёлкает... и начинает издавать последовательность тонов."

#     "Частота неуловимо колеблется. Иногда кажется, что это просто шум. Иногда — будто кто-то говорит через старый модем."

#     "На корпусе — кнопки и динамик. Лампа мигает в такт."

#     play sound "audio/dtmf_sequence.ogg"

#     "Звуки напоминают старые телефонные коды. DTMF?"

#     $ persistent.notes.append("Пульт Р-107 воспроизводит DTMF-подобный сигнал")

#     menu:
#         "Записать сигнал":
#             $ persistent.inventory.append("Распечатка сигнала Р-107")
#             "Ты записываешь последовательность: **3, 1, 2, 4, 7, 9, 6, #**"
#         "Прослушать ещё раз":
#             play sound "audio/dtmf_sequence.ogg"
#             "Ты снова слышишь тот же сигнал."
#         "Попробовать расшифровать":
#             jump day3_puzzle_signal
#         "Отключить пульт":
#             "Ты выключаешь пульт. Лампа медленно гаснет."
#             $ persistent.notes.append("Игрок отказался от расшифровки сигнала")
#             jump day3_free_roam


# label day3_puzzle_signal:
#     scene bg_lab_desk_pult_close
#     with fade

#     play music "audio/low_click_loop.ogg" fadein 1.0

#     "Ты открываешь блокнот и записываешь последовательность тонов, прозвучавших из пульта."

#     show text "Сигнал: 3, 1, 2, 4, 7, 9, 6, #" with dissolve

#     "Каждая цифра соответствует DTMF-кнопке. Возможно, это буквенный код?"

#     $ dtmf_map = {
#         "1": " ",
#         "2": "ABC",
#         "3": "DEF",
#         "4": "GHI",
#         "5": "JKL",
#         "6": "MNO",
#         "7": "PQRS",
#         "8": "TUV",
#         "9": "WXYZ",
#         "0": " ",
#         "*": "*",
#         "#": "#"
#     }

#     "Ты вспоминаешь: старые телефонные панели привязывали буквы к цифрам. Но какие именно буквы выбрать?"

#     $ puzzle_attempts = 0

# label signal_input_loop:

#     $ answer = renpy.input("Введите предполагаемое слово из сигнала:", length=16)
#     $ answer = answer.strip().upper()
#     $ puzzle_attempts += 1

#     if answer == "RESONANT":
#         "Слово «RESONANT» вспыхивает у тебя в голове, будто зажигается изнутри."

#         $ persistent.notes.append("Ключевое слово: RESONANT — возможно, имя или команда")
#         $ persistent.inventory.append("Кодовая фраза: RESONANT")

#         play sound "audio/success_chime.ogg"
#         "Лампа на пульте загорается ровным светом. Пульт больше не шумит."

#         jump day3_free_roam

#     elif puzzle_attempts >= 3:
#         "Ты уже третий раз вводишь неверный вариант."

#         menu:
#             "Попросить подсказку у Полины":
#                 show polina thinking at center
#                 polina "Если использовать DTMF и первую букву для каждой цифры, получим: DADGPRS#"
#                 polina "Но если взять средние буквы…"
#                 $ persistent.notes.append("Подсказка: использовать средние буквы с DTMF-клавиш")
#                 jump signal_input_loop
#             "Попробовать ещё раз":
#                 jump signal_input_loop
#     else:
#         "Нет, это не то. Попробуй ещё."
#         jump signal_input_loop


# label day3_free_roam:
#     $ time_of_day = "day"
#     "После расшифровки сигнала ты чувствуешь странную вибрацию — будто здание… живое."

#     $ persistent.notes.append("После сигнала всё стало казаться… искажённым")

#     call screen day3_map

# screen day3_map:
#     imagemap:
#         ground "images/map_day3_base.png"
#         idle "images/map_day3_idle.png"
#         hover "images/map_day3_hover.png"

#         hotspot (80,100,200,100) action Jump("day3_location_ploshad")          # Площадь
#         hotspot (300,150,200,100) action Jump("day3_location_bufet")           # Буфет
#         hotspot (500,200,200,100) action Jump("day3_location_kabinet")         # Кабинет
#         hotspot (680,260,200,100) action Jump("day3_location_buhgalteriya")    # Бухгалтерия
#         hotspot (300,400,200,100) action Jump("day3_location_lestnica")        # Лестница
#         hotspot (750,380,200,100) action Jump("day3_location_dvor")            # Двор
#         hotspot (880,80,100,100) action Jump("day3_evening_memory_shift")      # Конец дня

# label day3_location_ploshad:
#     scene bg_ploshad_day
#     with dissolve

#     "Ты стоишь на площади. Всё как в первый день… но урна теперь справа, а не слева."

#     "На табличке слово «исследовательский» стёрто. Осталась надпись: «институт универс..._»"

#     if not "Изменения на площади" in persistent.notes:
#         $ persistent.notes.append("Площадь изменилась: расположение объектов и таблички нарушено")

#     call screen day3_map

# label day3_location_bufet:
#     scene bg_bufet
#     with dissolve

#     "Буфет почти пуст. На экране — снова «Новости науки». Но диктор… смотрит прямо на тебя."

#     "Он говорит твоим голосом: «Ты уже здесь. Почему ты вернулся?»"

#     $ persistent.notes.append("На экране буфета диктор говорит голосом игрока")

#     call screen day3_map

# label day3_location_kabinet:
#     scene bg_kabinet_strateg
#     with dissolve

#     "Полина, Артём и Настя... снова говорят фразы, которые ты слышал вчера."

#     menu:
#         "Прервать их":
#             "Они зависают, как будто не знают, как реагировать."
#             show polina glitch at center
#             polina "…про…цесс… перезапуск…"
#             $ persistent.notes.append("Слова команды повторяются. Признаки сбоя.")
#         "Послушать":
#             "Словно сцена проигрывается повторно. Даже интонации одинаковые."

#     call screen day3_map

# label day3_location_buhgalteriya:
#     scene bg_buhgalteriya
#     with dissolve

#     show katya neutral at right

#     katya "Ты снова за платёжкой?"

#     menu:
#         "Сказать, что уже получал":
#             katya "Ты уверен? Я тебя впервые вижу."
#         "Промолчать":
#             "Катя смотрит внимательно. «Ты кажешься знакомым. Тот же взгляд. Только тише.»"

#     if not "Бухгалтерия сбоит во времени" in persistent.notes:
#         $ persistent.notes.append("Катя не помнит встречи. Возможно, петля.")

#     call screen day3_map

# label day3_location_lestnica:
#     scene bg_lestnica_dark
#     with fade

#     "Ты идёшь по лестнице. Свет погас. Шаги звучат двойным эхом — но ты идёшь один."

#     "На стене появляется слово: «ВНУТРИ» — оно светится как флуоресцентная краска."

#     "На ступеньке — сломанные часы. Стрелки движутся назад."

#     $ persistent.inventory.append("Сломанные часы")
#     $ persistent.notes.append("Лестница: надпись ВНУТРИ, стрелки назад")

#     call screen day3_map

# label day3_location_dvor:
#     scene bg_dvor
#     with dissolve

#     "Во дворе — странная тишина. Даже птицы не поют."

#     "Ты замечаешь силуэт вдалеке. Он машет рукой. Моргаешь — он исчезает."

#     menu:
#         "Подойти":
#             "Ты подходишь к кустам. Там пусто. Только платок с монограммой «R». Он пахнет химией."
#             $ persistent.inventory.append("Платок R")
#             $ persistent.notes.append("Силуэт во дворе исчез. Оставлен платок.")
#         "Уйти":
#             "Ты не рискуешь приближаться. Что-то в этом слишком знакомо."

#     call screen day3_map

# label day3_evening_memory_shift:
#     $ time_of_day = "evening"

#     scene bg_komnata_otdyha_evening
#     with slow_dissolve

#     play music "audio/ambience_disoriented_loop.ogg" fadein 2.0

#     "Ты возвращаешься в комнату отдыха. Свет лампы тускнеет, мигает. Комната кажется чуть иначе обставленной, чем утром."

#     "Ковёр другой. Шахматная доска повёрнута. На полке нет книги, которую ты читал."

#     "Ты садишься. Закрываешь глаза."

#     pause(1.5)

#     "Когда открываешь — всё снова как было с самого начала. Абажур старый, книга на месте. Только... на стене мелом:"

#     show text "КОГДА ТЫ ПОСЛЕДНИЙ РАЗ СПАЛ?" with dissolve

#     "Ты не помнишь. Ни сегодня. Ни вчера. Ни никогда."

#     show polina neutral at left with dissolve

#     polina "Ты чувствуешь это, да? Мир не двигается. Он просто… обновляется."

#     menu:
#         "Ты о петле?":
#             polina "Не совсем. Это скорее эхо. Или тест. Мы могли бы говорить об этом иначе, но боюсь — тогда всё сбросится."
#             $ persistent.notes.append("Полина намекает на тестовую реальность")
#         "Спросить, кто её заставил молчать":
#             polina "Нам запрещено знать, что мы знаем."

#     "Она садится рядом. В её взгляде — сожаление. Или отчёт?"

#     polina "Ты держишь форму лучше, чем предыдущий. Он не справился с третьим днём."

#     menu:
#         "Спросить, чем он закончился":
#             polina "Для него — ничем. Для нас — перезапуском."

#     "Полина протягивает тебе жетон. Такой же, как был у тебя в инвентаре."

#     if "Жетон без надписи" in persistent.inventory:
#         "Теперь у тебя их два. Совершенно одинаковых. Абсолютно симметричных."
#         $ persistent.notes.append("Игрок держит два одинаковых жетона. Один из них... откуда?")
#     else:
#         $ persistent.inventory.append("Жетон без надписи")
#         $ persistent.notes.append("Жетон появился снова. Мир цикличен.")

#     scene bg_komnata_otdyha_dark
#     with fade

#     "Ты засыпаешь. Или, скорее, выключаешься."

#     "Перед тем как закрыть глаза, ты видишь над диваном надпись:"

#     show text "YACMP: Подготовка к ВЫБОРУ активна. 93%." with slow_dissolve

#     stop music fadeout 3.0

#     jump day3_end

# label day3_end:
#     $ time_of_day = "night"

#     scene black
#     with fade

#     play sound "audio/page_flip.ogg"
#     pause 1.0

#     "Ты больше не различаешь сны и явь."

#     "Когда ты спишь — ты ощущаешь движение. Когда ты бодрствуешь — всё замирает."

#     scene bg_notebook_dark
#     with slow_dissolve

#     "Ты открываешь блокнот. Новая запись, сделанная не твоим почерком."

#     show text "Если ты это читаешь — значит, меня уже нет." with dissolve

#     menu:
#         "Продолжить читать":
#             "Ниже — фрагмент схемы. Это пульт. Тот, что у тебя. Но с другой маркировкой."
#             "Под ним — фраза: «НЕ СИНХРОНИЗИРУЙ ДО КОНЦА». И подпись: «R». Или «Я»?"

#     $ persistent.notes.append("Чужая запись в блокноте: 'меня уже нет'")
#     $ persistent.tasks = []
#     $ persistent.completed_days.append(3)

#     stop music fadeout 2.0

#     show screen day_summary("День 3 завершён", persistent.notes, persistent.inventory)

#     "В следующем цикле ты должен быть осторожнее. Теперь система знает, что ты знаешь."

#     return
