#-*- coding: utf-8 -*-
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route

@route('/')
def hello_world():
    return 'oiiii'

application = default_app()

