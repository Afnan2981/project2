# Generated by Django 5.0 on 2024-01-04 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0003_remove_listing_sale_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='photo_10',
            field=models.ImageField(blank=True, null=True, upload_to='listings/'),
        ),
        migrations.AddField(
            model_name='listing',
            name='photo_4',
            field=models.ImageField(blank=True, null=True, upload_to='listings/'),
        ),
        migrations.AddField(
            model_name='listing',
            name='photo_5',
            field=models.ImageField(blank=True, null=True, upload_to='listings/'),
        ),
        migrations.AddField(
            model_name='listing',
            name='photo_6',
            field=models.ImageField(blank=True, null=True, upload_to='listings/'),
        ),
        migrations.AddField(
            model_name='listing',
            name='photo_7',
            field=models.ImageField(blank=True, null=True, upload_to='listings/'),
        ),
        migrations.AddField(
            model_name='listing',
            name='photo_8',
            field=models.ImageField(blank=True, null=True, upload_to='listings/'),
        ),
        migrations.AddField(
            model_name='listing',
            name='photo_9',
            field=models.ImageField(blank=True, null=True, upload_to='listings/'),
        ),
    ]
