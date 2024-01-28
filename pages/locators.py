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
	BASKET_LINK = (By.CSS_SELECTOR, ".btn-group > a.btn-default")
	USER_ICON = (By.CSS_SELECTOR, ".icon-user")
	
class BasketPageLocators():
	BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
	MESSAGE_ABOUT_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner")
	
class LoginPageLocators():
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
	REG_FORM = (By.CSS_SELECTOR, "#register_form")
	EMAIL_ADRESS_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
	PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
	CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
	REGISTER_BUTTON= (By.CSS_SELECTOR, "[name = registration_submit]")