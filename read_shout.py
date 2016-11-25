#!/usr/bin/python2

import urllib
import httplib
import os
import ConfigParser
import StringIO
import json
import optparse
import time

description = "Ast4u.me Shoutbox Scrapper."
usage = "usage: %prog [-t timestamp]"
parser = optparse.OptionParser(description=description, usage=usage)
parser.add_option("-t", "--timestamp", dest="timestamp",
                  help="set specific unix timestamp since when messages should be returned. Defaults to current time.", type="int")
parser.add_option("-d", "--debug", dest="debug")

(options, args) = parser.parse_args()
if options.timestamp:
    timestamp = options.timestamp
else:
    timestamp = int(time.time())

conf_str = "[dummy]\n" + open(os.path.join(os.curdir,"read_shout.conf")).read()
conf_fp = StringIO.StringIO(conf_str)
config = ConfigParser.RawConfigParser()
config.readfp(conf_fp)
conf_uid = config.get('dummy', 'uid')
conf_pass = config.get('dummy', 'pass')
conf_passhash = config.get('dummy', 'passhash')

user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36'
values = {'rmode': 'fill', 'userid':conf_uid}
headers = { 'User-Agent' : user_agent,
            'Cookie': 'uid=' + conf_uid + '; pass=' + conf_pass + '; passhash=' + conf_passhash + ';'}
c = httplib.HTTPSConnection("ast4u.me")

if options.debug:
    c.set_debuglevel(1)

values['ts'] = str(timestamp)
c.request("GET", "/shoutbox.ajax.load.php?" + urllib.urlencode(values), "", headers)
response = c.getresponse()

collect = {}
if (response.status == 200):
    raw_data = response.read()
    json_data = json.loads(raw_data)
    for msg in json_data['messages']:
        if msg['username'] == 'Waschbaer':
            collect[int(msg['mid'])] = msg['text_message']

print(json_data['timestamp'])
for key, text in sorted(collect.items(), reverse=True):
    print(text)

