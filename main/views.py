from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

import json
import urllib

from .forms import ContactForm

# Create your views here.
def home(request):

    context = {
        "title":"Web Design"
    }
    return render(request, 'main/home.html', context)



def contact(request, website=''):

    if website == 'basic':
        initial = {'package':'Basic Website'}
    if website == 'standard':
        initial = {'package':'Standard Website'}
    if website == 'business':
        initial = {'package':'Business Website'}
    else:
        initial = ''

    if request.POST:
        form = ContactForm(request.POST)

        if form.is_valid():

            ''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req =  urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            ''' End reCAPTCHA validation '''

            if result['success']:
                first_name = request.POST['first_name']
                last_name = request.POST['last_name']
                email = request.POST['email']
                package = request.POST['package']
                message = request.POST['message']

                message_subject = first_name + ' ' + last_name

                email_message = 'Name: ' + first_name + ' ' + last_name + '\n\nTheir Email: ' + email + '\n\nWebsite Package: ' + package + '\n\nMessage: ' + message 

                send_mail(
                    message_subject, 
                    email_message,
                    email,
                    ['samthompson292@gmail.com'],
                )
                messages.success(request, 'You have successfully sent an email.')
                return redirect('contact', {'website':'consultation'})
            else:
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')
    else:
        form = ContactForm(initial=initial)

    context = {
        "title":"Free Website Consultation",
        "form":form,
    }
    return render(request, 'main/contact.html', context)



def pricing(request):

    context = {
        "title":"Pricing",
    }
    return render(request, 'main/pricing.html', context)



def portfolio(request):

    context = {
        "title":"Our Portfolio",
    }
    return render(request, 'main/portfolio.html', context)