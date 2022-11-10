
def generate_string(n, str_rep="x"):
    return str_rep * n


def russian_chars():
    return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


# 20 популярных китайских иероглифов
def chinese_chars():
    return '的一是不了人我在有他这为之大来以个中上们'


def special_chars():
    return '<>\'|\\/!@#$%^&*()-_=+`~?"№;:[]{}'


def sql_injection(inj_type=1):
    if inj_type == 1:
        return '\' or 1=1--'

    return 'SELECT *'
