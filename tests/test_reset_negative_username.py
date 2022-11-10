# import time
import pytest
from pages.rt_reset import *
from api_lib import *


@pytest.mark.parametrize("username_test", ["unexist_test_user", generate_string(1001), russian_chars(), russian_chars().upper(),
                                           chinese_chars(), special_chars(), sql_injection()],
                         ids=['unexist user', '1001 chars', 'russian', 'russian uppercase', 'chinese', 'special chars',
                              'sql injection 1'])
def test_reset_negative_username(web_browser, username_test):
    """ Восстановление пароля - негативные и деструктивные тесты на выдачу ошибки при невалидном логине """

    print("\n")

    page = RTReset(web_browser)
    # проверка, что мы на странице восстановления пароля
    assert page.reset_title.get_text() == "Восстановление пароля"
    assert page.username_input.find()

    # print("username =", username_test)

    page.tab_phone.click()
    page.username_input.send_keys(username_test)

    # на случай, если есть капча
    page.wait_for_captcha()

    page.login_button.click()

    time.sleep(3)  # задержка для смены страницы после аутентификации

    assert page.incorrect_user_error.find()  # проверка наличия сообщения об ошибке авторизации

    time.sleep(2)

