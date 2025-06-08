from django.views import View
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
class index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'send/index.html', {'state': ''})
    
    def post(self, request, *args, **kwargs):
        
        title = request.POST.get('title')
        text  = request.POST.get('text')
        to    = request.POST.get('to')

        send_mail(
            title,
            text,
            settings.EMAIL_HOST_USER,
            [to],
            fail_silently = False
        )
    
        return render(request, 'send/index.html', {'state':'Se Envió Correctamente'})