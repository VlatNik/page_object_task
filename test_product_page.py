from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
	page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0")
	page.open()
	page.adding_to_basket()
	page.solve_quiz_and_get_code()
	page.should_be_messages_about_product()

@pytest.mark.need_review	
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
	page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/")
	page.open()
	page.go_to_basket_page()
	basket_page = BasketPage(browser, browser.current_url)
	basket_page.should_not_be_products_in_basket()
	basket_page.should_be_message_about_empty_basket()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page (browser):
	page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/")
	page.open()
	page.go_to_login_page()

@pytest.mark.skip
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
	page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
	page.open()
	page.adding_to_basket()
	page.should_not_be_success_message()
	
@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
	page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
	page.open()
	page.should_not_be_success_message()
	
@pytest.mark.skip
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
	page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
	page.open()
	page.adding_to_basket()
	page.should_not_be_success_message_dissapeared()

@pytest.mark.skip	
def test_guest_should_see_login_link_on_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = ProductPage(browser, link)
	page.open()
	page.should_be_login_link()
		

class TestUserAddToBasketFromProductPage():
	@pytest.fixture(scope="function", autouse=True)
	def setup(self, browser):
		email = str(time.time()) + "@yandex.org"
		password = str(time.time())
		print(email + "/" + password)
		page = LoginPage(browser, "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/")
		page.open()
		page.register_new_user(email, password)
		page.should_be_authorized_user()
	@pytest.mark.skip	
	def test_user_cant_see_success_message(self,browser):
		page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
		page.open()
		page.should_not_be_success_message()
	@pytest.mark.need_review
	def test_user_can_add_product_to_basket(self,browser):
		page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
		page.open()
		page.adding_to_basket()
		page.should_be_messages_about_product()