import time
import pytest
from pages.rt_reg import *
from api_lib import *


@pytest.mark.parametrize("last_name", ["я", "My-Name", "Это_Имя", generate_string(31, "ю"),
                                       # + деструктивные варианты
                                       generate_string(1001, "э"), chinese_chars(), special_chars(), sql_injection()],
                         ids=['1 char', '', '', '31 chars',
                              '', '', '', ''])
def test_reg_invalid_last_name(web_browser, last_name):
    """ Тестирование вывода ошибки при вводе некорректной фамилии """

    print("\n")

    page = RTReg(web_browser)
    page.click_register()

    # проверка, что мы на странице Регистрации
    assert page.first_name_input.find()

    page.last_name_input.send_keys(last_name)

    # заполняем корректными данными все поля, кроме имени
    page.first_name_input.send_keys("Иван")
    page.phone_email_input.send_keys("sfsf-test@test.ru")
    page.password_input.send_keys("The_password")
    page.password_confirm_input.send_keys("The_password")

    page.reg_button.click()  # жмем на кнопку "Зарегистрироваться"

    # assert page.first_name_input.find()  # проверка, что мы остались на прежней странице
    assert page.name_error.find()  # проверка появившегося текста ошибки

    time.sleep(1)
