from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

@pytest.mark.skip
def test_guest_can_add_product_to_basket(browser, link):
	#link = f"{link}"
	page = ProductPage(browser, f"{link}")
	page.open()
	page.adding_to_basket()
	page.solve_quiz_and_get_code()
	page.should_be_messages_about_product()
	
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
	
class TestUserAddToBasketFromProductPage():
	@pytest.fixture(scope="function", autouse=True)
	def setup(self, browser):
		email = str(time.time()) + "@yandex.org"
		password = str(time.time())
		print(email + "/" + password)
		page = LoginPage(browser, "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/")
		page.open()
		page.register_new_user(email, password)
		browser.implicitly_wait(5)
		page.should_be_authorized_user()
	def test_user_cant_see_success_message(self,browser):
		page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
		page.open()
		page.should_not_be_success_message()
	def test_user_can_add_product_to_basket(self,browser):
		page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
		page.open()
		page.adding_to_basket()
		#page.solve_quiz_and_get_code()
		page.should_be_messages_about_product()