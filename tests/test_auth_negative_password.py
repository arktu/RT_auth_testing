import time
import pytest
from pages.rt_auth import *
from api_lib import *
# from pages.elements import WebElement


@pytest.mark.parametrize("password_test", ["wrong_password", generate_string(1001), russian_chars(),
                                           russian_chars().upper(), chinese_chars(), special_chars(), sql_injection()],
                         ids=['invalid password', '1001 chars', 'russian', 'russian uppercase', 'chinese',
                              'special chars', 'sql injection 1'])
def test_auth_negative_password(web_browser, password_test):
    """ Негативные тесты на проверку поля id=password при авторизации """

    print("\n")

    page = RTAuth(web_browser)
    # проверка, что на странице есть username input
    assert page.username_input.find()

    # print("username =", username_test)

    page.tab_mail.click()
    page.username_input.send_keys(EMAIL_VALID)
    page.password_input.send_keys(password_test)

    # на случай, если есть капча
    page.wait_for_captcha()

    page.login_button.click()

    time.sleep(2)  # задержка для смены страницы после аутентификации

    assert page.incorrect_user_error.find()  # проверка наличия сообщения об ошибке авторизации
    assert "rt-link--orange" in page.forgot_password_link.get_attribute("class")  # оранжевая ссылка "Забыл пароль"

    time.sleep(2)

