# Подключаем встроенные модули и библиотеки:
import time

# Подключаем свои модули:
import printer
import distribution as dist

# Нужные функции:
def range_digits(need_val: int, ran: int) -> bool:
    """Проверяет, входит ли введенное число в диапазон.

    Args:
        need_val: Введенное число от пользователя.
        ran: Максимальный диапазон чисел, для коректного ввода пользователя.

    Returns:
        Возвращает True, если число входит в диапозон, False иначе.
    """
    if not (0 < need_val <= ran):
        return False
    return True

def ex_isdigit(mes_user: str) -> bool:
    """Проверяет, что введенная строка является числом.

    Args:
        mes_user: Введенная строка от пользователя.

    Returns:
        Возвращает True, если строка является числом, False иначе.
    """
    if not (mes_user.isdigit()):
        return False
    return True

def questions(user_theme: str):
    """Предоставляет список вопросов, которые пользователь может задавать друг другу.

    Args:
       user_theme: Тема, которая выбрана пользователем в начале игры.
    """
    print('\n' * 35)
    print('-' * 100)
    print('Нажмите 1, если хотите посмотреть вспомогательные вопросы, и 2, если хотите продолжить.')
    print('-' * 100)

    mes_user = dist.result_input(2)
    if mes_user == 1:
        questions_list = printer.all_questions[user_theme]
        print('\n' * 35)
        print('-' * 100)
        print(questions_list)
        print('-' * 100)
    else:
        print('-' * 100)

def num_shpions(lst_players: list, num_shps: int) -> int:
    """Определяет количество шпионов в игре.

    Args:
        lst_players: Список текущих игроков.
        num_shps: Максимальное кол-во Шпионов.

    Returns:
        Выбранное или автоматически назначенное количество шпионов.
    """
    if num_shps == 2:
        if len(lst_players) >= 5:
            print('\n' * 35)
            print('-' * 100)
            print('Нажмите "1", если хотите оставить 1 Шпиона, и "2", если поставить 2 Шпионов')
            print('-' * 100)
            return dist.result_input(2)

    return 1

def search_themes(themes: dict) -> bool:
    """Проверяет, есть ли доступные темы.

    Args:
       themes: Словарь тем со словами.

    Returns:
         True, если есть доступные темы, иначе False.
    """
    if themes == {}:
        print('\n' * 35)
        print('-' * 100)
        print('У вас нет доступных тем, создайте хотя бы 1 тему со словами!')
        print('-' * 100)
        time.sleep(2)
        return False
    else:
        return True