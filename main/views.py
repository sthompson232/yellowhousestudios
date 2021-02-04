from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'main/home.html')



def contact(request, website):
    return render(request, 'main/contact.html')



def pricing(request):
    return render(request, 'main/pricing.html')



def portfolio(request):
    return render(request, 'main/portfolio.html')