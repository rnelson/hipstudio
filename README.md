# HipStudio

## About

HipStudio is a small web application to allow [Visual Studio Online](http://visualstudio.com) to post messages to a 
[HipChat](http://hipchat.com) room.

VSO [already supports HipChat](http://www.visualstudio.com/en-us/get-started/dn741294), but I wanted to be able to 
better customize the messages being posted.

## Prerequisites

This project is written in Python 3 and requires a few third-party libraries. They can all be installed with pip 
(e.g., `pip3` on OS X if installed from [Homebrew](http://brew.sh), `pip-python3` on Fedora 20):

`pip3 install python-simple-hipchat bottle simplejson`

## Installation

There is no installation. Simply clone this repository somewhere, set up *config.ini*, and run *hipstudio.py*.

There is an included *config.ini.example* file. Copy this to *config.ini* and customize it to your liking.

The two values under `[WebServer]` set the IP to listen on (the default, *0.0.0.0*, means all interfaces--you probably 
want this) as well as the port.

`[HipChat]` contains settings for HipChat. *Name* is the name of the bot; this is what messages in HipChat show as 
coming from. *Room* and *Token* are the room ID and API token, respectively.

The included *list_room_ids.py* script will help you find the ID for your room. To use it, set an administrator 
token (not a notification token) in *config.ini* and simply run the script from the command line.

## License

This software is licensed under the MIT license.

Copyright (c) 2014 Ross Nelson

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
