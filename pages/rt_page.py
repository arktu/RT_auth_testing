import time
from pages.base import WebPage
from pages.elements import WebElement


# родительский класс для страниц Ростелеком
class RTPage(WebPage):

    def wait_for_captcha(self, captcha_timeout=15):
        if self.captcha_input.is_presented():
            self.captcha_input.click()
            time.sleep(captcha_timeout)  # задержка для ввода капчи вручную

    # captcha input поле
    captcha_input = WebElement(id='captcha')

