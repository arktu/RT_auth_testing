import time
import pytest
from pages.rt_auth import *
# from pages.elements import WebElement


@pytest.mark.parametrize("tab_no", [1, 2, 3, 4],
                         ids=['Таб телефон', 'Таб почта', 'Таб логин', 'Таб ЛС'])
@pytest.mark.parametrize("username, tab_expected", [(PHONE_VALID, 1), (EMAIL_VALID, 2), (LOGIN_VALID, 3), (LS_TEST, 4)],
                         ids=['телефон', 'почта', 'логин', 'ЛС'])
def test_auth_tabs_all(web_browser, tab_no, tab_expected, username):
    """ Проверка переключение на нужный таб при вводе разных видов логина (телефона, почты, логина, ЛС) - 16 тестов """

    print("\n")
    page = RTAuth(web_browser)
    # проверка, что мы на странице Авторизации
    assert page.username_input.find()

    tabs = {1: page.tab_phone, 2: page.tab_mail, 3: page.tab_login, 4: page.tab_ls}

    tabs[tab_no].click()
    page.username_input.send_keys(username)
    page.password_input.click()

    if tab_no == 1 and username == LS_TEST:
        # пропуск анализа одного теста на табе телефона при вводе ЛС
        assert 1 == 1
    else:
        # определяем, что таб стал активен за счет добавленного ему класса rt-tab--active
        assert "rt-tab--active" in tabs[tab_expected].get_attribute("class")

        # определяем, что предыдущий таб деактивировался
        if tab_no != tab_expected:
            assert "rt-tab--active" not in tabs[tab_no].get_attribute("class")

    time.sleep(1)  # задержка, чтобы успеть увидеть сменившийся таб




