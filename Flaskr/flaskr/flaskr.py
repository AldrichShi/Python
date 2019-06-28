# -*- coding: utf-8 -*-
# flaskr.py
# @author King
# @description
# @created 2019-06-28T14:10:30.608Z+08:00
# @last-modified 2019-06-28T14:41:14.866Z+08:00
#

from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return 'hello world!'