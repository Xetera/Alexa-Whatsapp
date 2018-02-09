#!/usr/bin/env python
# -*- coding: utf-8 -*-


import time
import re
import commands
from alexa import Alexa
from youtube import YoutubeClient

from webwhatsapi import WhatsAPIDriver
from webwhatsapi.objects.message import Message
import secret
import constants

"""
import sys
# sys.setdefaultencoding() does not exist, here!
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')
"""
youtube = YoutubeClient()
alexa = Alexa()


def get_phone_number(msg):
	# regex matching id to phone number
	phone = re.search('\d+(?=@\w.\w{2,3})', msg.js_obj['sender']['id']).group(0)
	return '@{}'.format(phone)


def group_handler(msg):
	pass


def change_trigger_word(cnt, word):
	previous_trigger = constants.TRIGGER_WORD
	constants.TRIGGER_WORD = word
	cnt.chat.send_message("OK, I was listening for {} but I'll respond to {} from now.".format(previous_trigger, word))


def parse_audio(msg, cnt):
	pass


def parse_message(msg, cnt):
	if not msg.safe_content or msg.safe_content == "":
		# message is empty i.e. there was an emoji
		return
	elif re.search("({}|@{})".format(constants.TRIGGER_WORD, secret.BOT_PHONE_NUMBER), msg.safe_content, re.IGNORECASE):
		# upon hearing trigger word
		reply = alexa.say(msg.safe_content)
		cnt.chat.send_message(reply)
		return

	elif msg.safe_content[0] != '!':
		# message didn't start with !
		return

	arg_array = msg.safe_content.strip().split(' ')
	command = arg_array[0][1:]
	args = arg_array[1:]

	print command
	print args

	if command.lower() == 'info':
		cnt.chat.send_message(commands.info())

	elif command.lower() == 'discord':
		cnt.chat.send_message('{} {}'.format(get_phone_number(msg), commands.discord()))

	elif command.lower() == 'youtube' or command.lower() == 'song':
		response = youtube.get_video(' '.join(args))
		print response

		cnt.chat.send_message(response)
	elif command.lower() == 'mention':
		cnt.chat.send_message(get_phone_number(msg))

	elif command.lower() == 'respond':
		change_trigger_word(cnt, args[0])


	# stub
	if msg.js_obj['isGroupMsg']:
		group_handler(msg)


driver = WhatsAPIDriver(profile=secret.PROFILE)
print "Waiting for QR"
driver.wait_for_login()

print "Bot started"

while True:
	time.sleep(1)
	for contact in driver.get_unread():
		for message in contact.messages:
			if isinstance(message, Message):  # Currently works for text messages only.
				print message
				if message.js_obj['type'] == 'ptt':
					parse_audio(message, contact)
					break
				elif message.js_obj['type'] == 'chat':
					parse_message(message, contact)
	

