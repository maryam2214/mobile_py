from ..elements.login_page_elements import LoginPageElements
from ..actions.home_page_actions import HomePageActions


# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------

class LoginPageActions(LoginPageElements):

	def __init__(self, driver):
		super().__init__(driver)

# --------------------------------------------------------------------------------

	def perform_login(self, username, password):
		print("hello in  log in func")
# --------------------------------------------------------------------------------

	def verify_error(self, error_msg):
		assert self.read_text(self.error_tick) == error_msg

# --------------------------------------------------------------------------------
