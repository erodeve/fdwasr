from django.shortcuts import render
from home.models import Homecontent
from menu.models import Menu 


def menu_view(request): 
    menus = Menu.objects.all()
    home_content = Homecontent.objects.last()
    context = {
        'home_content': home_content,
        'menus': menus,
        'section': 'menu',
    }
    return render(request, 'menu/menu.html', context)
    