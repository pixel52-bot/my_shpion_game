# Подключаем встроенные модули и библиотеки:
import random
import time

# Подключаем свои модули:
import printer
import create_and_delete as cr_del
import exam

# Нужные функции:
def distribution_menu(user_choice: int, themes: dict) -> bool:
    """Распределяет выбор пользователя в главном меню и вызывает соответствующую функцию.

    Args:
        user_choice: Выбор действия от пользователя.
        themes: Словарь с темами и словами.

    Returns:
        Возвращает False, если пользователь выбрал `Выйти из игры`, True иначе.
    """
    if user_choice == 1:
        printer.rules()
    elif user_choice == 2:
        game_dist(themes)
    elif user_choice == 3:
        delete_create_theme(themes)
    elif user_choice == 4:
        printer.see_themes(themes)
    elif user_choice == 5:
        print('-' * 100)
        return False
    return True

def game_dist(themes: dict):
    """Отвечает за основную игру и распределяет информацию по другим функциям.

    Args:
        themes: Cловарь с темами и словами.
    """
    if exam.search_themes(themes):
        lst_players = cr_del.players()
        user_theme = printer.choice_theme(themes)
        choice_user = printer.game_mode()
        chaos_or_classic(choice_user, user_theme, lst_players, themes)

def dist_role_clas(lst_players: list, need_theme: str, location: str ,  shpions: list):
    """Определяет роль (Шпион или Мирный) для каждого игрока.

    Args:
        lst_players: Список игроков.
        need_theme: Тема, которая выбрана пользователем в начале игры.
        location: Рандомная локация из определенной темы.
        shpions: Шпион(-ы) в игре.
    """
    for index, name in enumerate(lst_players):
        printer.see_role(lst_players, index)
        if name in shpions:
            printer.printer_shpion(need_theme)
        else:
            printer.printer_live(location, need_theme)

def chaos(lst_players: list, user_theme: str, themes: dict):
    """Случайно выбирает и запускает 1 из 4 режимов Хаоса с шансом 25%.

    Args:
        lst_players: Список игроков.
        user_theme: Тема, которая выбрана пользователем в начале игры.
        themes: Словарь тем со словами.
    """
    mode_chaos = random.randint(1, 100)
    if mode_chaos <= 25:
        all_shpion(lst_players, user_theme)
    elif mode_chaos <= 50:
        all_life(lst_players, user_theme, themes)
    elif mode_chaos <= 75:
        random_secret_word(lst_players, user_theme, themes)
    else:
        classic(lst_players, user_theme, themes, max_shpions=1)

def classic(lst_players: list, user_theme: str, themes: dict, max_shpions: int=2):
    """Создает классическую игру и распределяет данные по другим функциям.

     Args:
         lst_players: Список игроков.
         user_theme: Тема, которая выбрана пользователем в начале игры.
         themes: Словарь тем со словами.
         max_shpions: Максимальное кол-во Шпионов.
     """
    num_shpions = exam.num_shpions(lst_players, max_shpions)
    shpions = cr_del.shpion(num_shpions, lst_players)
    secret_word = cr_del.sec_word(user_theme, themes)
    dist_role_clas(lst_players, user_theme, secret_word, shpions)

def chaos_or_classic(choice_user: int, user_theme: str, lst_players: list, themes: dict):
    """Проверяет выбор пользователя и распределяет в выбранный режим.

    Args:
        choice_user: Выбор режима пользователем.
        user_theme: Тема, которая выбрана пользователем в начале игры.
        lst_players: Список игроков.
        themes: Словарь тем со словами.
    """
    if choice_user == 1:
        chaos(lst_players, user_theme, themes)
    else:
        classic(lst_players, user_theme, themes)
    exam.questions(user_theme)

def result_input(ran: int) -> int:
    """Проверяет ввод от пользователя и распределяет информацию по другим функция.

    Args:
        ran: Максимальный диапазон чисел для корректного ввода пользователя.

    Returns:
        Возвращает корректно введённое число от пользователя.
    """
    while True:
        mes_user = input('Выберите номер нужного действия: ')
        if exam.ex_isdigit(mes_user):
            mes_user = int(mes_user)
            if exam.range_digits(mes_user, ran):
                return int(mes_user)
            else:
                print('-' * 100)
                print('Выберите число из диапазона!')
                print('-' * 100)
        else:
            print('-' * 100)
            print('Неправильный ввод, Введите только ЦИФРУ!')
            print('-' * 100)

def delete_create_theme(themes: dict):
    """Выводит меню создания и удаления тем и распределяет выбор пользователя.

     Args:
         themes: Словарь тем со словами.
    """
    print('\n' * 35)
    print('-' * 100)
    print('1. Добавить тему со словами')
    print('2. Удалить тему со словами')
    print('3. Выход в меню')
    print('-' * 100)
    choice_user = result_input(3)
    if choice_user == 1:
        cr_del.create_theme(themes)
    elif choice_user == 2:
        cr_del.delete_theme(themes)
    else:
        print('-' * 100)

def all_shpion(lst_players: list, user_theme: str):
    """Раздаёт роль Шпиона абсолютно всем игрокам в режиме Хаоса.

    Args:
        lst_players: Список игроков.
        user_theme: Тема, которая выбрана пользователем в начале игры.
    """
    for num, name in enumerate(lst_players):
        printer.see_role(lst_players, num)
        printer.printer_shpion(user_theme)

def all_life(lst_players: list, user_theme: str, themes: dict):
    """Раздаёт роль Мирного абсолютно всем игрокам в режиме Хаоса.

    Args:
        lst_players: Список игроков.
        user_theme: Тема, которая выбрана пользователем в начале игры.
        themes: Словарь тем со словами.
    """
    secret_word = cr_del.sec_word(user_theme, themes)
    for num, name in enumerate(lst_players):
        printer.see_role(lst_players, num)
        printer.printer_live(secret_word, user_theme)

def random_secret_word(lst_players: list, user_theme: str, themes: dict):
    """Раздаёт каждому игроку индивидуальное случайное слово из выбранной темы.

    Args:
        lst_players: Список игроков.
        user_theme: Тема, которая выбрана пользователем в начале игры.
        themes: Словарь тем со словами.
    """
    lst_words = themes[user_theme]
    for num, name in enumerate(lst_players):
        choice_word = random.choice(lst_words)
        printer.see_role(lst_players, num)
        printer.printer_live(choice_word, user_theme)
