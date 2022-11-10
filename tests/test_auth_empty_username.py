# import time
# import pytest
from pages.rt_auth import *


# python -m pytest -v --driver Chrome --driver-path chromedriver tests\test_auth_empty_username.py
def test_auth_empty_username(web_browser):
    """ Проверка авторизации с пустыми телефоном/почтой/логином/ЛС """

    print("\n")

    page = RTAuth(web_browser)

    # проверка, что мы на странице Авторизации
    assert page.username_input.find()

    tabs = {1: page.tab_phone, 2: page.tab_mail, 3: page.tab_login, 4: page.tab_ls}

    # проходимся по всем табам и проверяем ввод пустого username
    for i in tabs.keys():
        tabs[i].click()
        if i == 1:
            page.username_input.send_keys("")
            page.password_input.send_keys("test_password")
        page.login_button.click()

        page.empty_username_error.find()
        # print(i, page.empty_username_error.get_text())
        assert page.empty_username_error.get_text() != ""
        time.sleep(1)  # успеваем посмотреть вывод ошибки


