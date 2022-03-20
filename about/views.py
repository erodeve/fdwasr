from django.shortcuts import render
from home.models import Homecontent
from about.models import About 


def about_view(request): 
    about = About.objects.last()
    home_content = Homecontent.objects.last()
    context = {
        'home_content': home_content,
        'section': 'about',
        'about': about,
    }
    return render(request, 'about/about.html', context)

    