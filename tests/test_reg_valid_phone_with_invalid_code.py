# import time
# import pytest
from pages.rt_reg import *
from api_lib import *


def test_reg_valid_phone_with_invalid_code(web_browser):
    """ Проверка выдачи ошибки при вводе некорректного кода подтверждения номера телефона при регистрации
    по телефону в ЛК Ростелеком ID """

    print("\n")

    page = RTReg(web_browser)
    page.click_register()

    # проверка, что мы на странице Регистрации
    assert page.first_name_input.find()

    # заполняем корректными данными все поля, кроме имени
    page.first_name_input.send_keys("Иван")
    page.last_name_input.send_keys("Петров")
    page.phone_email_input.send_keys("+79059928947")
    page.password_input.send_keys("The_password")
    page.password_confirm_input.send_keys("The_password")

    page.reg_button.click()  # жмем на кнопку "Зарегистрироваться"

    time.sleep(2)

    assert page.title_confirm_phone.find()  # проверка наличия заголовка "Подтверждение телефона"
    rt_codes = {0: page.rt_code0, 1: page.rt_code1, 2: page.rt_code2, 3: page.rt_code3,
                4: page.rt_code4, 5: page.rt_code5}

    # ввод некорректного кода
    for i in rt_codes.keys():
        rt_codes[i].send_keys("1")

    time.sleep(2)

    assert page.code_error.find()  # проверка наличия строки с ошибкой "Неверный код"

    time.sleep(2)
