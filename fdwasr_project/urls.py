"""fdwasr_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include 
from django.conf import settings 
from django.conf.urls.static import static
from menu.views import *
from location.views import * 
from ordernow.views import *
from about.views import *
from home.views import *
from contact.views import * 


urlpatterns = [

    path('order_created/', order_created_view, name='order_created'),
    
    path('contact/', contact_view, name="contact"),

    path('about/', about_view, name="about"),

    path('checkout/', checkout_view, name='checkout'),
    path('submit_location/', submit_location_view, name="submit_location"),
    path('ordernow/', ordernow_view, name="ordernow"),

    path('location/', location_view, name="location"), 
    
    path('menu/', menu_view, name="menu"),

    path('', home_view, name='home'),

    path('admin/', admin.site.urls),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
