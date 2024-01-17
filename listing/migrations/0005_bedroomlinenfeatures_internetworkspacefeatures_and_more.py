# Generated by Django 5.0 on 2024-01-04 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0004_listing_photo_10_listing_photo_4_listing_photo_5_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BedroomLinenFeatures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('washing_machine', models.BooleanField(default=False)),
                ('basic_amenities', models.BooleanField(default=False)),
                ('hangers', models.BooleanField(default=False)),
                ('extra_pillows_blankets', models.BooleanField(default=False)),
                ('blinds', models.BooleanField(default=False)),
                ('iron', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='InternetWorkspaceFeatures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wifi', models.BooleanField(default=False)),
                ('dedicated_workspace', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='KitchenDiningFeatures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kitchen', models.BooleanField(default=False)),
                ('space_for_guests_to_cook', models.BooleanField(default=False)),
                ('refrigerator', models.BooleanField(default=False)),
                ('microwave', models.BooleanField(default=False)),
                ('basic_kitchen_equipment', models.BooleanField(default=False)),
                ('dishware_cutlery', models.BooleanField(default=False)),
                ('stove', models.BooleanField(default=False)),
                ('oven', models.BooleanField(default=False)),
                ('coffee_maker', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='OutdoorFeatures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('private_patio_balcony', models.BooleanField(default=False)),
                ('beach_essentials', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ParkingFacilitiesFeatures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid_parking_outside', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PrivacySecurityFeatures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lock_on_bedroom_door', models.BooleanField(default=False)),
                ('surveillance_cameras', models.BooleanField(default=False)),
                ('smoke_detector', models.BooleanField(default=False)),
                ('carbon_monoxide_detector', models.BooleanField(default=False)),
                ('fire_extinguisher', models.BooleanField(default=False)),
                ('first_aid_kit', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ServicesFeatures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allowed_luggage_storage', models.BooleanField(default=False)),
                ('long_term_stays_allowed', models.BooleanField(default=False)),
                ('keys_handed_over_by_host', models.BooleanField(default=False)),
                ('television', models.BooleanField(default=False)),
                ('dryer', models.BooleanField(default=False)),
                ('air_conditioning', models.BooleanField(default=False)),
            ],
        ),
    ]