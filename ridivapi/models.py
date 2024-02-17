from django.db import models
from django.core.exceptions import ValidationError


def non_negative_validator(value):
    if value < 0:
        raise ValidationError("Value must be non-negative")

class Invoice(models.Model):
    date = models.DateTimeField()
    customer = models.CharField(max_length=32)

    class Meta:
        unique_together = ('date', 'customer')

class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(to=Invoice, on_delete=models.CASCADE)
    description = models.CharField(max_length=256)
    quantity = models.PositiveIntegerField()
    unit_price = models.FloatField(validators=[non_negative_validator])
    price = models.FloatField(validators=[non_negative_validator])

    class Meta:
        unique_together = ('description', 'invoice')