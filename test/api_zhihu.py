# -*- coding: utf-8 -*-
import sys, urllib, urllib2, json


url = 'http://api.kanzhihu.com/getposts/'
req = urllib2.Request(url)


resp = urllib2.urlopen(req)
content = resp.read()
if(content):
	contentjson = json.loads(content)
	print(type(contentjson))
	for key,value in contentjson.items():
		print key,type(value)

	for value in contentjson["posts"]:
		print "date:",value["date"],"name:",value["name"],"publishtime:",value["publishtime"]
		content=value["excerpt"].split(u"、")
		for name in content:
			print name
