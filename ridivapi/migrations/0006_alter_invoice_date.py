# Generated by Django 5.0.2 on 2024-02-17 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ridivapi', '0005_alter_invoice_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='date',
            field=models.DateTimeField(),
        ),
    ]