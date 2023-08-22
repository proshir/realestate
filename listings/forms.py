from django import forms
from .models import Apartment, RentDetail, Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['street', 'zipcode', 'city']

class RentDetailForm(forms.ModelForm):
    class Meta:
        model = RentDetail
        fields = ['prepayment', 'monthly_fee', 'description']

class ApartmentForm(forms.ModelForm):
    enctype="multipart/form-data"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        data = kwargs.get('data')
        instance = kwargs.get('instance')

        if instance:
            del kwargs['instance']
            self.rent_detail_form = RentDetailForm(instance=instance.rent_detail, *args, **kwargs)
            self.address_form = AddressForm(instance=instance.address, *args, **kwargs)
        else:
            self.rent_detail_form = RentDetailForm(*args, **kwargs)
            self.address_form = AddressForm(*args, **kwargs)

    class Meta:
        model = Apartment
        fields = ['for_rent', 'title', 'image', 'beds', 'bathrooms', 'size']

    def save(self, commit=True):
        apartment = super().save(commit=False)
        address = self.address_form.save(commit=False)
        rent_detail = self.rent_detail_form.save(commit=False)
        address.save()
        rent_detail.save()
        apartment.address = address
        apartment.rent_detail = rent_detail
        if apartment.for_rent == True:
            apartment.tenant = None

        if commit:
            apartment.save()
        return apartment
