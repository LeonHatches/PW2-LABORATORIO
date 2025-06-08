from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):
    send_mail(
        'Hello from Django',
        'Hello there, this is an automated message.',
        '***@gmail.com',
        ['***@unsa.edu.pe'],
        fail_silently = False
    )
    
    return render(request, 'send/index.html', {})