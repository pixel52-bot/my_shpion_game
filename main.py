# Подключаем нужные модули и библиотеки:
import time
import random
import json

#Подключение своих модулей:
import themes

# Нужные переменные для игры:
is_game = True  # Игра запущена
themes = themes.json_load() # Словарь тем со словами

# Нужные функции:

def welcome():
    """
    Встреча и представления программы пользователю при запуске.
    """
    print('-' * 100)
    print('\n' * 50)
    print('-' * 100)
    print('Вас встречает игра "Шпион"')
    print('Перед началом игры, прошу ознакомиться с правилами! Заранее благодарю за внимане!')
    print('-' * 100)

def main_menu():
    """
    Главное меню программы, которое возвращаеться после каждого действия.
    """
    print('\n' * 50)
    print('-' * 100)
    print('Главное меню:')
    print('1. Правила игры')
    print('2. Создать новую игру')
    print('3. Добавить или удалить тему со словами')
    print('4. Просмотр тем со словами')
    print('5. Выйти из игры')
    print('-' * 100)

def distribution_menu(x: int, themes: dict):
    """
    Распределяющее меню, которое появляеться после выбранного действия пользователем и отправляет его в опрделённую функцию
    :args:
    1. Выбор действия от пользователя.
    2. Словарь с темами и словами.
    :retun: Возвращает True или False для дальнейшей проверки в основном цикле.
    """
    if x == 1:
        rules()
    elif x == 2:
        game(themes)
    elif x == 3:
        general_delete_create_theme(themes)
    elif x == 4:
        see_themes(themes)
    else:
        return False
    return True

def rules():
    """
    Функция идущая после распределяющего меню (distribution_menu), которая предоставляет осноные правила игры.
    """
    print('-' * 150)
    print('-------------Основные Правила игры--------------')
    print('0. Вы указываете кол-во игроков, которые примут участие в игре (минимум 3, максимум 10)')
    print('1. Вы выбераете тему со словами (есть встроены и вы можете добывить свою)')
    print('2. Выбор режима Классика или Хаос')
    print('3. Каждому игроку будет дана роль: Шпион или Мирный')
    print('4. Все Мирные игрок получают 1 слово, про которое Шпион(-ы) не знают')
    print('5. Главная задача Мирных вычеслить Шпиона(-ов), а Шпиону(-ам) угадать слово')
    print('6. Любой игрок может начать голосование, если его поддержат другие игроки')
    print('7. По концу голосования вы должны определить кто Шпион, и проголосовать за него')
    print('8. Если вы не уверены, то можете не голосовать (пропустить ход)')
    print('9. Если игрок за которого проголосовало большенство не Шпион, то Шпион(-ы) победили')
    print('10. Если игроки выгнали Шпиона, и Шпионов не осталось, то Мирные победили')
    print(
        '11. Чтобы Мирные могли понять кто Шпион, игроки друг другу должны задавать вопросы или говорить факты, связанные со словом')
    print('12. Далее будет настройка игры под ваш вкус')
    print('13. Если вы играли по другим правилам то можете оставить их!')
    print('14. НЕ СТОИТ удалять 4 основные темы, которые добавлены без вашего участия!')
    print('Хаос - режим, в котором могут быть разные усложнения:')
    print('1. Все игроки являются Шпионами')
    print('2. Все игроки Мирные')
    print('3. У всех игроков разные слова')
    print('4. Обычная классическая игра')
    print('Классика - режим, в котором првила обычные, есть от 1 до 2 Шпионов и у всех Мирных 1 слово')
    print('-------СПАСИБО ЗА ВНИМАНИЕ И ХОРОШЕЙ ИГРЫ!--------')
    print('-' * 150)

def game(themes: dict):
    """
    Функция идущая после распределяющего меню (distribution_menu), которая отвечает за игру и распределяет информацию по другим функциям.
    arg: Принимает словарь с темами и словами.
    """
    if search_themes(themes):
        lst_players = players()
        user_theme = choice_theme(themes)
        choice_user = game_mode()
        chaos_or_classic(choice_user, user_theme, lst_players, themes)

def chaos_or_classic(choice_user: int, user_theme: int, lst_players: list, themes: dict):
    if choice_user == 1:
        chaos(lst_players, user_theme, themes)
    else:
        classic(lst_players, user_theme, themes)
    questions(user_theme, themes)

def search_themes(themes: dict):
    """
    Одна из вспомогательных функций основной функции game. Она проверяет если есть доступные темы для игры.
    :arg: Принимает словарь с темами и словами.
    :return: Возвращает True или False для дальнейшей проверки в функции game.
    """
    if themes == {}:
        print('-' * 100)
        print('У вас нет доступных тем, создайте хотя бы 1 тему со словами!')
        print('-' * 100)
        time.sleep(5)
        return False
    else:
        return True

def players():
    """
    Одна из вспомогательных функций основной функции game. Она создает список игроков.
    :return: Возвращает список игроков в функцию game.
    """
    while True:
        raw_input = input('Введите имена разных игроков через пробел или их количество: ').split()
        if len(raw_input) == 1 and raw_input[0].isdigit():
            count_players = int(raw_input[0])
            lst_players = []
            for val in range(count_players):
                lst_players.append(f'Игрок {val + 1}')
        else:
            lst_players = raw_input
        if 3 <= len(set(lst_players)) <= 10:
            print(f"Отлично! Состав ({len(lst_players)} чел.): {', '.join(lst_players)}")
            print('-' * 100)
            break
        else:
            print(f"Ошибка! Нужно от 3 до 10 игроков (сейчас: {len(lst_players)}).")
    return lst_players

def num_shpion(lst_players: list):
    """

    """
    if len(lst_players) >= 5:
        print('Нажмите "1" если хотите оставить 1 Шпиона и "2" если поставить 2 Шпиона')
        return result_input(2)
    else:
        return 1

def choice_theme(themes: dict):
    """
    Одна из вспомогательных функций основной функции game. Она предоставляет все темы, котрые есть в словаре themes и из которых пользователь должен выбрать одну.
    :arg: Принимает словарь с темами (themes)
    :return: Направляет во вспомогательную функцию (result_input), в которой проверяеться ввод пользователя.
    """
    print('-' * 50)
    print('Выбор темы:')
    lst_themes = list(themes)
    for index, theme in enumerate(lst_themes, start=1):
        print(f'{index}. {theme}')
    print('-' * 50)
    return result_input(len(themes))

def game_mode():
    """
    Одна из вспомогательных функций основной функции game. Она предоставляет 2 режима игры, которые должен выбрать пользователь.
    :return: Направляет во вспомогательную функцию (result_input), в которой проверяеться ввод пользователя.
    """
    print('-' * 50)
    print('Выбирите режим:')
    print('1. Хаос')
    print('2. Классика')
    print('-' * 50)
    return result_input(2)

def questions(user_theme: str, themes:dict):
    """
    Одна из вспомогательных функций основной функции game. Она предоставляет список вопросов, которые пользователи могут задавать друг другу.
    """
    print('Нажмите 1, если хотите посмотреть вспомогательные вопросы, и 2, если хотите продолжить')
    mes_user = result_input(len(themes))
    if mes_user == 1:
        if len(themes) > 4:
            if user_theme == 1:
                locations()
            elif user_theme == 2:
                clash_royale()
            elif user_theme == 3:
                games()
            elif user_theme == 4:
                minecraft()
        else:
            other()

def locations():
    """
    Одна из вспомогательных функций основной функции questions. Она выдает список вопросов по теме Локации.
    """
    print('1. Часто ли здесь можно встретить детей?')
    print('2. Здесь обычно шумно или соблюдают тишину?')
    print('3. Нужно ли платить за вход в это место?')
    print('4. Используешь ли ты здесь какие-то специальные инструменты или предметы?')
    print('5. Это место находится под открытым небом или в помещении?')
    print('6. Есть ли здесь какие-то правила безопасности, которые нельзя нарушать?')
    print('7. Много ли здесь электрических приборов?')
    print('8. Бывает ли это место закрыто на перерыв или выходные?')
    print('9. Встречаются ли здесь очереди?')
    print('10. Какая здесь преобладающая цветовая гамма (однотонная или цветная)?')

def clash_royale():
    """
    Одна из вспомогательных функций основной функции questions. Она выдает список вопросов по теме Clash Royal.
    """
    print('1. Эта карта умеет летать?')
    print('2. Сколько эликсира стоит карта')
    print('3. Эта карта атакует только здания или всех подряд?')
    print('4. Эта карта появляется на арене одна или с друзьями?')
    print('5. Твоя карта бьет по области (сплеш) или в одну цель?')
    print('6. Эта карта редкости - ...')
    print('7. Можно ли карту встретить на самых первых аренах?')
    print('8. Карта передвигается по арене или быстро или не спеша?')
    print('9. У карты много здоровья или ее можно убить «Стрелами»?')
    print('10. Карта наносит урон мгновенно или постепенно?')

def games():
    """
    Одна из вспомогательных функций основной функции questions. Она выдает список вопросов по теме Видеоигры.
    """
    print('1. Можно ли в этой игре умереть от падения с высоты (с полный запасом здоровья)?')
    print('2. Эта одиночная игра или здесь важна командная работа?')
    print('3. Нужно ли здесь собирать ресурсы (фармить), чтобы стать сильнее?')
    print('4. Есть ли в игре инвентарь, в котором ты носишь кучу вещей?')
    print('5. Виден ли твой персонаж со стороны или ты смотришь его глазами(Вид от 1-го или 3-го лица)?.')
    print('6. Можно ли здесь управлять каким-то транспортом?')
    print('7. Есть ли в игре открытый мир, по которому можно просто гулять?')
    print('8. Есть ли в этой игре магия или сверхспособности?')
    print('9. Твоему персонажу нужно есть, пить или спать, чтобы выжить?')
    print('10. Есть ли в игре какой-то главный злодей (финальный босс)?')

def minecraft():
    """
    Одна из вспомогательных функций основной функции questions. Она выдает список вопросов по теме Minecraft.
    """
    print('1. Этот предмет/блок можно найти в обычном мире или нужно идти в другой портал?')
    print('2. Нужен ли специальный инструмент, чтобы это добыть, или можно справиться рукой?')
    print('3. Можно ли этот предмет скрафтить на верстаке?')
    print('4. Связано ли это с «эффектами» (зельеварением или наложением чар)?')
    print('5. Это можно встретить в деревне жителей?')
    print('6. Используется ли этот блок в механизмах редстоуна?')
    print('7. Является ли этот блок «полным» (занимает ли он весь куб)?')
    print('8. Стакается ли этот предмет до 64 или он занимает целый слот?')
    print('9. Нужен ли этот предмет, чтобы создать другой, более сложный?')
    print('10. Является ли этот предмет редким (можно ли его найти только в сундуках данжей)? ')

def other():
    """
    Одна из вспомогательных функций основной функции questions. Она выдает список вопросов по темам добавленным пользователем.
    """
    print('1. Как долго ты в этом разбирался, прежде чем начать?')
    print('2. Это занятие требует быстрой реакции или можно долго думать?')
    print('3. Часто ли здесь случаются конфликты или споры?')
    print('4. Тут преобладают яркие цвета или всё довольно мрачное?')
    print('5. Это скорее что-то современное или из прошлого?')
    print('6. Нужно ли здесь постоянно что-то копить или собирать? (Золото в играх, опыт, вещи)?')
    print('7. Есть ли здесь какой-то финал или это бесконечный процесс?')
    print('8. Тебе это быстро надоедает или можешь сидеть часами?')
    print('9. Много ли времени это отнимает в обычной жизни?')
    print('10. Это популярно сейчас или пик славы уже прошел?')
    print('11. Насколько сильно здесь всё зависит от удачи, а не от твоих навыков?')
    print('12. Это больше про творчество или про сухую логику и расчет?')
    print('13. Здесь важна физическая сила или только работа головой?')
    print('14. Лучше заниматься этим утром или ночью?')
    print('15. Много ли в этой теме непонятных слов и терминов для обычного человека?')

def result_input(ran):
    while True:
        mes_user = input('Выберите номер нужного действия: ')
        need_val = ex_isdigit(mes_user)
        if range_digits(need_val, ran):
            return int(need_val)
        else:
            print('Выберите число из диапозона!')

def range_digits(need_val, rang):
    need_val = int(need_val)
    while not (0 < need_val <= rang):
        return False
    return True

def ex_isdigit(st):
    while not (st.isdigit()):
        print('Неправильный ввод, Введите только ЦИФРУ!')
        st = input('Выберите номер нужного действия: ')
    return st

def val_shpions(lst_players,shpions):
    if shpions == 0:
        val_shpion = num_shpion(lst_players)
    else:
        val_shpion = 1
    return val_shpion

def classic(lst_players, user_theme, themes, shpions=0 ):
    val_shpion = val_shpions(lst_players,shpions)
    shpion1, shpion2 = shpion(val_shpion, lst_players)
    location, need_theme = locate(user_theme, themes)
    dist_role_clas(lst_players, need_theme, location, shpion1, shpion2)

def dist_role_clas(lst_players, need_theme, location ,  shpion1, shpion2):
    for index, name in enumerate(lst_players):
        see_role(lst_players, index)
        if shpion1 == name or shpion2 == name:
            dist_shpion(need_theme)
        else:
            dist_live(location, need_theme)

def dist_shpion(need_theme):
        print(f"ТЫ ШПИОН! Тема: {need_theme}")
        print("-" * 100)
        time.sleep(5)
        print("\n" * 50)

def dist_live(location, need_theme):
    print(f"ТЫ МИРНЫЙ. Слово: {location} из Темы: {need_theme}")
    print("-" * 100)
    time.sleep(5)
    print("\n" * 50)

def chaos(lst_players, user_theme, themes):
    mode_chaos = random.randint(1, 100)
    if mode_chaos <= 25:
        all_shpion(lst_players, user_theme)
    elif mode_chaos <= 50:
        all_life(lst_players, user_theme, themes)
    elif mode_chaos <= 75:
        random_locate(lst_players, user_theme, themes)
    else:
        classic(lst_players, user_theme, themes, 1)

def locate(user_theme, themes):
    lst_themes = list(themes)
    need_theme = lst_themes[user_theme - 1]
    lst_words = themes[need_theme]
    choice_word = random.choice(lst_words)
    return choice_word, need_theme

def shpion(shpion_num, lst_players):
    shpion1 = random.choice(lst_players)
    if shpion_num > 1:
        lst_without_shpion1 = [i for i in lst_players if i != shpion1]
        shpion2 = random.choice(lst_without_shpion1)
    else:
        shpion2 = None
    return shpion1, shpion2

def see_role(lst_players, i):
    input(f"Игрок {lst_players[i]}, нажми Enter, чтобы увидеть роль...")
    print("\n" * 50)
    print("-" * 100)

def all_shpion(lst_players, need_theme):
    for i in enumerate(lst_players):
        see_role(lst_players, i)
        dist_shpion(need_theme)

def all_life(lst_players, need_theme, themes):
    for i in enumerate(lst_players):
        location = locate(need_theme, themes)
        see_role(lst_players, i)
        dist_live(location, need_theme)

def random_locate(lst_players, need_theme, themes):
    for i in enumerate(lst_players):
        choice_word = random.choice(need_theme)
        see_role(lst_players, i)
        dist_live(choice_word, need_theme)

def general_delete_create_theme(themes):
    print('1. Добавить тему со словами')
    print('2. Удалить тему со словами')
    print('3. Выход в меню')
    choice_user = result_input(3)
    if choice_user == 1:
        create_theme(themes)
    elif choice_user == 2:
        delete_theme(themes)

def create_theme(themes):
    name_themes = input('Введите название темы: ')
    themes[name_themes] = input('Введите слова в тему через пробел: ').split()
    json_dump(themes)
    print('Тема со словами успешна создана!')

def json_dump(themes):
    with open('storage.json', 'w', encoding='utf-8') as file:
        json.dump(themes, file, indent=4, ensure_ascii=False)

def delete_theme(themes):
    name_themes = input('Введите название темы, которую хотите удалить: ')
    while name_themes not in themes:
        print('Такой темы не существует, повторите попытку!')
        name_themes = input('Введите название темы, которую хотите удалить: ')
    themes.pop(name_themes)
    json_dump(themes)
    print('Тема со словами удалена успешно!')

def see_themes(themes):
    print('Просмотр тем:')
    lst_themes = list(themes)
    for val, name in enumerate(themes, start=1):
        print(f'{val}. {name}')
    theme = result_input(len(themes))
    need_theme = lst_themes[theme - 1]
    lst_words = themes[need_theme]
    print('\n'.join(lst_words))
    print('-' * 100)


welcome()
while is_game:
    for val in range(0, 101):
        print(f'Загрузка тем со словами: {val}%', end='\r')
        time.sleep(0.05)
    main_menu()
    choice = result_input(5)
    is_game = distribution_menu(choice, themes)
    pause = input('Нажмите Enter, чтобы продолжить...')
