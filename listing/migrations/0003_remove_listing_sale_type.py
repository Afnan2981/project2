# Generated by Django 5.0 on 2024-01-03 23:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0002_listing_is_approved_listing_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='sale_type',
        ),
    ]