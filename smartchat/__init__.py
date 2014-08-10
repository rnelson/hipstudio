#!/usr/bin/env python3
import hipchat


class SmartChat:
    COLORS = {
        'success': 'green',
        'warning': 'yellow',
        'error': 'red',
        'other': 'gray'
    }

    def __init__(self, name, token, room_id):
        self.name = name
        self.token = token
        self.room_id = room_id
        self.hipster = hipchat.HipChat(token=self.token)

    def post(self, message, message_color):
        self.hipster.message_room(self.room_id, self.name, message, color=message_color)

    def info(self, message):
        self.post(message, self.COLORS['other'])

    def success(self, message):
        self.post(message, self.COLORS['success'])

    def warn(self, message):
        self.post('WARNING: ' + message, self.COLORS['warning'])

    def yellow(self, message):
        self.post(message, 'yellow')

    def error(self, message):
        self.post('ERROR: ' + message, self.COLORS['error'])