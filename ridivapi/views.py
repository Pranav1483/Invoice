import json
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from .models import *
from .serializers import *
from datetime import datetime

@api_view(['GET'])
def status(request):
    return HttpResponse(status=200)

@api_view(['GET', 'PUT', 'DELETE'])
def invoice_fn(request, id):
    if request.method == 'GET':
        invoice_filter = Invoice.objects.filter(id=id)
        if not invoice_filter.exists():
            return HttpResponse(status=404)
        else: 
            invoice_object = invoice_filter.first()
            invoice = InvoiceSerializer(invoice_object).data
            invoice['invoiceDetails'] = []
            invoiceDetail_filter = InvoiceDetail.objects.filter(invoice=invoice_object)
            for obj in invoiceDetail_filter:
                invoice['invoiceDetails'].append(InvoiceDetailSerializer(obj).data)
            return JsonResponse(invoice, status=200)
    elif request.method == 'PUT':
        invoice_filter = Invoice.objects.filter(id=id)
        if not invoice_filter.exists():
            return HttpResponse(status=404)
        else: 
            invoice_object = invoice_filter.first()
            try:
                data = json.loads(request.body.decode('utf-8'))
                invoiceDetail_filter = InvoiceDetail.objects.filter(invoice=invoice_object, description=data['description'])
                if not invoiceDetail_filter.exists():
                    return HttpResponse(status=404)
                else:
                    invoiceDetail_object = invoiceDetail_filter.first()
                    invoiceDetail_object.quantity = data.get('quantity', invoiceDetail_object.quantity)
                    invoiceDetail_object.unit_price = data.get('unit_price', invoiceDetail_object.unit_price)
                    invoiceDetail_object.price = data.get('price', invoiceDetail_object.price)
                    invoiceDetail_object.save()
                    return HttpResponse(status=204)
            except Exception as e:
                return HttpResponse(e, status=400)
    elif request.method == 'DELETE':
        invoice_filter = Invoice.objects.filter(id=id)
        if not invoice_filter.exists():
            return HttpResponse(status=404)
        else: 
            invoice_object = invoice_filter.first()
            invoice_object.delete()
            return HttpResponse(status=204)

@api_view(['POST'])
def invoice_post(request):
    try:
        invoiceDetail_object = InvoiceDetail()
        data = json.loads(request.body.decode('utf-8'))
        data['date'] = datetime.strptime(data['date'], "%Y-%m-%dT%H:%M:%S.%f")
        invoice_object, created = Invoice.objects.get_or_create(date=data['date'], customer=data['customer'])
        if created:
            invoice_object.save()
        invoiceDetail_object.invoice = invoice_object
        invoiceDetail_object.description = data['description']
        invoiceDetail_object.quantity = data['quantity']
        invoiceDetail_object.unit_price = data['unit_price']
        invoiceDetail_object.price = data['price']
        invoiceDetail_object.save()
        invoiceDetail = InvoiceDetailSerializer(invoiceDetail_object).data
        invoiceDetail['invoice'] = InvoiceSerializer(invoice_object).data
        return JsonResponse(invoiceDetail, status=200)
    except Exception as e:
        return HttpResponse(e, status=400)