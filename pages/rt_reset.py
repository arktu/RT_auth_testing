import time
from pages.rt_page import RTPage
from pages.elements import WebElement
from constants import *


# класс страницы "Восстановление пароля"
class RTReset(RTPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = RESET_URL

        super().__init__(web_driver, url)

    reset_title = WebElement(css_selector='h1[class="card-container__title"]')
    reset_button = WebElement(id='reset')  # кнопка "Продолжить"

    username_input = WebElement(id='username')  # логин

    # табы вариантов логина
    tab_phone = WebElement(id="t-btn-tab-phone")  # таб "телефон"
    tab_mail = WebElement(id="t-btn-tab-mail")  # таб "почта"
    tab_login = WebElement(id="t-btn-tab-login")  # таб "логин"
    tab_ls = WebElement(id="t-btn-tab-ls")  # таб "лицевой счет"

    # span элемент с ошибкой о пустом поле логина
    empty_username_error = WebElement(css_selector=
                                      'span[class="rt-input-container__meta rt-input-container__meta--error"]')

    # ошибка с текстом "Неверный логин или текст с картинки"
    incorrect_user_error = WebElement(css_selector='p[class="card-container__error"]')

    # radio-кнопки для выбора вида восстановления пароля
    radio_phone = WebElement(xpath='//span[.="По номеру телефона" and @class="rt-radio__container"]')
    radio_email = WebElement(xpath='//span[.="По e-mail" and @class="rt-radio__container"]')

    # кнопка "Продолжить"
    submit_button = WebElement(css_selector='button[type="submit"]')

    page_code_enter_email = WebElement(xpath='//p[contains(text(),"Код подтверждения отправлен на адрес")]')
    page_code_enter_phone = WebElement(xpath='//p[contains(text(),"Код подтверждения отправлен на номер")]')

    # кнопки "Вернуться назад"
    back_button = WebElement(css_selector='button[name="back_to_login"]')
    cancel_button = WebElement(css_selector='button[name="cancel_reset"]')

    # локаторы ввода кода
    rt_code0 = WebElement(id="rt-code-0")
    rt_code1 = WebElement(id="rt-code-1")
    rt_code2 = WebElement(id="rt-code-2")
    rt_code3 = WebElement(id="rt-code-3")
    rt_code4 = WebElement(id="rt-code-4")
    rt_code5 = WebElement(id="rt-code-5")
    # rt_codes = {0: WebElement(id="rt-code-0"), 1: WebElement(id="rt-code-1"), 2: WebElement(id="rt-code-2"),
    #             3: WebElement(id="rt-code-3"), 4: WebElement(id="rt-code-4"), 5: WebElement(id="rt-code-5")}

    # локатор ошибки после ввода ошибочного кода
    code_error = WebElement(xpath='//*[contains(text(), "Неверный код. Повторите попытку")]')