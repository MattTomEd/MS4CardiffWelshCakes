from django.test import TestCase
from django.urls import reverse
from django.http import HttpRequest
from django.contrib.auth.models import User

from .models import Category, Product


class ProductTests(TestCase):

    def setUp(self):
        """ Create a test category and product """
        self.category = Category.objects.create(
            name = "test",
            friendly_name = "Friendly test",
        )

        self.product = Product.objects.create(
            category = Category.objects.get(id=1),
            sku = "99999",
            name = "Test name",
            description = "Test description",
            price = "10.00",
            rating = "4.00",
        )

    def test_product(self):
        """ Test product returns with correct info """
        product = Product.objects.get(id=1)
        expected_name = f'{product.name}'
        expected_description = f'{product.description}'
        expected_price = f'{product.price}'
        expected_rating = f'{product.rating}'
        self.assertEquals(expected_name, 'Test name')
        self.assertEquals(expected_description, 'Test description')
        self.assertEquals(expected_price, '10.00')
        self.assertEquals(expected_rating, '4.00')

    def test_category(self):
        """ Test category returns with correct info """
        category = Category.objects.get(id=1)
        expected_name = f'{category.name}'
        expected_friendlyname = f'{category.friendly_name}'
        self.assertEquals(expected_name, 'test')
        self.assertEquals(expected_friendlyname, 'Friendly test')

    