from django.conf import settings
from django.db import models
from django.utils.timezone import now




class BedroomLinenFeatures(models.Model):
    washing_machine = models.BooleanField(default=False)
    basic_amenities = models.BooleanField(default=False)
    hangers = models.BooleanField(default=False)
    extra_pillows_blankets = models.BooleanField(default=False)
    blinds = models.BooleanField(default=False)
    iron = models.BooleanField(default=False)

class PrivacySecurityFeatures(models.Model):
    lock_on_bedroom_door = models.BooleanField(default=False)
    surveillance_cameras = models.BooleanField(default=False)
    smoke_detector = models.BooleanField(default=False)
    carbon_monoxide_detector = models.BooleanField(default=False)
    fire_extinguisher = models.BooleanField(default=False)
    first_aid_kit = models.BooleanField(default=False)

class InternetWorkspaceFeatures(models.Model):
    wifi = models.BooleanField(default=False)
    dedicated_workspace = models.BooleanField(default=False)

class KitchenDiningFeatures(models.Model):
    kitchen = models.BooleanField(default=False)
    space_for_guests_to_cook = models.BooleanField(default=False)
    refrigerator = models.BooleanField(default=False)
    microwave = models.BooleanField(default=False)
    basic_kitchen_equipment = models.BooleanField(default=False)
    dishware_cutlery = models.BooleanField(default=False)
    stove = models.BooleanField(default=False)
    oven = models.BooleanField(default=False)
    coffee_maker = models.BooleanField(default=False)

class OutdoorFeatures(models.Model):
    private_patio_balcony = models.BooleanField(default=False)
    beach_essentials = models.BooleanField(default=False)

class ParkingFacilitiesFeatures(models.Model):
    paid_parking_outside = models.BooleanField(default=False)

class ServicesFeatures(models.Model):
    allowed_luggage_storage = models.BooleanField(default=False)
    long_term_stays_allowed = models.BooleanField(default=False)
    keys_handed_over_by_host = models.BooleanField(default=False)
    television = models.BooleanField(default=False)
    dryer = models.BooleanField(default=False)
    air_conditioning = models.BooleanField(default=False)


class Listing(models.Model):
    class SaleType(models.TextChoices):
        FOR_SALE = 'For Sale'
        FOR_RENT = 'For Rent'

    class HomeType(models.TextChoices):
        HOUSE = 'House'
        CONDO = 'Condo'
        TOWNHOUSE = 'Townhouse'

    class Status(models.TextChoices):
        PENDING = 'Pending', 'Pending'
        APPROVED = 'Approved', 'Approved'
        REJECTED = 'Rejected', 'Rejected'

    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    realtor = models.EmailField(max_length=255)
    is_approved = models.BooleanField(default=False)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=20)
    description = models.TextField()
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)

    home_type = models.CharField(max_length=10, choices=HomeType.choices, default=HomeType.HOUSE)
    main_photo = models.ImageField(upload_to='listings/')
    photo_1 = models.ImageField(upload_to='listings/')
    photo_2 = models.ImageField(upload_to='listings/')
    photo_3 = models.ImageField(upload_to='listings/')
    photo_4 = models.ImageField(upload_to='listings/', blank=True, null=True)
    photo_5 = models.ImageField(upload_to='listings/', blank=True, null=True)
    photo_6 = models.ImageField(upload_to='listings/', blank=True, null=True)
    photo_7 = models.ImageField(upload_to='listings/', blank=True, null=True)
    photo_8 = models.ImageField(upload_to='listings/', blank=True, null=True)
    photo_9 = models.ImageField(upload_to='listings/', blank=True, null=True)
    photo_10 = models.ImageField(upload_to='listings/', blank=True, null=True)
    is_published = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=now)
        # Property Features
    bathtub = models.BooleanField(default=False)
    hairdryer = models.BooleanField(default=False)
    washing_machine = models.BooleanField(default=False)
    hangers = models.BooleanField(default=False)
    extra_pillows_blankets = models.BooleanField(default=False)
    blinds = models.BooleanField(default=False)
    iron = models.BooleanField(default=False)

    # Bathroom
    hot_water = models.BooleanField(default=False)
    shampoo = models.BooleanField(default=False)

    # Family
    baby_crib = models.BooleanField(default=False)
    changing_table = models.BooleanField(default=False)
    babysitter_recommendations = models.BooleanField(default=False)

    # Heating and Cooling
    heating = models.BooleanField(default=False)
    air_conditioning = models.BooleanField(default=False)

    # Privacy and Security
    lock_on_bedroom_door = models.BooleanField(default=False)
    exterior_common_area_surveillance_cameras = models.BooleanField(default=False)
    smoke_detector = models.BooleanField(default=False)
    carbon_monoxide_detector = models.BooleanField(default=False)
    fire_extinguisher = models.BooleanField(default=False)
    first_aid_kit = models.BooleanField(default=False)

    # Internet and Workspace
    wifi = models.BooleanField(default=False)
    dedicated_workspace = models.BooleanField(default=False)

    # Kitchen and Dining
    kitchen = models.BooleanField(default=False)
    space_for_guests_to_cook = models.BooleanField(default=False)
    refrigerator = models.BooleanField(default=False)
    microwave = models.BooleanField(default=False)
    basic_kitchen_equipment = models.BooleanField(default=False)
    dishware_cutlery = models.BooleanField(default=False)
    stove = models.BooleanField(default=False)
    oven = models.BooleanField(default=False)
    coffee_maker = models.BooleanField(default=False)

    # Outdoor
    private_patio_balcony = models.BooleanField(default=False)
    beach_essentials = models.BooleanField(default=False)

    # Parking and Facilities
    paid_parking_outside_property = models.BooleanField(default=False)

    # Services
    allowed_luggage_storage = models.BooleanField(default=False)
    long_term_stays_allowed = models.BooleanField(default=False)
    keys_handed_over_by_host = models.BooleanField(default=False)
    television = models.BooleanField(default=False)
    dryer = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def delete(self):
        self.main_photo.storage.delete(self.main_photo.name)
        self.photo_1.storage.delete(self.photo_1.name)
        self.photo_2.storage.delete(self.photo_2.name)
        self.photo_3.storage.delete(self.photo_3.name)
        self.photo_4.storage.delete(self.photo_4.name)
        self.photo_5.storage.delete(self.photo_5.name)
        self.photo_6.storage.delete(self.photo_6.name)
        self.photo_7.storage.delete(self.photo_7.name)
        self.photo_8.storage.delete(self.photo_8.name)
        self.photo_9.storage.delete(self.photo_9.name)
        self.photo_10.storage.delete(self.photo_10.name)

        super().delete()

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
         return self.text