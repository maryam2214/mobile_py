from configparser import ConfigParser
from os.path import dirname, realpath, exists


# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------

class ConfigReader:

	def __init__(self):
		self.config_file = "{}config.ini".format(dirname(realpath(__file__))[:-7])
		assert exists(self.config_file)
		self.config = ConfigParser()
		self.config.read(self.config_file)

# --------------------------------------------------------------------------------

	def browser(self):
		return self.config['CORE']['browser']

# --------------------------------------------------------------------------------

	def base_url(self):
		return self.config['CORE']['base_url']

# --------------------------------------------------------------------------------

	def username(self):
		return self.config['CORE']['username']

# --------------------------------------------------------------------------------

	def password(self):
		return self.config['CORE']['password']

# --------------------------------------------------------------------------------

	def locked_username(self):
		return self.config['CORE']['locked_username']

# --------------------------------------------------------------------------------

