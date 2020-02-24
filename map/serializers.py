# from django.contrib.auth.models import GPS
from .models import GPS
from rest_framework import serializers


class GPSSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GPS
        fields = ['created_at','lat','long','updated_at']
