from ..elements.home_page_elements import HomePageElements


# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------

class HomePageActions(HomePageElements):

	def __init__(self, driver):
		super().__init__(driver)

# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------

	def perform_logout(self):
		self.click(self.menu_button)
		self.click(self.logout_link)
		return self

# --------------------------------------------------------------------------------
