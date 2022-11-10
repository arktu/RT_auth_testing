import time
import pytest
from pages.rt_reg import *
from api_lib import *


# from pages.elements import WebElement
# from selenium.webdriver.common.keys import Keys


# негативные варианты тестов с некорректным именем при регистрации
@pytest.mark.parametrize("first_name", ["", "я", "My-Name", "Это_Имя", generate_string(31, "ю"),
                                        # + деструктивные варианты
                                        generate_string(1001, "ю"), chinese_chars(), special_chars(), sql_injection()],
                         ids=['', '1 char', '', '', '31 chars',
                              '', '', '', ''])
def test_reg_invalid_first_name(web_browser, first_name):
    """ Тестирование вывода ошибки при вводе некорректного имени """

    print("\n")

    page = RTReg(web_browser)
    page.click_register()

    # проверка, что мы на странице Регистрации
    assert page.first_name_input.find()

    page.first_name_input.send_keys(first_name)

    # заполняем корректными данными все поля, кроме имени
    page.last_name_input.send_keys("Фамилия")
    page.phone_email_input.send_keys("sfsf-test@test.ru")
    page.password_input.send_keys("The_password")
    page.password_confirm_input.send_keys("The_password")

    page.reg_button.click()  # жмем на кнопку "Зарегистрироваться"

    # assert page.first_name_input.find()  # проверка, что мы остались на прежней странице
    assert page.name_error.find()  # проверка появившегося текста ошибки

    time.sleep(1)
