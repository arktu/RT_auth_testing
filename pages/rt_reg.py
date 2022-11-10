import time
from pages.rt_page import RTPage
from pages.elements import WebElement, ManyWebElements
from constants import *


# класс страницы "Регистрация"
class RTReg(RTPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = AUTH_URL
        super().__init__(web_driver, url)

    def click_register(self):
        """ Переход на страницу регистрации со страницы авторизации """
        self.register_ref.find()
        self.register_ref.click()

    register_ref = WebElement(id="kc-register")  # ссылка на страницу регистрации на странице авторизации

    first_name_input = WebElement(name="firstName")  # Имя
    last_name_input = WebElement(name="lastName")  # Фамилия
    phone_email_input = WebElement(id="address")
    password_input = WebElement(id="password")
    password_confirm_input = WebElement(id="password-confirm")

    reg_button = WebElement(name="register")  # кнопка "Зарегистрироваться"

    name_error = WebElement(xpath='//span[contains(text(), '
                                  '"Необходимо заполнить поле кириллицей. От 2 до 30 символов.")]')

    account_exists_text = WebElement(xpath='//h2[contains(text(), "Учётная запись уже существует")]')

    passwords_differ_error = WebElement(xpath='//span[contains(text(), "Пароли не совпадают")]')

    # ведите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru
    email_phone_error = WebElement(xpath='//span[contains(text(), "Введите телефон в формате")]')

    # 1 Длина пароля должна быть не менее 8 символов
    # 2 Пароль должен содержать хотя бы одну заглавную букву
    # 3 Пароль должен содержать только латинские буквы
    # 4 Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру
    # 5 Пароль не должен содержать пробелов
    password_error1 = WebElement(xpath='//span[contains(text(), "Длина пароля должна быть не менее 8 символов")]')
    password_error2 = WebElement(xpath='//span[contains(text(), "Пароль должен содержать хотя бы одну заглавную букву")]')
    password_error3 = WebElement(xpath='//span[contains(text(), "Пароль должен содержать только латинские буквы")]')
    password_error4 = WebElement(xpath='//span[contains(text(), "Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру")]')
    password_error5 = WebElement(xpath='//span[contains(text(), "Пароль не должен содержать пробелов")]')
    password_error6 = WebElement(xpath='//span[contains(text(), "должен") or contains(text(), "должна")]')

    # rt-base-icon rt-base-icon--fill-path rt-eye-icon rt-input__eye rt-input__eye
    # aria-hidden="true"
    password_eyes = ManyWebElements(css_selector='svg[class="rt-base-icon rt-base-icon--fill-path rt-eye-icon rt-input__eye rt-input__eye"]')

    title_confirm_email = WebElement(xpath='//h1[contains(text(), "Подтверждение email")]')
    # p Kод подтверждения отправлен на адрес arktur7001@yandex.ru
    title_confirm_phone = WebElement(xpath='//h1[contains(text(), "Подтверждение телефона")]')
    # Kод подтверждения отправлен на номер +7 905 992-89-47

    # локаторы ввода кода
    rt_code0 = WebElement(id="rt-code-0")
    rt_code1 = WebElement(id="rt-code-1")
    rt_code2 = WebElement(id="rt-code-2")
    rt_code3 = WebElement(id="rt-code-3")
    rt_code4 = WebElement(id="rt-code-4")
    rt_code5 = WebElement(id="rt-code-5")

    code_error = WebElement(xpath='//span[contains(text(), "Неверный код")]')  # . Повторите попытку