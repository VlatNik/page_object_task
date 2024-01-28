from selenium.webdriver.common.by import By


class ProductPageLocators():
	add_button = (By.CSS_SELECTOR, ".btn-add-to-basket")
	message_add = (By.CSS_SELECTOR, ".alertinner")
	message_price = (By.CSS_SELECTOR, "#messages > div.alert-info > div")
	product_name_in_message = (By.CSS_SELECTOR, ".alertinner > strong")
	price_in_message = (By.CSS_SELECTOR, ".alertinner > p > strong")
	product_name_in_card = (By.CSS_SELECTOR, ".product_main > h1")
	price_in_card = (By.CSS_SELECTOR, ".product_main > .price_color")
	
class BasePageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
	