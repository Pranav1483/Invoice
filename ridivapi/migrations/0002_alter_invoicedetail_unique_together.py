# Generated by Django 5.0.2 on 2024-02-17 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ridivapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='invoicedetail',
            unique_together=set(),
        ),
    ]