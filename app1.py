# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 23:00:38 2021

@author: ASHISH
"""
from flask import Flask



app =Flask(__name__)

@app.route('/hi')
def hello():
    return "Hello"

if __name__ == "__main__":
    app.run()