# HipStudio

## About

HipStudio is a small web application to allow [Visual Studio Online](http://visualstudio.com) to post messages to a 
[HipChat](http://hipchat.com) room.

VSO [already supports HipChat](http://www.visualstudio.com/en-us/get-started/dn741294), but I wanted to be able to 
better customize the messages being posted.



## Prerequisites

This project is written in Python 3 and requires a few third-party libraries:

+ [python-simple-hipchat](https://github.com/kurttheviking/python-simple-hipchat)
+ [bottle](http://bottlepy.org/docs/dev/index.html)
+ [simplejson](https://simplejson.github.io/simplejson/)

They can all be installed with pip.

`pip3 install python-simple-hipchat bottle simplejson`

The following instructions are valid at time of writing for the various systems I've run this code on. Note that in all 
cases I tell the package manager to give me Python 3, but I don't specify which minor version. The minor version 
represented by that package may change the package for setuptools on FreeBSD (step 2) and the filenames for 
easy_install on FreeBSD (step 3) and Fedora (step 3).

### OS X

1. Install [Homebrew](http://brew.sh)
2. Install Python 3, `brew install python3`
3. Install libraries, `pip3 install python-simple-hipchat bottle simplejson`

### FreeBSD

(Based on FreeBSD 10)

1. Install Python 3, `pkg install python3`
2. Install setuptools, `pkg install py33-setuptools33`
3. Install pip, `easy_install-3.3 pip`
4. Install libraries, `pip3 install python-simple-hipchat bottle simplejson`

### Fedora

(Based on Fedora 20. Version of easy_install may change)

1. Install Python 3, `yum install python3`
2. Install setuptools, `yum install python3-setuptools`
3. Install pip, `easy_install-3.3 pip`
4. Install libraries, `pip-python3 install python-simple-hipchat bottle simplejson`

### Debian

(Based on Debian 7. Version of easy_install may change)

1. Install Python 3, `apt-get install python3`
2. Install setuptools, `apt-get install python3-setuptools`
3. Install pip, `easy_install-3 pip`
4. Install libraries, `pip3 install python-simple-hipchat bottle simplejson`



## Installation

There is no installation. Simply install the prerequisites, clone this repository somewhere, set up *config.ini*, and 
run *hipstudio.py*.

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
