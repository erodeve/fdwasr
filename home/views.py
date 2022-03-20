from django.shortcuts import render
from home.models import Homecontent, Mapboxtoken
from location.models import Location 
from menu.models import Menu 


def home_view(request): 
    mapbox_token = Mapboxtoken.objects.last()
    home_content = Homecontent.objects.last() 
    location = Location.objects.last()
    menus = Menu.objects.all() 
    context = {
        'mapbox_token': mapbox_token.token,
        'menus': menus,
        'location': location,
        'home_content': home_content,
        'section': 'home',
    }
    return render(request, 'home/home.html', context)
    