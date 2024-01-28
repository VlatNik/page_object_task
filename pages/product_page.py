from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

	def adding_to_basket(self):
		self.browser.find_element(*ProductPageLocators.add_button).click()
		
	def should_be_messages_about_product(self):
		self.should_be_message_about_add()
		self.should_be_message_about_price()
		self.should_be_correct_name()
		self.should_be_correct_price()
		
	def should_be_message_about_add(self):
		assert self.is_element_present(*ProductPageLocators.message_add), "Message about add is not presented"
		
	def should_be_correct_name(self):
		assert self.browser.find_element(*ProductPageLocators.product_name_in_card).text == self.browser.find_element(*ProductPageLocators.product_name_in_message).text, "Product name is not correct"

	def should_be_message_about_price(self):
		assert self.is_element_present(*ProductPageLocators.message_price), "Price message is not presented"
		
	def should_be_correct_price(self):
		assert self.browser.find_element(*ProductPageLocators.price_in_card).text == self.browser.find_element(*ProductPageLocators.price_in_message).text, "Price is not correct"