#!/usr/bin/python3
from models.basemodel import BaseModel
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
'''
Implementation of the Product model.
'''


class Product(BaseModel):
    '''
    Implementation of the Product model.
    '''
    __tablename__ = 'products'
    name = Column(String(128), nullable=False)
    price = Column(Integer, nullable=False)
    sales = relationship('Sale', backref='product', lazy=True)
