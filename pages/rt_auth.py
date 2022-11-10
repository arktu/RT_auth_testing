import time
from pages.rt_page import RTPage
from pages.elements import WebElement
from constants import *


# класс страницы "Авторизация"
class RTAuth(RTPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = AUTH_URL

        super().__init__(web_driver, url)

    auth_title = WebElement(css_selector='h1[class="card-container__title"]')
    login_button = WebElement(id='kc-login')  # кнопка "Войти"

    username_input = WebElement(id='username')  # логин
    password_input = WebElement(id='password')  # пароль

    # табы вариантов логина
    tab_phone = WebElement(id="t-btn-tab-phone")  # таб "телефон"
    tab_mail = WebElement(id="t-btn-tab-mail")  # таб "почта"
    tab_login = WebElement(id="t-btn-tab-login")  # таб "логин"
    tab_ls = WebElement(id="t-btn-tab-ls")  # таб "лицевой счет"

    # h2 элемент на странице пользователя с его ФИО
    user_fio = WebElement(css_selector='h2[class="user-name user-info__name"]')

    # span элемент с ошибкой о пустом поле логина
    empty_username_error = WebElement(css_selector=
                                      'span[class="rt-input-container__meta rt-input-container__meta--error"]')

    # ошибка с текстом "Неверный логин или пароль"
    incorrect_user_error = WebElement(css_selector='p[class="card-container__error login-form-container__error--bold"]')

    # ссылка "Забыли пароль"
    forgot_password_link = WebElement(id="forgot_password")
