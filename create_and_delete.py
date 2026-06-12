# Подключаем встроенные модули и библиотеки:
import json
import random
import time

# Нужные функции:
def players() -> list:
    """Создаёт список игроков на основе ввода имён или их количества.

    Returns:
        Возвращает список игроков.
    """
    while True:
        print('\n' * 35)
        raw_input = input('Введите имена разных игроков через пробел или их количество: ').split()
        print('\n' * 35)
        if len(raw_input) == 1 and raw_input[0].isdigit():
            count_players = int(raw_input[0])
            lst_players = []
            for val in range(count_players):
                lst_players.append(f'Игрок {val + 1}')
        else:
            lst_players = raw_input
        print('-' * 100)
        if 3 <= len(set(lst_players)) <= 10:
            print(f"Отлично! Состав ({len(lst_players)} чел.): {', '.join(lst_players)}")
            print('-' * 100)
            time.sleep(3)
            break
        else:
            print(f"Ошибка! Нужно от 3 до 10 уникальных игроков (сейчас: {len(set(lst_players))}).")
        print('-' * 100)
        time.sleep(2)
    return lst_players

def create_theme(themes: dict):
    """Создаёт тему со словами от пользователя.

    Args:
        themes: Словарь тем со словами.
    """
    print('\n' * 35)
    name_themes = input('Введите название темы, которую хотите добавить: ')
    print('-' * 100)
    if name_themes in themes:
        print('Такая тема уже существует!')
        print('-' * 100)
        time.sleep(2)
        return
    print('\n' * 35)
    themes[name_themes] = input('Введите слова в тему через пробел: ').split()
    json_dump(themes)

    print('\n' * 35)
    print('-' * 100)
    print('Тема со словами успешно создана!')
    print('-' * 100)
    time.sleep(2)

def json_dump(themes: dict):
    """Сохраняет обновлённый словарь тем в файл JSON.

    Args:
        themes: Словарь тем со словами.
    """
    with open('storage.json', 'w', encoding='utf-8') as file:
        json.dump(themes, file, indent=4, ensure_ascii=False)

def delete_theme(themes: dict):
    """Удаляет тему, выбранную пользователем, кроме 4 основных тем.

    Args:
        themes: Словарь тем со словами.
    """
    print('\n' * 35)
    name_themes = input('Введите название темы, которую хотите удалить: ')
    print('\n' * 35)
    print('-' * 100)
    if name_themes not in themes:
        print('Такой темы не существует!')
        print('-' * 100)
        time.sleep(2)
        return
    if name_themes in ["Локации", "Clash Royale", "Видеоигры", "Minecraft"]:
        print('Тема является основной, её удалять нельзя!')
        print('-' * 100)
        time.sleep(2)
        return
    themes.pop(name_themes)
    json_dump(themes)
    print('Тема со словами удалена успешно!')
    print('-' * 100)
    time.sleep(2)

def sec_word(user_theme:str, themes: dict) -> str:
    """Выбирает случайное секретное слово, которое должны угадать Шпионы.

    Args:
        user_theme: Тема, которая выбрана пользователем в начале игры.
        themes: Словарь тем со словами.

    Returns:
          Возвращает секретное слово.
    """
    lst_words = themes[user_theme]
    choice_word = random.choice(lst_words)
    return choice_word

def shpion(num_shpions: int, lst_players: list) -> list:
    """Создаёт список шпионов для игры.

    Args:
        num_shpions: Кол-во Шпионов.
        lst_players: Список игроков.

    Returns:
        Возвращает список Шпионов.
    """
    shpion1 = random.choice(lst_players)
    shpions = [shpion1]
    if num_shpions == 2:
        lst_without_shpion1 = [i for i in lst_players if i != shpion1]
        shpion2 = random.choice(lst_without_shpion1)
        shpions.append(shpion2)
    return shpions

