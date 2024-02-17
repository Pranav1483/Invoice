from django.urls import path
from . import views

urlpatterns = [
    path('', views.status, name='status'),
    path('invoices/<int:id>', views.invoice_fn, name='invoice_fn'),
    path('invoices/', views.invoice_post, name='invoice_post'),
]