#!/usr/bin/python3
from models.basemodel import BaseModel
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship
'''
Implementation of the Employee model.
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
    sales = relationship('Sale', backref='employee', lazy=True)

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
