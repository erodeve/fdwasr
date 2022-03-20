from django.shortcuts import render, HttpResponse
from django.forms import ModelForm
from home.models import Homecontent
from contact.models import Message, Contactcontent


class MessageForm(ModelForm): 
    class Meta: 
        model = Message 
        fields = ['phone', 'email', 'message']


def contact_view(request): 
    if request.method == 'POST': 
        message_form = MessageForm(request.POST)
        if message_form.is_valid(): 
            message_form.save()

            return HttpResponse("""
                <h2>Your message was sent succesfully</h2>
                <a href="/">come back home</a>
            """)
    else: 
        contact_content = Contactcontent.objects.last()
        home_content = Homecontent.objects.last()
        message_form = MessageForm() 
        context = {
            'homw_content': home_content,
            'section': 'contact',
            'message_form': message_form,
            'contact_content': contact_content,
        }
    return render(request, 'contact/contact.html', context)
    