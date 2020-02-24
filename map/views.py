from django.shortcuts import render
from django.http import HttpResponse

# from django.contrib.auth.models import GPS
from .models import GPS
from rest_framework import viewsets
from .serializers import GPSSerializer


def index(request):

    lat = GPS.objects.latest('created_at').lat
    long = GPS.objects.latest('created_at').long
    created = GPS.objects.latest('created_at').created_at.strftime('%Y-%m-%d')
    updated = GPS.objects.latest('created_at').updated_at.strftime('%Y-%m-%d')

    return HttpResponse("Our latest coordinates are: %f lat, %f long. This was sent at %s and recieved at %s." % (lat,long,created,updated))


def location(request):
    lat = GPS.objects.latest('created_at').lat
    long = GPS.objects.latest('created_at').long
    created = GPS.objects.latest('created_at').created_at.strftime('%Y-%m-%d')
    updated = GPS.objects.latest('created_at').updated_at.strftime('%Y-%m-%d')
    return render(request, 'map/location.html', {'title': 'Current location', 'latitude': lat,'longitude': long, 'created': created, 'updated': updated})


class GPSViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = GPS.objects.order_by('-created_at').all()
    serializer_class = GPSSerializer
