# import time
# import pytest
from pages.rt_reg import *
from api_lib import *


def test_reg_passwords_differ(web_browser):
    """ Проверка вывода ошибки на странице регистрации при вводе не совпадающих паролей """

    print("\n")

    page = RTReg(web_browser)
    page.click_register()

    # проверка, что мы на странице Регистрации
    assert page.first_name_input.find()

    # заполняем корректными данными все поля, кроме имени
    page.first_name_input.send_keys("Иван")
    page.last_name_input.send_keys("Петров")
    page.phone_email_input.send_keys("sfsf-test@test.ru")

    page.password_input.send_keys("The_password")
    page.password_confirm_input.send_keys("_Thepassword8")

    page.reg_button.click()  # жмем на кнопку "Зарегистрироваться"

    assert page.passwords_differ_error.find()  # проверка появившегося текста ошибки "Пароли не совпадают"

    time.sleep(2)
