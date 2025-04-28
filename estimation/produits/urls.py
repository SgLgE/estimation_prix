from django.urls import path
from . import views

urlpatterns = [
    path('ajouter/', views.ajouter_produit, name='ajouter_produit'),
    path('', views.liste_produits, name='liste_produits'),
]
