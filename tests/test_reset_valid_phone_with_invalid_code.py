# import time
# import pytest
from pages.rt_reset import *


def test_reset_valid_phone_with_invalid_code(web_browser):
    """ Тестирование выдачи ошибки при вводе некорректного кода подтверждения номера телефона, при восстановлении
    пароля по зарегистрированному телефону  """

    print("\n")

    page = RTReset(web_browser)
    # проверка, что мы на странице восстановления пароля
    # assert page.reset_title.get_text() == "Восстановление пароля"
    assert page.username_input.find()

    page.tab_phone.click()
    page.username_input.send_keys(PHONE_VALID)

    # на случай, если есть капча
    page.wait_for_captcha()

    assert page.back_button.find()  # проверка наличия кнопки "Вернуться назад"

    page.reset_button.click()

    time.sleep(2)  # задержка для смены страницы

    assert page.radio_phone.find()
    assert page.cancel_button.find()  # проверка наличия кнопки "Вернуться назад"

    page.radio_phone.click()
    page.submit_button.click()

    time.sleep(2)  # задержка для смены страницы

    # проверка, что мы оказались на странице ввода кода, высланного на е-мэйл
    assert page.page_code_enter_phone.find()

    # проверка на совпадение 4х последних цифр телефона сообщении
    last_digits = f"{PHONE_VALID[-4:-2]}-{PHONE_VALID[-2:]}"
    assert last_digits in page.page_code_enter_phone.get_text()

    assert page.cancel_button.find()  # проверка наличия кнопки "Вернуться назад"

    rt_codes = {0: page.rt_code0, 1: page.rt_code1, 2: page.rt_code2, 3: page.rt_code3,
                4: page.rt_code4, 5: page.rt_code5}

    # ввод некорректного кода
    for i in rt_codes.keys():
        rt_codes[i].send_keys("1")

    time.sleep(2)

    assert page.code_error.find()  # проверка наличия строки с ошибкой

    time.sleep(2)

