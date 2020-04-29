from rest_framework import serializers
from django_countries.serializers import CountryFieldMixin
from django_countries.serializer_fields import CountryField

from core.models import Address


class AddressSerializer(CountryFieldMixin, serializers.ModelSerializer):
    
    user = serializers.StringRelatedField(read_only=True)
    date_added = serializers.SerializerMethodField(read_only=True)
    country = CountryField( country_dict=True)

    class Meta:
        model = Address
        exclude = ("date_updated",)

    def get_date_added(self, instance):
        return instance.date_added.strftime("%B %d, %Y")

