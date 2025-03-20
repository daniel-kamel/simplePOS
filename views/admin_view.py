#!/usr/bin/env python3
from flask import Blueprint, render_template
'''
Admin view for the SimplePOS application
'''
# Create the admin blueprint
admin = Blueprint('admin', __name__)


@admin.route('/dashboard')
def dashboard():
    '''
    Render admin template for /admin/dashboard route
    '''
    return render_template('admin_dashboard.html', admin=True)
