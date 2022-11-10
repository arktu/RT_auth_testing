import time
from pages.rt_auth import *
# from pages.elements import WebElement


def test_auth_valid_phone_password(web_browser):
    """ Проверка авторизации по телефону зарегистрированного пользователя """

    print("\n")

    page = RTAuth(web_browser)

    # проверка, что мы на странице Авторизации
    assert page.username_input.find()
    assert page.password_input.find()

    page.tab_login.click()
    page.username_input.send_keys(LOGIN_VALID)
    page.password_input.send_keys(PASSWORD_VALID)

    # на случай, если есть капча
    page.wait_for_captcha()

    page.login_button.click()

    time.sleep(3)  # задержка для смены страницы после аутентификации
    assert page.user_fio.find()
    assert page.user_fio.get_attribute("title") == USER_FIO_VALID

    time.sleep(4)

