from appium.webdriver.common.by import By

from ..base_page import BasePage


class HomePageElements(BasePage):

	def __init__(self, driver):
		super().__init__(driver)
		self.menu_button = (By.ID, "react-burger-menu-btn")
		self.logout_link = (By.ID, "logout_sidebar_link")

