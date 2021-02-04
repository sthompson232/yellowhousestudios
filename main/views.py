from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'main/home.html')



def contact(request, website):

    if request.POST:
        form = ContactForm(request.POST)

        if form.is_valid():
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
        form = ContactForm()

    context = {
        "title":"Contact",
        "form":form,
    }
    return render(request, 'main/contact.html', context)



def pricing(request):
    return render(request, 'main/pricing.html')



def portfolio(request):
    return render(request, 'main/portfolio.html')