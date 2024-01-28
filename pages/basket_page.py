from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
		
	def should_not_be_products_in_basket(self):
		assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Items in busket is presented"
	
	def should_be_message_about_empty_basket(self):
		assert self.is_element_present(*BasketPageLocators.MESSAGE_ABOUT_EMPTY_BASKET), "Message about empty is not presented"
		
