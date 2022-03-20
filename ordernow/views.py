from django.urls import reverse
from django.shortcuts import render, redirect 
from django.http import JsonResponse, HttpResponse
from django.core.serializers import serialize
from home.models import Homecontent, Mapboxtoken
from ordernow.models import Order 
from menu.models import Menu 
from location.models import Location 
import json 


def order_created_view(request): 
    Order.objects.create(
        is_delivered=True,
        cost=request.session.get('total_cost'),
        details=json.loads(request.session.get('order_details'))
    )
    context = { 
        'section': 'order created',
    }
    return render(request, 'ordernow/order_created.html', context)


def checkout_view(request): 

    context = {
        'total_cost': request.session.get('total_cost'),
        'order_details': request.session.get('order_details'),
        'delivery_address': request.session.get('delivery_address'),
        'section': 'checkout',
    }
    return render(request, 'ordernow/checkout.html', context)


def submit_location_view(request): 
    
    if request.method == "POST": 
        request.session['delivery_lat'] = request.POST.get('lat')
        request.session['delivery_lng'] = request.POST.get('lng')
        request.session['delivery_address'] = request.POST.get('address')
        request.session['delivery_name'] = request.POST.get('name')
        request.session['delivery_phone'] = request.POST.get('telephone')
        return JsonResponse({'status': True})
    
    else: 
        mapbox_token = Mapboxtoken.objects.last()
        location = Location.objects.last()
        polygon_json = json.dumps(location.polygon)
        context = {
            'mapbox_token': mapbox_token.token,
            'section': 'submit_location',
            'location': location,
            'polygon': polygon_json,
        }
    return render(request, 'ordernow/submit_location.html', context)


def ordernow_view(request): 
    if request.method == 'POST': 
        request.session['total_cost'] = request.POST.get('totalCost')
        request.session['order_details'] = request.POST.get('orderDetails')
        return JsonResponse({'status': True})

    else: 
        home_content = Homecontent.objects.last()
        items_py = Menu.objects.all()
        items_json = serialize('json', items_py)

        context = {
            'home_content': home_content,
            'section': 'ordernow',
            'items': items_json,
        }
    return render(request, 'ordernow/ordernow.html', context)

    
