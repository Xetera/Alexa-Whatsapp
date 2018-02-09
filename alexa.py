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
		"""
		Getting the initial conversation start, this either has to be
		saved to a database or fetched at startup every single time
		"""
		r = requests.get(self.cs_endpoint)
		return r.json()['cs']

	def _format_query_endpoint(self, text):
		"""Fetching formatted endpoint """
		return 'http://www.cleverbot.com/getreply?key={}&input={}&cs={}'\
			.format(secret.CLEVERBOT_API_KEY, text, self.cs)

	def _format_question(self, text):
		"""Replacing the word alexa to avoid confusing cleverbot"""
		return re.sub(constants.TRIGGER_WORD, 'cleverbot', text, re.IGNORECASE)

	def say(self, text):
		"""Ask alexa a question"""
		print "Asking {}...".format(constants.TRIGGER_WORD)
		interaction = urllib.quote_plus(self._format_question(text))
		query = self._format_query_endpoint(interaction)
		r = requests.get(query)
		reply = r.json()['output']
		print "{0} replied: {1}".format(constants.TRIGGER_WORD, reply)
		return reply

