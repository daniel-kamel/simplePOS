#!/usr/bin/python3
from models.basemodel import BaseModel, session
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
'''
Implementation of models of simplePOS system.
'''


class Employee(BaseModel):
    '''
    Employee model.
    '''
    __tablename__ = 'employees'
    name = Column(String(128), nullable=False)
    admin = Column(Boolean, nullable=False, default=False)
    salary = Column(Integer, nullable=False)
    commission = Column(Boolean, nullable=False, default=False)
    commision_rate = Column(Integer)
    sales = relationship('Sale', back_populates='employee', lazy=True)

    def calculate_commission(self):
        '''
        Calculate the commission for the employee.
        '''
        total_sales = sum(sale.total for sale in self.sales)
        commission = total_sales * (self.commision_rate / 100)
        return commission

    def calculate_earnings(self):
        '''
        Calculate the total earnings for the employee.
        '''
        total_earnings = self.salary + self.calculate_commission()
        return total_earnings

    def __repr__(self):
        '''
        Return a string representation of the Employee object.
        '''
        return f'<Employee[{self.id}] {self.name}>'


class ProductSale(BaseModel):
    __tablename__ = 'product_sales'
    product_id = Column(Integer, ForeignKey('products.id'))
    sale_id = Column(Integer, ForeignKey('sales.id'))
    quantity = Column(Integer, nullable=False, default=1)

class Product(BaseModel):
    '''
    Implementation of the Product model.
    '''
    __tablename__ = 'products'
    name = Column(String(128), nullable=False)
    price = Column(Integer, nullable=False)
    sales = relationship('Sale', back_populates='products', secondary='product_sales', lazy=True)

    def __init__(self, name, price):
        '''
        Initialize a Product object.
        '''
        self.name = name.title()
        self.price = price

    def get_product(self, name):
        '''
        Get a product by name.
        '''
        product = self.query.filter_by(name=name.title()).first()
        return product

    def __repr__(self):
        '''
        Return a string representation of the Product object.
        '''
        return f'<Product[{self.id}] {self.name}>'


class Sale(BaseModel):
    '''
    Implementation of the Sale model.
    '''
    __tablename__ = 'sales'
    employee_id = Column(Integer, ForeignKey('employees.id'), nullable=False)
    total = Column(Integer, nullable=False, default=0)
    employee = relationship('Employee', back_populates='sales', lazy=True)
    products = relationship('Product', back_populates='sales', secondary='product_sales', lazy=True)

    def __init__(self, employee_id, product_data):
        '''
        Initialize a Sale object.
        '''
        self.employee_id = employee_id
        self.total = 0
        session.add(self)
        session.flush()
        if product_data is not None:
            for product, quantity in product_data.items():
                product_sale = ProductSale(product_id=product.id, sale_id=self.id, quantity=quantity)
                session.add(product_sale)
                session.flush()
                self.total += product.price * quantity

    def __repr__(self):
        '''
        Return a string representation of the Sale object.
        '''
        return f'<Sale[{self.id}] seller: {self.employee.name}>'
