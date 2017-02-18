#!/bin/env python

from bottle import route, run, response
from cowsay import *
from os import getpid, getlogin, getuid, getgid, getcwd
from socket import getfqdn


@route('/')
def root():
    response.content_type = 'text/plain'
    text = 'Hello, This is {}, \
            I\'m running as {}, \
            my PID is {:d}, \
            my UID/GID is {:d}/{:d}, \
            I\'m operating from {}'.format(
        getfqdn(),
        getlogin(),
        getpid(),
        getuid(),
        getgid(),
        getcwd()
    )

    return '\n'.join(cowsay(text, max_width=30))

run(host='localhost', port=8080, debug=True)
