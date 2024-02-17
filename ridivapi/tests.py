from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from .models import Invoice, InvoiceDetail
from datetime import datetime
import json


class InvoiceAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.invoice = Invoice.objects.create(customer="Test Customer", date=datetime.strptime("2024-02-17T15:30:00.123456", "%Y-%m-%dT%H:%M:%S.%f"))
        self.invoiceDetails1 = InvoiceDetail.objects.create(description="Test Invoice 1", quantity=1, unit_price=100, price=100, invoice=self.invoice)
        self.invoiceDetails2 = InvoiceDetail.objects.create(description="Test Invoice 2", quantity=3, unit_price=50, price=150, invoice=self.invoice)
    
    def test_getInvoice(self):
        url = reverse('invoice_fn', args=[self.invoice.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_putInvoice(self):
        url = reverse('invoice_fn', args=[self.invoice.id])
        data = {
            "description": "Test Invoice 2",
            "quantity": 2,
            "unit_price": 20.0,
            "price": 40.0
        }
        data = json.dumps(data)
        response = self.client.put(url, data, content_type='application/json')
        self.assertEqual(response.status_code, 204)
    
    def test_postInvoice(self):
        url = reverse('invoice_post')
        data = {
            "customer": "Pranav P",
            "date": "2024-02-17T15:30:00.123456",
            "description": "Test POST Invoice",
            "quantity": 2,
            "unit_price": 200,
            "price": 400
        }
        data = json.dumps(data)
        response = self.client.post(url, data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
    
    def test_deleteInvoice(self):
        url = reverse('invoice_fn', args=[self.invoice.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)