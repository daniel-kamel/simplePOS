#!/usr/bin/python3
from models.basemodel import BaseModel
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


class product_sale(BaseModel):
    __tablename__ = 'product_sales'
    product_id = Column(Integer, ForeignKey('products.id'), primary_key=True)
    sale_id = Column(Integer, ForeignKey('sales.id'), primary_key=True)

class Product(BaseModel):
    '''
    Implementation of the Product model.
    '''
    __tablename__ = 'products'
    name = Column(String(128), nullable=False)
    price = Column(Integer, nullable=False)
    sales = relationship('Sale', back_populates='product', secondary=product_sale, lazy=True)


class Sale(BaseModel):
    '''
    Implementation of the Sale model.
    '''
    __tablename__ = 'sales'
    employee_id = Column(Integer, ForeignKey('employees.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    employee = relationship('Employee', back_populates='sales', lazy=True)
    products = relationship('Product', back_populates='sales', secondary=product_sale, lazy=True)
