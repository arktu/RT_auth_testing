import time
import pytest
from pages.rt_reg import *
from api_lib import *


# python -m pytest -v tests\test_reg_invalid_confirm_password.py

# Здесь error_expected:
# 1 Длина пароля должна быть не менее 8 символов
# 2 Пароль должен содержать хотя бы одну заглавную букву
# 3 Пароль должен содержать только латинские буквы
# 4 Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру
# 5 Пароль не должен содержать пробелов
# 6 универсальный вариант - ищем только слово "должен" или "должна", т.к. они присутствуют во всех вариантах ошибок
@pytest.mark.parametrize("password, error_expected", [("", 1), ("Пароль78", 3), ("Passwo7", 1), ("password7", 2),
                                                      ("The password8", 5),
                                                      # + деструктивные варианты
                                                      (generate_string(1001, "э"), 6), (chinese_chars(), 6),
                                                      (special_chars(), 6), (sql_injection(), 6)],
                         ids=['empty str', 'rus', '7 chars', 'no caps', 'with space',
                              '', '', '', ''])
def test_reg_invalid_confirm_password(web_browser, password, error_expected):
    """ Тестирование вывода ошибки при вводе некорректного пароля подтверждения """

    print("\n")

    page = RTReg(web_browser)
    page.click_register()

    # проверка, что мы на странице Регистрации
    assert page.first_name_input.find()

    # открываем видимость второго пароля
    eye = page.password_eyes.find()[1]
    eye.click()

    # заполняем корректными данными все поля, кроме пароля
    page.first_name_input.send_keys("Иван")
    page.last_name_input.send_keys("Петров")
    page.phone_email_input.send_keys(EMAIL_TEST)

    page.password_input.send_keys("The-password")
    page.password_confirm_input.send_keys(password)

    page.reg_button.click()  # жмем на кнопку "Зарегистрироваться"

    password_errors = {1: page.password_error1, 2: page.password_error2, 3: page.password_error3,
                       4: page.password_error4, 5: page.password_error5, 6: page.password_error6}

    print("", password_errors[error_expected].get_text())
    assert password_errors[error_expected].find()  # проверка появившегося текста ошибки

    time.sleep(2)
