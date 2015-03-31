#!/usr/bin/env python3
from bottle import get, post, run, request, template
import simplejson as json
from smartchat import SmartChat
from dateutil.parser import parse
import configparser
from sys import exit

PRODUCT = 'HipStudio'
VERSION = '0.0.2'
COPYRIGHT = 'Copyright (C) 2014-2015 Ross Nelson'
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
DEFAULT_DATETIME_FORMAT = '%a, %d %b %Y at %I:%M %p'

def getname(vsoname):
    mappings = config['NameMappings']
    for hcname, vsname in mappings.items():
        if vsoname == vsname:
            return '@' + hcname

def formatdate(d):
    return parse(d).strftime(DEFAULT_DATETIME_FORMAT)


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
        date = formatdate(data['createdDate'])

        message = 'Build ' + name + ' ' + status + ' (' + date + ')'
        if 'succeeded' == status:
            chat.success(message)
        elif 'failed' == status:
            chat.error(message)
        else:
            chat.info(message)
    elif 'message.posted' == data['eventType']:
        content = data['resource']['content']
        date = formatdate(data['resource']['postedTime'])
        name = data['resource']['postedBy']['displayName']

        message = 'Chat: <' + name + '>: ' + content
        chat.yellow(message)
    elif 'git.pullrequest.created' == data['eventType']:
        id = str(data['resource']['pullRequestId'])
        name = data['resource']['createdBy']['displayName']
        date = formatdate(data['resource']['creationDate'])
        title = data['resource']['title']

        # Swap src/dest because sourceRef is where you're creating the PR, which
        # is the destination for the merge
        destination = data['resource']['sourceRefName']
        source = data['resource']['targetRefName']

        message = getname(name) + ' created pull request #' + id + ' ((branch)' + source + ' => (branch)' + destination + '): ' + title + ' (' + date + ')'
        chat.info(message)
    elif 'git.pullrequest.updated' == data['eventType']:
        id = str(data['resource']['pullRequestId'])
        name = data['resource']['createdBy']['displayName']
        date = formatdate(data['resource']['creationDate'])
        title = data['resource']['title']

        # Swap src/dest because sourceRef is where you're creating the PR, which
        # is the destination for the merge
        destination = data['resource']['sourceRefName']
        source = data['resource']['targetRefName']

        message = getname(name) + ' updated pull request #' + id + ' ((branch)' + source +' => (branch)' + destination + '): ' + title + ' (' + date + ')'
        chat.info(message)
    elif 'git.push' == data['eventType']:
        repo = data['resource']['repository']['name']
        date = formatdate(data['resource']['date'])
        user = data['resource']['pushedBy']['displayName']
        branch = data['resource']['refUpdates'][0]['name']

        message = getname(user) + ' pushed to (branch)' + branch + ' on ' + repo + ' (' + date + ')'
        chat.success(message)
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
