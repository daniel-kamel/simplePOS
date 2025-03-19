#!/usr/bin/python3
import unittest
from models.models import Employee, Product, Sale, ProductSale
from models.basemodel import session


class TestModels(unittest.TestCase):
    '''
    Test cases for the models classes.
    '''
    @classmethod
    def setUpClass(cls):
        '''
        Set up the test class.
        '''
        cls.employee_1 = Employee(
            name='Employee1', salary=5000, comission=True, commision_rate=10)
        cls.employee_1.save()
        cls.employee_2 = Employee(
            name='Employee2', salary=1000, comission=True, commision_rate=50)
        cls.employee_1.save()
        cls.product_1 = Product(name='Product1', price=100)
        cls.product_1.save()
        cls.product_2 = Product(name='Product2', price=200)
        cls.product_2.save()
        cls.sale_1 = Sale(
            employee=cls.employee_1, product_data={cls.product_1:2})
        cls.sale_1.save()
        cls.sale_2 = Sale(
            employee=cls.employee_2, product_data={cls.product_1:1, cls.product_2:2})
        cls.sale_2.save()
        cls.sale_3 = Sale(
            employee=cls.employee_1, product_data={cls.product_2:1})
        cls.sale_3.save()

    def test_employee_calculate_commission(self):
        '''
        Test the calculate_commission method of the Employee class.
        '''
        self.assertEqual(self.employee_1.calculate_commission(), 400)
        self.assertEqual(self.employee_2.calculate_commission(), 500)

    def test_employee_calculate_earnings(self):
        '''
        Test the calculate_earnings method of the Employee class.
        '''
        self.assertEqual(self.employee_1.calculate_earnings(), 5400)
        self.assertEqual(self.employee_2.calculate_earnings(), 1500)

    def test_product_sale(self):
        '''
        Test the ProductSale class.
        '''
        sale_1_product_sale = session.query(ProductSale).filter_by(sale_id=self.sale_1.id).all()
        self.assertEqual(len(sale_1_product_sale), 1)
        self.assertEqual(sale_1_product_sale[0].product_id, self.product_1.id)
        self.assertEqual(sale_1_product_sale[0].quantity, 2)

    def test_product(self):
        '''
        Test the Product class.
        '''
        product_1 = Product.get_product(self.product_1.name)
        self.assertEqual(product_1.name, self.product_1.name)
        self.assertEqual(product_1.price, self.product_1.price)
        self.assertEqual(product_1.sales, [self.sale_1, self.sale_2])

    def test_sale(self):
        '''
        Test the Sale class.
        '''
        self.assertEqual(self.sale_1.total, 200)
        self.assertEqual(self.sale_2.total, 500)
        self.assertEqual(self.sale_3.total, 200)
        self.assertEqual(self.sale_1.employee, self.employee_1)
        self.assertEqual(self.sale_2.employee, self.employee_2)
        self.assertEqual(self.sale_3.employee, self.employee_1)
        self.assertEqual(self.sale_1.products, [self.product_1])
        self.assertEqual(self.sale_2.products, [self.product_1, self.product_2])
        self.assertEqual(self.sale_3.products, [self.product_2])

    def test_sale_employee_commission(self):
        '''
        Test the employee_commission method of the Sale class.
        '''
        self.assertEqual(self.sale_1.employee_commission(), 20)
        self.assertEqual(self.sale_2.employee_commission(), 250)
        self.assertEqual(self.sale_3.employee_commission(), 20)

    def tearDownClass(cls):
        '''
        Clean up the test class.
        '''
        cls.employee_1.delete()
        cls.employee_2.delete()
        cls.product_1.delete()
        cls.product_2.delete()
        cls.sale_1.delete()
        cls.sale_2.delete()
