#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import re
import commands
from alexa import Alexa
from youtube import YoutubeClient

from webwhatsapi import WhatsAPIDriver
from webwhatsapi.objects.message import Message

youtube = YoutubeClient()
alexa = Alexa()


def get_mention(msg):
	# print msg.js_obj
	return '@{}'.format(msg.js_obj['sender']['pushname'])


def group_handler(msg):
	pass


def parse(msg, cnt):
	if msg.safe_content == "":
		# when people send emojis
		return
	elif re.search('alexa', msg.safe_content, re.IGNORECASE):
		reply = alexa.say(msg.safe_content)
		cnt.chat.send_message(reply)
		return
	elif msg.safe_content[0] != '!':
		return

	arg_array = msg.safe_content.strip().split(' ')
	command = arg_array[0][1:]
	args = arg_array[1:]

	print command
	print args

	if command.lower() == 'info':
		cnt.chat.send_message(commands.info())

	elif command.lower() == 'discord':
		cnt.chat.send_message('{} {}'.format(get_mention(msg), commands.discord()))

	elif command.lower() == 'youtube' or command.lower() == 'song':
		response = youtube.get_video(' '.join(args))
		print response
		cnt.chat.send_message(response)



	if msg.js_obj['isGroupMsg']:
		group_handler(msg)


driver = WhatsAPIDriver(profile='C:\\Users\\Ali\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\alx932ri.Xetera')
print "Waiting for QR"
driver.wait_for_login()

print "Bot started"

while True:
	time.sleep(1)
	for contact in driver.get_unread():
		for message in contact.messages:
			if isinstance(message, Message):  # Currently works for text messages only.

				print message
				# print message.js_obj
				# print message.js_obj['isGroupMsg']
				parse(message, contact)

