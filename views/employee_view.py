#!/usr/bin/env python3
from flask import Blueprint, render_template
'''
Employee view for the SimplePOS application
'''
# Create the employee blueprint
employee = Blueprint('employee', __name__)


@employee.route('/')
def index():
    '''
    Render employee template for /employee route
    '''
    return render_template('employee_home.html')


@employee.route('/new-sale')
def new_sale():
    '''
    Render employee template for /employee/new_sale route
    '''
    return render_template('new_sale.html')
