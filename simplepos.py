#!/usr/bin/env python3
from flask import Flask
from views.admin_view import admin
'''
Main file for the SimplePOS application
'''
# Create the Flask application
app = Flask(__name__)

# Register blueprints
app.register_blueprint(admin, url_prefix='/admin')

if __name__ == '__main__':
    app.run(debug=True)
