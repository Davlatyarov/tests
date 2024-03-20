from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import *

# Create your views here.
class PlacesView(View):
    def get(self, request):
        places = Place.objects.all()
        return render(request, 'places/places_list.html', context={'places': places})

def product_desc(request, place_id):
    desc = get_object_or_404(Place, pk=place_id)
    return render(request, 'places/description.html', {'desc': desc})

def Profile(request):
    return render(request, 'places/profile.html')
