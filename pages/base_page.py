from appium import webdriver
from appium.webdriver.common.by import By
from appium.webdriver.support import expected_conditions
from appium.webdriver.support.ui import WebDriverWait


# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------

class BasePage:
	"""
	Base class used for common page functionality
	"""
	def __init__(self, driver: webdriver):
		self.driver: webdriver = driver
		self.wait = WebDriverWait(self.driver, 10)

# --------------------------------------------------------------------------------

	def wait_visibility(self, locator):
		return self.wait.until(expected_conditions.element_to_be_clickable(locator))

# --------------------------------------------------------------------------------

	def click(self, locator):
		return self.wait_visibility(locator).click()

# --------------------------------------------------------------------------------

	def clear(self, locator):
		return self.wait_visibility(locator).clear()

# --------------------------------------------------------------------------------

	def write_text(self, locator, text):
		return self.wait_visibility(locator).send_keys(text)

# --------------------------------------------------------------------------------

	def read_text(self, locator):
		return self.wait_visibility(locator).text

# --------------------------------------------------------------------------------

	def read_alert_text(self):
		self.wait.until(expected_conditions.alert_is_present())
		return self.driver.switch_to.alert.text

# --------------------------------------------------------------------------------

	def accept_alert(self):
		self.wait.until(expected_conditions.alert_is_present())
		return self.driver.switch_to.alert.accept()

# --------------------------------------------------------------------------------

	def dismiss_alert(self):
		self.wait.until(expected_conditions.alert_is_present())
		return self.driver.switch_to.alert.dismiss()

# --------------------------------------------------------------------------------

	def current_url(self):
		return self.driver.current_url

# --------------------------------------------------------------------------------

	def current_endpoint_is(self, endpoint):
		assert self.current_url().endswith(endpoint)
		return self

# --------------------------------------------------------------------------------
