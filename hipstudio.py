#!/usr/bin/env python3
from bottle import get, post, run, request, template
import simplejson as json
from smartchat import SmartChat
import configparser

PRODUCT = 'HipStudio'
VERSION = '0.0.1'
COPYRIGHT = 'Copyright (C) 2014 Ross Nelson'
LICENSE = 'MIT'

# Read the config file
config = configparser.ConfigParser()
config.read('config.ini')

# Set our configuration variables
HOST = config['WebServer'].get('Host', '0.0.0.0')
PORT = config['WebServer'].get('Port', 1984)
BOT_NAME = config['HipChat'].get('Name')
HIPCHAT_TOKEN = config['HipChat'].get('Token')
HIPCHAT_ROOM_ID = config['HipChat'].get('Room')


# Print out some info if a user tries to visit the url
@get('/')
def index():
    content = """    <!DOCTYPE html>
    <html lang="en">
        <head>
            <title>HipSmart</title>
        </head>
        <body>
            <h1>Welcome to HipSmart</h1>
            <p>
                This server is made to receive and act upon
                <a href="http://www.visualstudio.com/en-us/get-started/dn741288">Visual Studio Online
                service hooks</a>.
            </p>
            <p>
                To use it, configure each type of service hook that you want and point it to port 1984
                on this machine.
            </p>
        </body>
    </html>
"""
    return template(content, host=HOST, port=PORT)

# Handle POSTs to /
@post('/')
def index():
    data = json.loads(request.body.read())
    print(data)

    chat = SmartChat(BOT_NAME, HIPCHAT_TOKEN, HIPCHAT_ROOM_ID)

    if 'build.complete' == data['eventType']:
        name = data['resource']['name']
        status = data['resource']['status']
        date = data['createdDate']

        message = 'Build ' + name + ' ' + status + ' (' + date + ')'
        if 'succeeded' == status:
            chat.success(message)
        elif 'failed' == status:
            chat.error(message)
        else:
            chat.info(message)
    elif 'message.posted' == data['eventType']:
        content = data['resource']['content']
        date = data['resource']['postedTime']
        name = data['resource']['postedBy']['displayName']

        message = 'Chat: ' + date + ' <' + name + '>: ' + content
        chat.yellow(message)
    elif 'git.pullrequest.created' == data['eventType']:
        id = str(data['resource']['pullRequestId'])
        name = data['resource']['createdBy']['displayName']
        date = data['resource']['creationDate']
        title = data['resource']['title']

        # Swap src/dest because sourceRef is where you're creating the PR, which
        # is the destination for the merge
        destination = data['resource']['sourceRefName']
        source = data['resource']['targetRefName']

        message = 'New PR #' + id + ': ' + title + ' (' + source + ' => ' + destination + ') by ' + name + ' (' + date + ')'
        chat.info(message)
    elif 'git.pullrequest.updated' == data['eventType']:
        id = str(data['resource']['pullRequestId'])
        name = data['resource']['createdBy']['displayName']
        date = data['resource']['creationDate']
        title = data['resource']['title']

        # Swap src/dest because sourceRef is where you're creating the PR, which
        # is the destination for the merge
        destination = data['resource']['sourceRefName']
        source = data['resource']['targetRefName']

        message = 'Updated PR #' + id + ': ' + title + ' (' + source + ' => ' + destination + ') by ' + name + ' (' + date + ')'
        chat.info(message)
    elif 'git.push' == data['eventType']:
        repo = data['resource']['repository']['name']
        date = data['resource']['date']
        user = data['resource']['pushedBy']['displayName']
        branch = data['resource']['refUpdates'][0]['name']

        message = user + ' pushed to ' + branch + ' on ' + repo + ' (' + date + ')'
        chat.info(message)
    elif 'workitem.created' == data['eventType']:
        chat.info(data['detailedMessage']['text'])
    elif 'workitem.commented' == data['eventType']:
        chat.info(data['detailedMessage']['text'])
    elif 'workitem.updated' == data['eventType']:
        chat.info(data['detailedMessage']['text'])

# Start the server
print(PRODUCT + ' v' + VERSION)
print(COPYRIGHT)
print('Licensed under the ' + LICENSE + ' license')
print('')
print('')
print(BOT_NAME + ' listening on ' + HOST + ':' + PORT)
print('Posting to HipChat room ' + HIPCHAT_ROOM_ID + ' with token ' + HIPCHAT_TOKEN)
print('')

run(host=HOST, port=PORT)
