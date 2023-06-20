# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------

class TestLogin:

	def test_empty_login(self, login_page, config):
		login_page.perform_login("", "").verify_error("Epic sadface: Username is required")

# --------------------------------------------------------------------------------

	#def test_empty_password(self, login_page, config):
	#	login_page.perform_login(config.username(), "").verify_error("Epic sadface: Password is required")

# --------------------------------------------------------------------------------

	#def test_locked_out_user(self, login_page, config):
	#	login_page.perform_login(config.locked_username(), config.password()).verify_error("Epic sadface: Sorry, this user has been locked out.")

# --------------------------------------------------------------------------------

	#def test_successful_login(self, login_page, config):
	#	login_page.perform_login(config.username(), config.password()).current_endpoint_is("inventory.html").perform_logout()

# --------------------------------------------------------------------------------
