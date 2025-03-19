#!/usr/bin/python3
import unittest
from models.basemodel import BaseModel, Base, session
from datetime import datetime
'''
Unit tests for the BaseModel class.
'''


class TestBaseModel(unittest.TestCase):
    '''
    Test cases for the BaseModel class.
    '''
    @classmethod
    def setUpClass(cls):
        '''
        Set up the test class.
        '''
        cls.model = BaseModel()
        cls.model.save()

    def test_save(self):
        '''
        Test the save method of the BaseModel class.
        '''
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)
        self.assertIsInstance(self.model.id, int)
        self.assertTrue(issubclass(BaseModel, Base))

    def test_get(self):
        '''
        Test the get method of the BaseModel class.
        '''
        self.assertIs(self.model, self.model.get(self.model.id))

    def test_delete(self):
        '''
        Test the delete method of the BaseModel class.
        '''
        self.model.delete()
        self.assertIsNone(self.model)
