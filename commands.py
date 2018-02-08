import constants
import requests


def info():
	"""General information about the bot"""

	out =   "Author: Xetera#9596\n" \
			"Version: {}\n".format(constants.BOT_VERSION)
	out +=  "Language: Python2.7\n" \
			"Lib: https://github.com/mukulhase/WebWhatsAPI"
	# docstrings don't format properly
	return out


def discord():
	"""Discord invite link to the shared whatsapp channels"""
	return 'Join our discord channel here! discord.gg/nZFVvTW'


