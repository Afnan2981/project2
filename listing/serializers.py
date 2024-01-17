from rest_framework import serializers
from .models import Listing

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'

    def to_representation(self, instance):
        ret = super().to_representation(instance)

        # Check if the user is an admin or the realtor of the listing
        user = self.context['request'].user
        if user.is_authenticated and (user.is_admin or user.email == instance.realtor):
            # Include the "status" field for admins and the listing's realtor
            ret['status'] = instance.get_status_display()

            # Include the new property features
            ret['bathtub'] = instance.bathtub
            ret['hairdryer'] = instance.hairdryer
            ret['shampoo'] = instance.shampoo
            ret['hot_water'] = instance.hot_water
            ret['washing_machine'] = instance.washing_machine
            ret['towels_sheets_soap_toilet_paper'] = instance.towels_sheets_soap_toilet_paper
            ret['hangers'] = instance.hangers
            ret['extra_pillows_blankets'] = instance.extra_pillows_blankets
            ret['blinds'] = instance.blinds
            ret['iron'] = instance.iron
            ret['baby_crib'] = instance.baby_crib
            ret['changing_table'] = instance.changing_table
            ret['babysitter_recommendations'] = instance.babysitter_recommendations
            ret['heating'] = instance.heating
            ret['air_conditioning'] = instance.air_conditioning
            ret['lock_on_bedroom_door'] = instance.lock_on_bedroom_door
            ret['exterior_common_area_surveillance_cameras'] = instance.exterior_common_area_surveillance_cameras
            ret['smoke_detector'] = instance.smoke_detector
            ret['carbon_monoxide_detector'] = instance.carbon_monoxide_detector
            ret['fire_extinguisher'] = instance.fire_extinguisher
            ret['wifi'] = instance.wifi
            ret['dedicated_workspace'] = instance.dedicated_workspace
            ret['kitchen'] = instance.kitchen
            ret['space_for_guests_to_cook'] = instance.space_for_guests_to_cook
            ret['refrigerator'] = instance.refrigerator
            ret['microwave'] = instance.microwave
            ret['basic_kitchen_equipment'] = instance.basic_kitchen_equipment
            ret['dishware_cutlery'] = instance.dishware_cutlery
            ret['bowls_chopsticks_plates_cups_etc'] = instance.bowls_chopsticks_plates_cups_etc
            ret['stove'] = instance.stove
            ret['oven'] = instance.oven
            ret['coffee_maker'] = instance.coffee_maker
            ret['private_patio_balcony'] = instance.private_patio_balcony
            ret['beach_essentials'] = instance.beach_essentials
            ret['paid_parking_outside_property'] = instance.paid_parking_outside_property
            ret['allowed_luggage_storage'] = instance.allowed_luggage_storage
            ret['long_term_stays_allowed'] = instance.long_term_stays_allowed
            ret['keys_handed_over_by_host'] = instance.keys_handed_over_by_host
            ret['television'] = instance.television
            ret['dryer'] = instance.dryer
            ret['air_conditioning'] = instance.air_conditioning

        return ret
