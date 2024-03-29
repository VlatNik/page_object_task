from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait

class LoginPage(BasePage):
	def should_be_login_page(self):
		self.should_be_login_url()
		self.should_be_login_form()
		self.should_be_register_form()
		
	def should_be_login_url(self):
		assert "login" in self.browser.current_url, "Login is not presented in url"

	def should_be_login_form(self):
		assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

	def should_be_register_form(self):
		assert self.is_element_present(*LoginPageLocators.REG_FORM), "Register form is not presented"
		
	def register_new_user(self,email,password):
		self.browser.find_element(*LoginPageLocators.EMAIL_ADRESS_FIELD).send_keys(email)
		self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(password)
		self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_FIELD).send_keys(password)
		self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()