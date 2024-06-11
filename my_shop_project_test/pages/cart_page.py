import time

from selene import browser, have, by
import allure

class CartPage:
    with allure.step("Book search"):
        def find_item(self):

            browser.element(".header__search input").type(
                "Искусственный интеллект с примерами на Python. Создание приложений искусственного интеллекта"
            ).press_enter()
            browser.element(".header__search input").with_(timeout=200).should(have.value(
                "Искусственный интеллект с примерами на Python. Создание приложений искусственного интеллекта"
            ))
            # time.sleep(5)
            return self
    #
    with allure.step("Open product page"):
        def open_page_item(self):
            browser.element('.item .item__title').click()
            browser.element('[to="#reviews"] [class="md:block"]').with_(timeout=50).should(have.text("Задать вопрос"))
            # time.sleep(6)
            return self

    with allure.step("Click add to cart"):
        def click_add_to_cart(self):
            browser.element('.form-control>.field.flex-grow>button').click()
            browser.element('[href="/my/cart"] .badge').with_(timeout=100).should(have.exact_text('1'))
            # time.sleep(6)
            return self

    with allure.step("Open cart"):
        def open_cart(self):
            browser.element('[href="/my/cart"]').click()
            browser.element('[class="cart-sort-pane__control"]').with_(timeout=50).should(have.text("Выбрать всё"))
            # time.sleep(6)
            return self

    with allure.step("Clear cart"):
        def clear_cart(self):
            browser.element('.cart-item .icon__delete').click()
            browser.element(".h2").with_(timeout=50).should(have.text("Удаление товаров"))
            # time.sleep(6)
            return self

    with allure.step("Confirm clear cart"):
        def confirm_clear_cart(self):
            browser.element(
                ' .popup-modal .cart-confirm__btns'
            ).element(by.text('Удалить')).click()

            return self

    with allure.step("Assert text cart"):
        def assert_page_cart(self):
            browser.element('.wrap h3').with_(timeout=50).should(
                have.text('Ваша корзина пуста')
            )

            return self

cart = CartPage()
