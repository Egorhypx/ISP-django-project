from urllib import response
from django.test import TestCase
from django.urls import reverse
from .models import Customer
from insurance.models import Category
import json

class TestCustomerViews(TestCase):

    def test_sign_in_page(self):
        response = self.client.get('/sign_in/')
        self.assertEqual(response.status_code, 200)

    def test_registration_page(self):
        response = self.client.get('/registration/')
        self.assertEqual(response.status_code, 200)

    def test_profile_page(self):
        customers = Customer.objects.all()

        for customer in customers:
            response = self.client.get(f'/customer_profile/{customer.pk}/')
            self.assertEqual(response.status_code, 200)

    def test_home_page(self):
        response = self.client.get('/home/')
        self.assertEqual(response.status_code, 200)