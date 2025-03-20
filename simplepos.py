#!/usr/bin/env python3
from flask import Flask, render_template
from views.admin_view import admin
from views.employee_view import employee
'''
Main file for the SimplePOS application
'''
# Create the Flask application
app = Flask(__name__)

# Register blueprints
app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(employee, url_prefix='/employee')

@app.route('/')
def index():
    '''
    Render home template for / route
    '''
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
