from django.urls import path
from . import views

urlpatterns = [
    path('', views.apartment_list, name='apartment_list'),
    path('apartment/<int:apartment_id>/', views.apartment_detail, name='apartment_detail'),
    path('add_apartment', views.add_apartment, name='add_apartment'),
    path('my_apartments', views.my_apartments, name='my_apartments'),
    path('rented_apartments', views.rented_apartments, name='rented_apartments'),
    path('apartment_detail_owner/<int:apartment_id>/', views.apartment_detail_owner, name='apartment_detail_owner'),
    path('offers/', views.offer_list_view, name='offer_list'),
    path('offers/accept/<int:offer_id>/', views.accept_offer_view, name='accept_offer'),
    path('send_offer/<int:apartment_id>/', views.send_offer_view, name='send_offer'),
]