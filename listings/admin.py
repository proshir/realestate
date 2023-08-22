from django.contrib import admin
from .models import Address, City, Offer, Province, Apartment, RentDetail

admin.site.register([City, Province, Apartment, Offer, RentDetail, Address])
