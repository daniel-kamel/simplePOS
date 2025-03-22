#!/usr/bin/env python3
from models import Product, Sale, session
from flask import Blueprint, render_template, request, redirect, url_for
'''
Employee view for the SimplePOS application
'''
# Create the employee blueprint
employee = Blueprint('employee', __name__)

# List to hold product data in the cart
# Format: [{'product': product, 'quantity': quantity, 'total': total}]
CART = []


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
    products_list = session.query(Product).all()
    total = sum(product['total'] for product in CART) if CART else 0
    return render_template('new_sale.html', products_list=products_list, cart=CART, total=total)


@employee.route('/sale/add-product', methods=['POST'])
def add_product():
    '''
    Add a product to the cart
    '''
    product_name = request.form.get('product_name')
    product = Product.get_product(product_name)
    quantity = int(request.form.get('quantity'))
    new_product = {
        'product': product,
        'quantity': quantity,
        'total': product.price * quantity
    }
    CART.append(new_product)
    return redirect(url_for('employee.new_sale'))

@employee.route('/sale/<int:product_id>/delete', methods=['POST', 'GET'])
def delete_product(product_id):
    '''
    Delete a product from the cart
    '''
    for product in CART:
        if product['product'].id == product_id:
            CART.remove(product)
    return redirect(url_for('employee.new_sale'))

@employee.route('/sale/save', methods=['POST', 'GET'])
def save_sale():
    '''
    Save a sale
    '''
    product_data = {}
    for product in CART:
        product_data[product['product']] = product['quantity']
    sale = Sale(1, product_data)
    sale.save()
    CART.clear()
    return redirect(url_for('employee.new_sale'))
