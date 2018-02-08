# -*- coding: utf-8 -*-

import sys
# sys.setdefaultencoding() does not exist, here!
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')

import constants
import secret
import pprint
import json
from youtubeapi import YoutubeAPI


class YoutubeClient:
	def __init__(self):
		self.youtube = YoutubeAPI({"key": secret.YOUTUBE_API_KEY})
		print "Youtube API Authenticated"

	def _search_by_video_name(self, name):
		search = self.youtube.search(name)
		# pprint.pprint(search)
		for i in search:
			if i['id']['kind'] == 'youtube#video':
				# we don't want to return channels or ads
				return i


	@staticmethod
	def _parse_video_url(packet):
		try:
			description = packet['snippet']['description'].encode('utf-8')
			return '{}\n{}\nDescription: {}'\
				.format(
					packet['snippet']['title'],
					YoutubeClient._build_url(packet['id']['videoId']),
					YoutubeClient._trim_description(description)
				)
		except KeyError as e:
			print packet

	@staticmethod
	def _build_url(video_id):
		return 'https://youtu.be/{}'.format(video_id)

	@staticmethod
	def _trim_description(desc):
		return desc if len(desc) <= 50 else u'{}...'.format(desc[:50])

	def get_video(self, search):
		print "Getting video {}".format(search)
		packet = self._search_by_video_name(search)
		return YoutubeClient._parse_video_url(packet)
