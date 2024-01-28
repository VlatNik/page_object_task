from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

	def adding_to_basket(self):
		self.browser.find_element(*ProductPageLocators.ADD_BUTTON).click()
		
	def should_be_messages_about_product(self):
		self.should_be_message_about_add()
		self.should_be_message_about_price()
		self.should_be_correct_name()
		self.should_be_correct_price()
		
	def should_be_message_about_add(self):
		assert self.is_element_present(*ProductPageLocators.MESSAGE_ADD), "Message about add is not presented"
		
	def should_be_correct_name(self):
		assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_CARD).text == self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE).text, "Product name is not correct"

	def should_be_message_about_price(self):
		assert self.is_element_present(*ProductPageLocators.MESSAGE_PRICE), "Price message is not presented"
		
	def should_be_correct_price(self):
		assert self.browser.find_element(*ProductPageLocators.PRICE_IN_CARD).text == self.browser.find_element(*ProductPageLocators.PRICE_IN_MESSAGE).text, "Price is not correct"
		
	def should_not_be_success_message(self):
		assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ADD), "Success message is presented, but should not be"
		
	def should_not_be_success_message_dissapeared(self):
		assert self.is_disappeared(*ProductPageLocators.MESSAGE_ADD), "Success message is presented, but should not be"
		
