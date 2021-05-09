from django.contrib import admin
from django.urls import path
from .views import get_contacts_list , get_contact

urlpatterns = [
    path('contact', get_contacts_list),
    path('contact/<int:pk>', get_contact),
]