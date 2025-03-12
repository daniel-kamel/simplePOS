#!/usr/bin/env python
from flask import Flask
'''
Main file for the SimplePOS application
'''
# Create the Flask application
app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)
