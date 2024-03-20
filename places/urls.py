from django.urls import path
from . import views

app_name = 'places'

urlpatterns = [
    path('', views.PlacesView.as_view(), name='places'),
    path('desc/<int:place_id>/', views.product_desc, name='places_desc'),
    path('profile/', views.Profile , name='profile'),
]