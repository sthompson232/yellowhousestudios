from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/<str:website>/', views.contact, name='contact'),
    path('contact/', views.contact, name='contact'),
    path('pricing/', views.pricing, name='pricing'),
    path('portfolio/', views.portfolio, name='portfolio'),
]