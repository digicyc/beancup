from rest_framework import serializers

from beanbrew.models import Brew


class BrewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brew
        fields = (
            'creator', 'bean', 'ground_option', 'ground_level', 'scoops',
            'water_bottles', 'description', 'date_added',
        )


