from django.shortcuts import render, redirect
from .models import Produit
from .forms import ProduitForm
import pickle
import numpy as np
import os

# Chemin vers model.pkl
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # produits/
BASE_DIR = os.path.dirname(BASE_DIR)  # estimation/
model_path = os.path.join(BASE_DIR, 'model.pkl')

def ajouter_produit(request):
    # Charger le modèle seulement ici, au moment de l'estimation
    with open(model_path, 'rb') as f:
        model = pickle.load(f)

    if request.method == 'POST':
        form = ProduitForm(request.POST)
        if form.is_valid():
            produit = form.save(commit=False)

            poids = np.array([[produit.poids]])
            prix_estime = model.predict(poids)[0]

            produit.prix_estime = prix_estime
            produit.save()
            return redirect('liste_produits')
    else:
        form = ProduitForm()
    return render(request, 'produits/ajouter_produit.html', {'form': form})

def liste_produits(request):
    produits = Produit.objects.all()
    return render(request, 'produits/liste_produits.html', {'produits': produits})
