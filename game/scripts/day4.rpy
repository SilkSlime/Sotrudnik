# label day4_intro:
#     $ day = 4
#     $ time_of_day = "morning"
#     $ persistent.tasks = ["Получить доступ в магнитную комнату", "Откалибровать узел", "Вернуться в кабинет СТРАТЕГ"]
#     $ persistent.notes.append("Четвёртый день начался не как обычно. Что-то в мире изменилось.")

#     scene bg_black
#     with fade

#     play music "audio/ambience_reverse.ogg" fadein 1.5

#     "Ты просыпаешься в полной темноте. Но... глаза открыты."

#     "Звук — как сквозь вату. Кажется, всё играет задом наперёд."

#     "На потолке (или полу?) — надпись. Она светится. Ты читаешь её вверх ногами."

#     show text "НЕ ВЫХОДИ ВНЕ ПОЛОЖЕННОГО" with dissolve

#     pause(1.5)

#     scene bg_komnata_otdyha_glitched
#     with glitch_fade

#     "Ты сидишь в комнате отдыха. Но свет от лампы пульсирует нереальным ритмом. Диван дёргается, как будто под видеофильтром."

#     "Ты пытаешься вспомнить вчера… но всё перепутано."

#     show screen system_message("НОВАЯ СИНХРОНИЗАЦИЯ: НЕ УДАЛАСЬ. ОЖИДАНИЕ…")

#     pause(2.0)
#     hide screen system_message

#     "Внезапно из стены доносится голос. Не голос. Команда?"

#     play sound "audio/system_prompt.ogg"

#     voice "Подтвердите идентификатор: 197.001-бета. Подтвердите активацию."

#     menu:
#         "Подтвердить":
#             $ persistent.notes.append("Игрок подтвердил ID 197.001-бета — система распознала")
#             voice "Субъект идентифицирован. Вмешательство разрешено. Переназначение протоколов: активно."
#         "Отказаться":
#             $ persistent.notes.append("Игрок отказался подтверждать ID — последствия неизвестны")
#             voice "Нарушение процедуры. Частичная синхронизация принудительно активирована."

#     scene bg_kabinet_strateg_empty
#     with slow_dissolve

#     "Ты оказываешься в кабинете СТРАТЕГ. Но тут никого нет. Мониторы включены. Окна открыты. На полу — следы."

#     "На экране терминала мигает строка:"

#     show text "ПЕРЕЙДИ В КОМНАТУ МАГНИТНОГО УЗЛА" with dissolve

#     $ persistent.notes.append("Система требует калибровку магнитного узла")

#     jump day4_lab_glitch

# label day4_lab_glitch:
#     scene bg_kabinet_strateg_empty
#     with fade

#     play music "audio/ambience_magnetic_loop.ogg" fadein 2.0

#     "Ты стоишь один в кабинете «СТРАТЕГ». Шум вентиляции отсутствует. Экран терминала мерцает, хотя ЭВМ отключена от сети."

#     "Стол Полины накрыт белой тканью. Но ты точно видел, как она вчера здесь сидела."

#     "На стенде с логотипом «ССЛ — больше, чем логика» — теперь другая надпись:"

#     show text "Я ЕСМЬ ВНЕ" with dissolve
#     pause(1.5)

#     "Ты подходишь к системному блоку, который вчера был выключен. Сейчас он работает — без питания."

#     "Экран показывает системный лог:"

#     show screen system_terminal("""
#     SYSTEM CORE LOG:
#     --- ERROR STACK 197 ---
#     :: MEMORY BLOCK UNBOUND ::
#     :: ENTITY [BETA] ACTIVE ::
#     :: LOCATION: MAGNETIC CORE UNSTABLE ::
#     """)

#     pause(4.0)
#     hide screen system_terminal

#     "В углу комнаты мигает синий огонёк. Вчера его не было. Подойдя ближе, ты находишь пластиковую карту."

#     $ persistent.inventory.append("Повреждённая карта доступа")
#     $ persistent.notes.append("Повреждённая карта ведёт к неизвестному уровню")

#     "На карте — надпись: «Δ CORE ZONE» и инициал «R.»"

#     "Ты решаешь проверить лифт. Может, это даст доступ к новым уровням."

#     scene bg_lift
#     with dissolve

#     play sound "audio/lift_startup_corrupt.ogg"

#     "Лифт откликается мгновенно. Панель кнопок моргает. Среди них — новая кнопка, обозначенная греческой буквой Δ."

#     menu:
#         "Нажать кнопку Δ":
#             "Ты нажимаешь. Лифт дрожит, резко гаснет свет. Потом — резкое движение вниз."
#             $ persistent.notes.append("Лифт повёл на уровень Δ — вне карты института")
#         "Попробовать другие кнопки":
#             "Ничего не происходит. Кажется, Δ — единственный активный вариант."

#     scene bg_magnetic_door
#     with fade

#     play music "audio/low_magnetic_buzz.ogg" fadein 2.0

#     "Ты оказываешься в коридоре, стены которого покрыты графитом и медными полосами. Воздух пахнет железом и чем-то... синтетическим."

#     "На стене — знак: «Комната магнитного узла. Только для допущенных. Перепроверка вектора – ОБЯЗАТЕЛЬНА»"

#     if "Повреждённая карта доступа" in persistent.inventory:
#         "Ты прикладываешь карту к сканеру. Он мигает жёлтым, а потом открывает дверь."

#         scene bg_magnetic_room
#         with dissolve

#         "Ты входишь в магнитную комнату. Пространство внутри не соответствует внешнему размеру. Здесь больше, чем может быть."

#         "В центре — стоячая волна, замкнутый узор из колеблющихся форм. Вокруг — пульты, ручки, дисплеи."

#         $ persistent.notes.append("Комната магнитного узла нарушает геометрию и логику пространства")

#         "На стенде — инструкция: «Настроить резонансную частоту, сохранить стабильность ядра»."

#         $ persistent.tasks.remove("Получить доступ в магнитную комнату")
#         $ persistent.tasks.append("Выполнить калибровку частоты")

#         jump day4_puzzle_frequency_gate
#     else:
#         "Сканер мигает красным. Ты не можешь войти. Карта повреждена слишком сильно."

#         "Пока ничего не поделаешь. Возможно, есть другой способ проникнуть внутрь позже."
#         jump day4_free_roam

# label day4_puzzle_frequency_gate:
#     scene bg_magnetic_room_center
#     with fade

#     play music "audio/frequency_oscillation.ogg" fadein 2.5

#     "Ты стоишь в центре магнитной комнаты."

#     "Вокруг — панели, рычаги, дисплеи с колеблющимися графиками. Всё пульсирует. В середине — светящаяся фигура, форма которой постоянно меняется."

#     "Ты видишь надпись:"

#     show text "ИНСТРУКЦИЯ: ВЫБЕРИ ПРАВИЛЬНУЮ ЧАСТОТУ. ПОДБЕРИ РЕЗОНАНС. НЕ ПЕРЕКАЛИБРОВЫВАЙ БОЛЕЕ 3 РАЗ." with dissolve
#     pause(2.0)

#     "На панели — 7 регуляторов с подписями:"

#     show screen calibration_panel

# screen calibration_panel:
#     vbox:
#         xalign 0.5
#         yalign 0.2
#         spacing 15

#         text "Выберите частоту:"
#         textbutton "113.2 МГц — Чисто" action Jump("calibration_113")
#         textbutton "129.9 МГц — Сдвиг ↑" action Jump("calibration_129")
#         textbutton "141.0 МГц — Стабильно" action Jump("calibration_141")  # ← правильная
#         textbutton "159.3 МГц — Дрожание" action Jump("calibration_159")
#         textbutton "176.7 МГц — Тон утончается" action Jump("calibration_176")
#         textbutton "201.8 МГц — Искажение ↑↑" action Jump("calibration_201")
#         textbutton "Отойти от панели" action Jump("day4_free_roam")

# # Варианты частот

# label calibration_113:
#     play sound "audio/freq_wrong1.ogg"
#     "На экране вспыхивает красный крест. Контур пульсирующей фигуры становится неустойчивым."
#     $ persistent.notes.append("Попытка 1: 113.2 МГц — слишком чисто")
#     $ persistent.calibration_attempts = getattr(persistent, "calibration_attempts", 0) + 1
#     if persistent.calibration_attempts >= 3:
#         jump calibration_failure
#     else:
#         jump day4_puzzle_frequency_gate

# label calibration_129:
#     play sound "audio/freq_wrong2.ogg"
#     "График резко подскакивает вверх. Возникает резонансный гул."
#     $ persistent.notes.append("Попытка 2: 129.9 МГц — перегрузка в верхнем регистре")
#     $ persistent.calibration_attempts += 1
#     if persistent.calibration_attempts >= 3:
#         jump calibration_failure
#     else:
#         jump day4_puzzle_frequency_gate

# label calibration_141:
#     play sound "audio/freq_correct.ogg"
#     stop music fadeout 1.5
#     scene bg_magnetic_room_calm
#     with dissolve

#     "График стабилизируется. Центр фигуры выравнивается, превращаясь в почти круглый импульс."

#     "На стене появляется надпись:"

#     show text "РЕЗОНАНС ДОСТИГНУТ. УРОВЕНЬ ПОДТВЕРЖДЁН: 141.0 МГц" with dissolve
#     pause(1.5)

#     play sound "audio/unlock_gate.ogg"

#     "За стеной сдвигается панель. За ней — тёмный коридор. Из него идёт ровное сияние и еле различимый низкий голос:"

#     voice "ты_готов.следующий_узел.ожидает"

#     $ persistent.notes.append("Узел калиброван. Доступ к следующему сегменту открыт")
#     $ persistent.tasks.remove("Выполнить калибровку частоты")

#     jump day4_free_roam

# label calibration_159:
#     play sound "audio/freq_wrong3.ogg"
#     "Появляется дрожание. Форма структуры начинает колебаться всё быстрее, как будто готовится к распаду."
#     $ persistent.notes.append("Попытка: 159.3 МГц — дрожание структуры")
#     $ persistent.calibration_attempts += 1
#     if persistent.calibration_attempts >= 3:
#         jump calibration_failure
#     else:
#         jump day4_puzzle_frequency_gate

# label calibration_176:
#     play sound "audio/freq_whisper.ogg"
#     "Звук почти исчезает. Всё становится слишком тихим. Панель гаснет на 2 секунды."
#     $ persistent.notes.append("Попытка: 176.7 МГц — исчезновение сигнала")
#     $ persistent.calibration_attempts += 1
#     if persistent.calibration_attempts >= 3:
#         jump calibration_failure
#     else:
#         jump day4_puzzle_frequency_gate

# label calibration_201:
#     play sound "audio/freq_distortion.ogg"
#     "Искажение усиливается. Всё вокруг мерцает, как старое видео. Появляются рваные образы людей в белых халатах."
#     $ persistent.notes.append("Попытка: 201.8 МГц — тяжёлое искажение, зрительный сбой")
#     $ persistent.calibration_attempts += 1
#     if persistent.calibration_attempts >= 3:
#         jump calibration_failure
#     else:
#         jump day4_puzzle_frequency_gate

# label calibration_failure:
#     stop music fadeout 2.0
#     play sound "audio/error_fail.ogg"

#     scene bg_magnetic_room_shutdown
#     with glitch_fade

#     "Панель гаснет. Свет тухнет. Фигура в центре вздрагивает и распадается."

#     show text "КАЛИБРОВКА ПРОВАЛЕНА. ОБРАТИТЕСЬ В СИСТЕМУ." with dissolve
#     pause(2.5)

#     $ persistent.notes.append("Калибровка провалена. Возможно, последствия позже")

#     jump day4_free_roam

# label day4_free_roam:
#     $ time_of_day = "day"
#     $ persistent.notes.append("Мир стал вести себя иначе. Реальность реагирует на тебя")

#     "После калибровки всё изменилось."

#     "Ты ощущаешь, что локации не просто связаны — они смотрят на тебя. Следят. Отвечают."

#     call screen day4_glitch_map

# screen day4_glitch_map:
#     imagemap:
#         ground "images/map_day4_base.png"
#         idle "images/map_day4_idle.png"
#         hover "images/map_day4_hover.png"

#         hotspot (80,100,200,100) action Jump("day4_location_bufet")
#         hotspot (280,120,200,100) action Jump("day4_location_buhgalteriya")
#         hotspot (500,160,200,100) action Jump("day4_location_lestnica")
#         hotspot (680,240,200,100) action Jump("day4_location_kabinet")
#         hotspot (300,320,200,100) action Jump("day4_location_dvor")
#         hotspot (760,360,200,100) action Jump("day4_location_cafe")
#         hotspot (860,80,100,100) action Jump("day4_evening_interference") # конец дня

# label day4_location_bufet:
#     scene bg_bufet_corrupted
#     with dissolve

#     play music "audio/broken_radio.ogg"

#     "Буфет. Всё на своих местах. Но цвета поменялись местами. Меню на латыни."

#     "Телевизор показывает пустой экран, но ты слышишь:"

#     voice "Изменение подтверждено. Переменная [197.001.бета] нестабильна."

#     $ persistent.notes.append("Буфет зациклился. Меню на латыни, а голос системы — в прямом эфире")

#     "Ты поворачиваешься — и видишь себя сидящим за соседним столом."

#     menu:
#         "Подойти к себе":
#             "Ты встаёшь… и ничего нет. Место пусто. Только зеркало. Когда ты его поставил?"
#             $ persistent.notes.append("Видел себя в буфете — возможно, остаточное эхо")
#         "Уйти":
#             "Ты выходишь, не глядя по сторонам."

#     call screen day4_glitch_map


# label day4_location_buhgalteriya:
#     scene bg_buhgalteriya
#     with dissolve

#     show katya glitch at right

#     katya "Вы снова? Мы не выдаём документы дважды. Подписано: вы же это вы."

#     menu:
#         "Спросить, что она имеет в виду":
#             katya "Ваш договор — от [persistent.date_started], но зарегистрирован в 2022. Совпадений не бывает."
#             $ persistent.notes.append("Катя называет дату оформления, которую ты не помнишь")
#         "Промолчать":
#             "Катя открывает сейф и достаёт пустой лист бумаги. Печатает: «ПОДПИСАНО»"

#     "Ты получаешь распечатку, на которой — только твоя подпись."

#     $ persistent.inventory.append("Бумага с подписью, появившейся сама")
#     $ persistent.notes.append("Катя дала документ без текста. Только подпись.")

#     call screen day4_glitch_map

# label day4_location_lestnica:
#     scene bg_lestnica_dark
#     with dissolve

#     play sound "audio/reverse_steps.ogg"

#     "Ты поднимаешься по лестнице. Но каждый раз, выходя на новый пролёт — ты попадаешь на тот же."

#     "Ты оставляешь бумажку на ступеньке. Поднимаешься. Она уже на следующем пролёте."

#     "Ты пытаешься вернуться назад — и снова оказываешься на том же пролёте."

#     $ persistent.notes.append("Лестница стала зацикленной. Петля внутри петли.")

#     menu:
#         "Бежать вверх":
#             "Ты бежишь. Но ничего не меняется. Потом — темнота. Потом — ты стоишь внизу."
#         "Сесть на ступеньку":
#             "Ты сидишь. Слышен стук шагов сверху. Очень медленно. Очень… знакомо."

#     call screen day4_glitch_map

# label day4_location_kabinet:
#     scene bg_kabinet_strateg
#     with dissolve

#     "Команда на месте. Но ты их не слышишь. Они говорят, как в немом кино."

#     show polina glitch at left
#     show artem glitch at right
#     show nastya glitch at center

#     "Движения повторяются. Полина смотрит в камеру. Потом снова. Снова. И снова."

#     menu:
#         "Взглянуть на экран Артёма":
#             "На экране открыт каталог: `~/петля/второй/архив/197/`"
#             $ persistent.notes.append("Появился каталог 'петля/второй/архив/197'")
#         "Подойти к Насте":
#             "Она тебя не замечает. Только когда ты стоишь рядом — она произносит: «Пожалуйста. Не выбирай...»"

#     call screen day4_glitch_map

# label day4_location_cafe:
#     scene bg_cafe_dark
#     with dissolve

#     play music "audio/cafe_static.ogg"

#     "В кафе всё замерло. В углу сидит человек в костюме 50-х годов. Он не двигается."

#     "Ты смотришь на него. Он поворачивает голову… слишком плавно. Улыбается."

#     voice "Наблюдение активно. Подготовка завершена."

#     menu:
#         "Спросить, кто он":
#             "Ты открываешь рот, но слов нет. Он кивает, словно понял. Исчезает."
#             $ persistent.notes.append("Гость в кафе реагирует на игрока. Исчезает после контакта")
#         "Уйти":
#             "Ты быстро покидаешь кафе. Свет там остался включён."

#     call screen day4_glitch_map


# label day4_evening_interference:
#     $ time_of_day = "evening"

#     scene black
#     with fade
#     stop music fadeout 2.0

#     "Ты возвращаешься… или тебя возвращают?"

#     "Ты не помнишь, как оказался здесь. Комната пуста. Экран включён."

#     scene bg_terminal_dark
#     with slow_dissolve

#     "На экране мигает зелёный текст."

#     show screen system_terminal("""
#     ::: ВНИМАНИЕ :::

#     СУБЪЕКТ 197.001-БЕТА ОПРЕДЕЛЁН КАК:
#     - НЕПРЕДСКАЗУЕМЫЙ
#     - ИНИЦИАТИВНЫЙ
#     - КОНТУРНЫЙ

#     ВЫХОД ИЗ ПЕТЛИ — ДОСТУПЕН

#     // ПРОДОЛЖИТЬ УЧАСТИЕ?
#     [ 1 ] ОСТАВАТЬСЯ ВНУТРИ
#     [ 2 ] ИСКАТЬ ВЫХОД
#     """)

#     pause(4.0)

#     hide screen system_terminal

#     "Ты чувствуешь, как пространство вокруг замирает. Ни звука. Ни дыхания. Только ты и... наблюдение."

#     play sound "audio/system_voice.ogg"

#     voice "Сделай выбор, [СУБЪЕКТ_197_001], но знай — мы уже знаем результат."

#     menu:
#         "1 — ОСТАВАТЬСЯ ВНУТРИ":
#             $ persistent.choice_system_path = "stay"
#             $ persistent.notes.append("Выбран путь: оставаться внутри. Система одобряет.")
#             show text "ПРИНЯТО. ВЫ БУДЕТЕ ЗАЩИЩЕНЫ." with dissolve
#         "2 — ИСКАТЬ ВЫХОД":
#             $ persistent.choice_system_path = "exit"
#             $ persistent.notes.append("Выбран путь: искать выход. Система регистрирует отклонение.")
#             show text "ЗАПИСАНО. ВОЗВРАТ НЕВОЗМОЖЕН." with dissolve

#     pause(2.0)

#     "Экран гаснет. Из динамика слышен тяжёлый рёв — не технический. Живой?"

#     scene bg_komnata_otdyha_dark
#     with dissolve
#     play music "audio/night_low_tension.ogg" fadein 2.0

#     "Ты сидишь на диване. Но диван — теперь другой. Темнее. Тверже. Как будто… не для сна, а для фиксации."

#     "Ты открываешь блокнот. Он уже записан. На последней странице — строки, которые ты не писал:"

#     show text """
#     ТЫ УЖЕ СДЕЛАЛ ЭТО.
#     ПРОСТО НЕ ПОМНИШЬ.
#     ТВОЙ ВЫБОР — ВТОРОЙ.
#     ТЫ ВЫБРАЛ ВЫХОД.
#     ПОЭТОМУ ОНИ ВЕРНУЛИ ТЕБЯ.
#     """ with dissolve

#     pause(4.0)

#     "Свет выключается. Слышно: кто-то в комнате. Или что-то."

#     play sound "audio/footsteps_close.ogg"
#     pause(2.0)

#     "Ты закрываешь глаза. Слишком поздно менять что-либо."

#     jump day4_end

# label day4_end:
#     $ time_of_day = "night"

#     scene black
#     with fade
#     stop music fadeout 2.0

#     "..."

#     "Ты не спишь. Сон ушёл. Осталась только фиксация. Ты — наблюдающий и наблюдаемый одновременно."

#     "Тебе хочется записать что-то в блокнот, но он уже заполнен."

#     scene bg_terminal_dark
#     with slow_dissolve

#     "Ты подходишь к терминалу. На экране мигает лог:"

#     show screen system_terminal("""
#     === СИСТЕМА ЯСИМП v4.0 ===
#     Время: неизвестно
#     Память: перегружена
#     Сессия: нестабильна

#     === ЛОГ 4Х ===
#     [!] Обнаружено: ВНЕШНЕЕ СУЩЕСТВОВАНИЕ
#     [@] Идентификатор отсутствует
#     [#] Характеристика: адаптивное. контурное. древнее.
#     [!] Сопровождает субъект 197.001
#     [~] Потенциальное имя: «тень наблюдателя»
#     """)

#     pause(6.0)
#     hide screen system_terminal

#     play sound "audio/system_warning_low.ogg"

#     "Ты не понимаешь, кто или что это. Но ты чувствовал: ты не один."

#     "Что-то следовало за тобой не первый день. Не в виде страха. В виде… алгоритма?"

#     scene bg_notebook_dark
#     with dissolve

#     "На развороте блокнота — символ, который ты не рисовал: перекрещённый глаз, обрамлённый стрелками."

#     $ persistent.notes.append("Лог 4Х: обнаружена сущность без ID, связанная с игроком")
#     $ persistent.inventory.append("Заметка с символом 'перекрещённый глаз'")

#     "Ты трогаешь бумагу — она тёплая. Ни чернил. Ни карандаша. Только тиснение."

#     menu:
#         "Попробовать стереть":
#             "Ты трёшь страницу. Символ исчезает. Но сквозь бумагу проступает новый: «∆197»."
#             $ persistent.notes.append("Попытка стереть знак вызвала новый: ∆197")
#         "Закрыть блокнот":
#             "Ты чувствуешь, что пока не готов знать всё. И всё же уже знаешь больше, чем должен."

#     stop sound

#     scene bg_komnata_otdyha_dark
#     with fade
#     play music "audio/silence_loop.ogg" fadein 3.0

#     "Ты ложишься. Свет не выключается. Диван кажется другим. Мягче. Или это не диван?"

#     "Ты засыпаешь. Или входишь в другой процесс."

#     $ persistent.completed_days.append(4)
#     $ persistent.tasks = []

#     show screen day_summary("День 4 завершён", persistent.notes, persistent.inventory)

#     "Тень наблюдателя приближается. Система не реагирует. Возможно, и ты — её часть."

#     return
