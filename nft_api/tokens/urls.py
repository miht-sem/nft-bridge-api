from django.urls import path
from . import views

urlpatterns = [
    path('list', views.getNFTS),
    path('create', views.mintNFT),
    path('total_supply', views.getTotalSupply),
]