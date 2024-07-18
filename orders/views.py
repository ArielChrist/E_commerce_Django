from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Produit, Client, Commande
from .decorators import decorator
from django.views.decorators.http import require_http_methods

# Create your views here.

def hello(request):
    produits = Produit.objects.all()
    lists = list()
    for produit in produits:
        lists.append(f"<li>{produit.libelle}</li>")

    result = "".join(lists)
    html = f"""
        <h3>Produits</h3>
        <ul>
          {result}
        </ul>
    """
    return HttpResponse(html)


def client_infos(request, id):
    client = get_object_or_404(Client, id=id)
    commande = client.commandes.all().first()
    produits = commande.produits.all()
    divs = [f"""<div>
            <p>{produit.libelle}</p>
            <p>{produit.prix}</p>
            <p>{produit.disponibilite}</p>
            </div>
         """for produit in produits]
    html = f"""
        <h3>Client</h3>
        <p>Nom et Prenom : {client.first_name} {client.last_name}</p>
         <h3>Commande</h3>
        <p>Numero de commande: {commande.numero_commande}</p>
        <p>Date de commande: {commande.create_at}</p>
        <h3>Produits</h3>
        <div>
            {"".join(divs)}
        </div>

           
    """
    return HttpResponse(html)


@decorator
def process_test_request():
    return HttpResponse('You can pass') 
