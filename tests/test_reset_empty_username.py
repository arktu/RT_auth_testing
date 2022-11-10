# import time
# import pytest
from pages.rt_reset import *


def test_reset_empty_username(web_browser):
    """ Проверка выдачи ошибки при восстановлении пароля с пустым логином (телефон/почта/логин/ЛС) """

    print("\n")

    page = RTReset(web_browser)

    # проверка, что мы на странице есть поле id=username
    assert page.username_input.find()

    tabs = {1: page.tab_phone, 2: page.tab_mail, 3: page.tab_login, 4: page.tab_ls}

    # проходимся по всем табам и проверяем ввод пустого username
    for i in tabs.keys():
        tabs[i].click()
        if i == 1:
            page.username_input.send_keys("")
        page.submit_button.click()

        page.empty_username_error.find()
        # print(i, page.empty_username_error.get_text())
        assert page.empty_username_error.get_text() != ""
        time.sleep(1)  # успеваем посмотреть вывод ошибки


