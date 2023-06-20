from appium.webdriver.common.by import By
from ..base_page import BasePage


class LoginPageElements(BasePage):

	def __init__(self, driver):
		super().__init__(driver)
		self.login_button = (By.ID, "login-button")
		self.username_input = (By.ID, "user-name")
		self.password_input = (By.ID, "password")
		self.error_tick = (By.CSS_SELECTOR, "h3[data-test='error']")
