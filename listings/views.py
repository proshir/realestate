from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Apartment, Offer
from .forms import ApartmentForm
from django.contrib import messages

def apartment_list(request):
    apartments = Apartment.objects.filter(for_rent=True)
    context = {'apartments': apartments}
    return render(request, 'apartments/apartment_list.html', context)

def apartment_detail(request, apartment_id):
    apartment = get_object_or_404(Apartment, id=apartment_id)
    can_send_offer = False
    tenant = request.user
    if tenant and tenant.is_authenticated:
        existing_offer = Offer.objects.filter(apartment=apartment, tenant=tenant).exists()
        if request.user != apartment.owner and apartment.for_rent and not apartment.tenant and not existing_offer:
            can_send_offer = True

        if request.method == 'POST':
            if apartment.for_rent and apartment.owner != request.user:
                    offer = Offer.objects.create(apartment=apartment, tenant=tenant)

    context = {
        'apartment': apartment,
        'can_send_offer' : can_send_offer
    }
    return render(request, 'apartments/apartment_detail.html', context)

@login_required
def add_apartment(request):
    if request.method == 'POST':
        form = ApartmentForm(request.POST, request.FILES)
        if form.is_valid():
            apartment = form.save(commit=False)
            apartment.owner =  request.user
            apartment.save()
            return redirect('apartment_detail', apartment.id)
        else:
            print(form.errors)
            messages.error(request, 'Invalid apartment detail.')
    else:
        form = ApartmentForm()
    return render(request, 'apartments/add_apartment.html', {'form': form})

@login_required
def my_apartments(request):
    user = request.user
    apartments = Apartment.objects.filter(owner=user)
    context = {'apartments': apartments}
    return render(request, 'apartments/my_apartments.html', context)

@login_required
def rented_apartments(request):
    user = request.user
    apartments = Apartment.objects.filter(tenant=user)
    context = {'apartments': apartments}
    return render(request, 'apartments/rented_apartments.html', context)

@login_required
def apartment_detail_owner(request, apartment_id):
    apartment = get_object_or_404(Apartment, id=apartment_id, owner=request.user)
    if request.method == 'POST':
        form = ApartmentForm(request.POST, request.FILES, instance=apartment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Apartment details updated successfully.')
            return redirect('apartment_detail_owner', apartment_id=apartment.id)
    else:
        form = ApartmentForm(instance=apartment)

    context = {
        'form': form,
        'apartment': apartment,
    }
    return render(request, 'apartments/apartment_detail_owner.html', context)

def send_offer_view(request, apartment_id):
    apartment = get_object_or_404(Apartment, id=apartment_id, for_rent=True)
    tenant = request.user
    if request.method == 'POST':
        if tenant and tenant.is_authenticated:
            existing_offer = Offer.objects.filter(apartment=apartment, tenant=tenant).exists()
            if request.user != apartment.owner and apartment.for_rent and not apartment.tenant and not existing_offer:
                offer = Offer.objects.create(apartment=apartment, tenant=tenant)
    return redirect('apartment_detail', apartment_id=apartment.id)

@login_required
def offer_list_view(request):
    owner_offers = Offer.objects.filter(apartment__owner=request.user)
    context = {'offers': owner_offers}
    return render(request, 'offers/offer_list.html', context)

@login_required
def accept_offer_view(request, offer_id):
    offer = get_object_or_404(Offer, id=offer_id)
    apartment = offer.apartment
    apartment.tenant = offer.tenant
    apartment.for_rent = False
    apartment.save()

    related_offers = Offer.objects.filter(apartment=apartment)
    related_offers.delete()

    return redirect('offer_list')