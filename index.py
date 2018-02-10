#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import re
import commands
from alexa import Alexa
from youtube import YoutubeClient
import secret
import constants

from webwhatsapi import WhatsAPIDriver
from webwhatsapi.objects.message import Message


if secret.YOUTUBE_API_KEY:
	youtube = YoutubeClient()

alexa = Alexa()


def configure():
	pass # configuring settings here


def get_phone_number(msg):
	# regex matching id to phone number
	phone = re.search('\d+(?=@\w.\w{2,3})', msg.js_obj['sender']['id']).group(0)
	return '@{}'.format(phone)


def group_handler(msg):
	pass  # TODO


def change_trigger_word(cnt, word):
	previous_trigger = constants.TRIGGER_WORD
	constants.TRIGGER_WORD = word
	cnt.chat.send_message("OK, I was listening for {} but I'll respond to {} from now.".format(previous_trigger, word))


def parse_audio(msg, cnt):
	pass  # when audio is received


def parse_message(msg, cnt):
	if not msg.safe_content or msg.safe_content == "":
		# message is empty. Triggered when messages only contain emojis
		return
	elif re.search("({}|@{})".format(constants.TRIGGER_WORD, secret.BOT_PHONE_NUMBER), msg.safe_content, re.IGNORECASE):
		# upon hearing trigger word
		reply = alexa.say(msg.safe_content)
		cnt.chat.send_message(reply)
		return

	elif msg.safe_content[0] != '!':
		# message didn't start with !
		return

	parsed_message = msg.safe_content.strip().split(' ')
	command = parsed_message[0][1:]  # single command
	args = parsed_message[1:]        # args are in a list split by the word

	if command.lower() == 'info':
		cnt.chat.send_message(commands.info())

	elif command.lower() == 'discord':
		cnt.chat.send_message('{} {}'.format(get_phone_number(msg), commands.discord()))

	elif command.lower() == 'youtube' or command.lower() == 'song':
		if not youtube:
			return
		response = youtube.get_video(' '.join(args))
		cnt.chat.send_message(response)

	elif command.lower() == 'mention':
		cnt.chat.send_message(get_phone_number(msg))

	elif command.lower() == 'respond':
		change_trigger_word(cnt, args[0])


driver = WhatsAPIDriver(profile=secret.PROFILE or None)
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


