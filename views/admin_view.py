#!/usr/bin/env python3
from flask import Blueprint, render_template, request, redirect, url_for
from models.basemodel import session
from models.models import Employee, Product, Sale, ProductSale
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
    # Get the top employee
    employees_sales = {}
    employees = session.query(Employee).all()
    for employee in employees:
        total_sales = sum(sale.total for sale in employee.sales)
        employees_sales[total_sales] = employee
    max_sales = max(employees_sales.keys())
    top_employee = employees_sales[max_sales].name
    # Get the top product
    product_sales = {}
    for product in session.query(Product).all():
        product_totals = session.query(ProductSale).filter(ProductSale.product_id == product.id).all()
        total_sales = sum(product_total.quantity for product_total in product_totals)
        product_sales[total_sales] = product
    max_sales = max(product_sales.keys())
    top_product = product_sales[max_sales].name
    # Get the top sale
    sales = session.query(Sale).all()
    top_sale = max(sale.total for sale in sales)
    return render_template('admin_dashboard.html', admin=True, top_employee=top_employee, top_product=top_product, top_sale=top_sale)

@admin.route('/employees')
def employees():
    '''
    Render admin template for /admin/employees route
    '''
    employees = session.query(Employee).all()
    return render_template('admin_employees.html', admin=True, employees=employees)

@admin.route('/employees/new', methods=['GET', 'POST'])
def new_employee():
    '''
    Render admin template for /admin/employees/new route
    '''
    if request.method == 'POST':
        name = request.form.get('name')
        salary = request.form.get('salary')
        commission = request.form.get('commission') == 'on'
        commission_rate = request.form.get('commission_rate')
        admin = request.form.get('admin') == 'on'
        employee = Employee(name=name, salary=salary, commission=commission, commission_rate=commission_rate, admin=admin)
        employee.save()
        return redirect(url_for('admin.employees'))
    else:
        return render_template('admin_new_employee.html', admin=True)

@admin.route('/employees/<int:employee_id>/delete', methods=['POST', 'GET'])
def delete_employee(employee_id):
    '''
    Delete an employee
    '''
    employee = session.query(Employee).get(employee_id)
    employee.delete()
    return redirect(url_for('admin.employees'))

@admin.route('/products')
def products():
    '''
    Render admin template for /admin/products route
    '''
    products = session.query(Product).all()
    return render_template('admin_products.html', admin=True, products=products)

@admin.route('/products/new', methods=['GET', 'POST'])
def new_product():
    '''
    Render admin template for /admin/products/new route
    '''
    if request.method == 'POST':
        name = request.form.get('name')
        price = request.form.get('price')
        product = Product(name=name, price=price)
        product.save()
        return redirect(url_for('admin.products'))
    else:
        return render_template('admin_new_product.html', admin=True)

@admin.route('/products/<int:product_id>/delete', methods=['POST', 'GET'])
def delete_product(product_id):
    '''
    Delete a product
    '''
    product = session.query(Product).get(product_id)
    product.delete()
    return redirect(url_for('admin.products'))
