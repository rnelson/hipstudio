#!/usr/bin/env python3
import hipchat
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
hc_token = config['HipChat'].get('Token')

hc = hipchat.HipChat(token=hc_token)
rooms = hc.list_rooms()

print('ID\tName\t\t\tTopic')
print('-------------------------------------------------------------------------------')
for room in rooms['rooms']:
    name = room['name']
    id = room['room_id']
    archived = room['is_archived']
    topic = room['topic']

    if not archived:
        print("%d\t%s\t\t\t%s" % (id, name, topic))