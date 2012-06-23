#!/usr/bin/python
# -*- coding: utf-8 -*-
# author: sullenlook <sullenlook@sullenlook.eu> 
# needs feedparser (easy_install feedparser)

import feedparser
from plugin import *


class mummmyi(Plugin):   

	@register("de-DE", ".*neues.*(blog|Rss).*")
	def mummmyi_updates(self, speech, language):
		if language == "de-DE":
			rss_url = "http://feeds.feedburner.com/MummMyIphoneFeed?format=xml"
			feed = feedparser.parse( rss_url )
			answer = self.ask("Updates mit zusammenfassung?")
			self.say("Aktuelles von Sullen Look's iPhone Blog:")
			feedcontent = ""
			for entry in feed["items"]:
				#self.say(entry["title"])
				if format(answer) == "Ja":
					#self.say(summary)
					feedcontent = feedcontent + "\"" + entry["title"] + "\": " + entry["summary"] + "\n\n"
				else:
					feedcontent = feedcontent + "\"" + entry["title"] + "\",\n"
			self.say(feedcontent, ' ')
		self.complete_request()



