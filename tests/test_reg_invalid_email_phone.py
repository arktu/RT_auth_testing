import time
import pytest
from pages.rt_reg import *
from api_lib import *


@pytest.mark.parametrize("email_phone", ["", "105999001",
                                         # + деструктивные варианты
                                         generate_string(1001, "x"), chinese_chars(), special_chars(), sql_injection()],
                         ids=['', '', '', '', '', ''])
def test_reg_invalid_email_phone(web_browser, email_phone):
    """ Тестирование вывода ошибки при вводе некорректных e-mail/телефон """

    print("\n")

    page = RTReg(web_browser)
    page.click_register()

    # проверка, что мы на странице Регистрации
    assert page.first_name_input.find()

    # заполняем корректными данными все поля, кроме телефона/почты
    page.first_name_input.send_keys("Иван")
    page.last_name_input.send_keys("Петров")

    page.phone_email_input.send_keys(email_phone)

    page.password_input.send_keys("The_password")
    page.password_confirm_input.send_keys("The_password")

    page.reg_button.click()  # жмем на кнопку "Зарегистрироваться"

    # assert page.first_name_input.find()  # проверка, что мы остались на прежней странице
    assert page.email_phone_error.find()  # проверка появившегося текста ошибки

    time.sleep(1)
