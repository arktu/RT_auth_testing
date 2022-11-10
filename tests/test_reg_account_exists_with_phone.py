import time
import pytest
from pages.rt_reg import *
from api_lib import *


def test_reg_account_exists_with_email(web_browser):
    """ Проверка невозможности регистрации с телефоном уже зарегистрированного пользователя """

    print("\n")

    page = RTReg(web_browser)
    page.click_register()

    # проверка, что мы на странице Регистрации
    assert page.first_name_input.find()

    # заполняем корректными данными все поля, кроме имени
    page.first_name_input.send_keys("Иван")
    page.last_name_input.send_keys("Петров")
    page.phone_email_input.send_keys(PHONE_VALID)
    page.password_input.send_keys("The_password")
    page.password_confirm_input.send_keys("The_password")

    page.reg_button.click()  # жмем на кнопку "Зарегистрироваться"

    assert page.account_exists_text.find()  # проверка появившегося окна с текстом "учетная запись уже существует"

    time.sleep(2)
