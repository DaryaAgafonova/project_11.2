def string_in_capital_letters(string):

    """ Функция, которая принимает на вход строку
        и возвращает ее со всеми заглавными буквами."""

    return string.upper()

string = input()
print(string_in_capital_letters(string))


def capital_letters(string):

    """ Функция, которая делает заглавными первые буквы каждого слова в строке,
    поступившей на вход функции"""

    return string.title()

string_title = input()
print(capital_letters(string_title))