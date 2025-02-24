from django.shortcuts import redirect, render
from .models import Product , Commande
from django.contrib.auth.decorators import login_required
from datetime import timedelta
from django.utils.timezone import now

#from django.core.paginator import Paginator

# Create your views here.
"""
def index(request):
    return render (request , 'shop/index.html')

"""
@login_required
def index(request):
    Product_object = Product.objects.all()
    item_name= request.GET.get('item-name')
    if item_name !='' and item_name is not None:
        #categories_object = Category.objects.filter(
        Product_object = Product.objects.filter(title__icontains=item_name)
        Product_object = Product.objects.filter(description__icontains=item_name)

  #  paginator = Paginator(Product_object , 4 )
   # page = request.GET.get('page')
   # Product_object = paginator.get_page(page)
    return render (request,'shop/index.html' , {'Product_object' : Product_object})





def checkout(request):
    if request.method == 'POST':
        items = request.POST.get('items')
        total = request.POST.get('total')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        adresse = request.POST.get('adresse')
        statu = request.POST.get('statu')

        
        
        # Créer la commande
        com = Commande(
            user=request.user,
            items=items, 
            total=total, 
            latitude=latitude if latitude else None, 
            longitude=longitude if longitude else None, 
            adresse=adresse if adresse else None,
            statu=statu if statu else 'Normale'
        )
        com.save()
        

        #  Redirige vers la page de confirmation
        return redirect('confirmation')

    return render(request, 'shop/checkout.html')
    
"""
def ajouter_frais_livraison(commande_id):
    try:
        commande = Commande.objects.get(id=commande_id)
        
        # Vérifie le statut et ajoute les frais appropriés
        if commande.statu == 'Normale 1000 FCFA':
            commande.total = float(commande.total) + 1000
        elif commande.statu == 'Express 1500 FCFA':
            commande.total = float(commande.total) + 1500
        
        commande.save()
        return f"Frais ajoutés avec succès. : {commande.total}"
    
    except Commande.DoesNotExist:
        return "Commande introuvable."
    except Exception as e:
        return f"Erreur : {str(e)}"""


def confirmation(request):
    derniere = Commande.objects.filter(user=request.user).order_by('-date_commande').first()
    nouveau_total = request.session.pop('nouveau_total', None)
    commande_id = request.session.pop('commande_id', None)

    commande = None
    if commande_id:
        commande = Commande.objects.get(id=commande_id)

    return render(request, 'shop/confirmation.html', {'derniere_commande': derniere,
                                                      'commande': commande,
                                                      'nouveau_total': nouveau_total})


