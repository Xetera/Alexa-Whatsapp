import constants
import secret
import requests
import re
import urllib


class Alexa:
	def __init__(self):
		self.cs_endpoint = 'https://www.cleverbot.com/getreply?key={}'.format(secret.CLEVERBOT_API_KEY)
		self.cs = self._get_cs()
		print "CS: {}".format(self.cs)

	def _get_cs(self):
		r = requests.get(self.cs_endpoint)
		return r.json()['cs']

	def _format_query_endpoint(self, text):
		return 'http://www.cleverbot.com/getreply?key={}&input={}&cs={}'\
			.format(secret.CLEVERBOT_API_KEY, text, self.cs)

	def _format_question(self, text):
		return re.sub('alexa', 'cleverbot', text, re.IGNORECASE)

	def say(self, text):
		print "Asking alexa..."
		interaction = urllib.quote_plus(self._format_question(text))
		query = self._format_query_endpoint(interaction)
		r = requests.get(query)
		print "Alexa replied: {}".format(r.json()['output'])
		return r.json()['output']

