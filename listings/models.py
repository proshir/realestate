from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Province(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Address(models.Model):
    street = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=10)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.zipcode + " " + self.street

class RentDetail(models.Model):
    description = models.TextField()
    prepayment = models.IntegerField()
    monthly_fee = models.IntegerField()

    def __str__(self):
        return self.monthly_fee
    
class Apartment(models.Model):
    address = models.OneToOneField(Address, on_delete=models.CASCADE, related_name='apartment')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='oapartment')
    tenant = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='rapartment')
    rent_detail = models.ForeignKey(RentDetail, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='apartment/')
    beds = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    size = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    for_rent = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Offer(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name='offers')
    tenant = models.ForeignKey(User, on_delete=models.CASCADE)
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return f"Offer ID: {self.id} | Apartment: {self.apartment.title} | Tenant: {self.tenant.username}"