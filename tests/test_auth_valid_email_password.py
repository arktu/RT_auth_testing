import time
from pages.rt_auth import *
from pages.elements import WebElement


def test_auth_valid_email_password(web_browser):
    """ Проверка авторизации по email зарегистрированного пользователя """

    print("\n")

    page = RTAuth(web_browser)

    # time.sleep(2)
    # проверка, что мы на странице Авторизации
    assert page.username_input.find()
    assert page.password_input.find()
    # assert page.auth_title.get_text() == "Авторизация"
    # assert page.search.get_text() == "Войти"

    page.tab_mail.click()
    page.username_input.send_keys(EMAIL_VALID)
    page.password_input.send_keys(PASSWORD_VALID)

    # проверка, что сменился таб авторизации на "Почта"
    # assert "rt-tab--active" in page.tab_mail.get_attribute("class")
    # assert page.tab_mail_active.find()

    # на случай, если есть капча
    page.wait_for_captcha()

    page.login_button.click()

    time.sleep(3)  # задержка для смены страницы после аутентификации
    assert page.user_fio.find()
    # print("title =", page.user_fio.get_attribute("title"))
    assert page.user_fio.get_attribute("title") == USER_FIO_VALID

    time.sleep(4)

