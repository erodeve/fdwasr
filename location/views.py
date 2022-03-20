from django.shortcuts import render
from location.models import Location 
from home.models import Homecontent, Mapboxtoken
import json 



def location_view(request): 
    mapbox_token = Mapboxtoken.objects.last()
    location = Location.objects.last()
    polygon = json.dumps(location.polygon)
    home_content = Homecontent.objects.last()
    
    context = {
        'mapbox_token': mapbox_token.token,
        'home_content': home_content,
        'polygon': polygon,
        'location': location,
        'section': 'location',
    }
    return render(request, 'location/location.html', context)
    