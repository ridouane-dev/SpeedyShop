from django.shortcuts import redirect, render
from .models import Product , Commande
from django.contrib.auth.decorators import login_required
#from django.core.paginator import Paginator

# Create your views here.
"""
def index(request):
    return render (request , 'shop/index.html')

"""
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




@login_required
def checkout(request):
    if request.method == 'POST':
        items = request.POST.get('items')
        total = request.POST.get('total')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        adresse = request.POST.get('adresse')

        # Créer la commande avec l'utilisateur connecté et sa localisation
        com = Commande(
            user=request.user,  # Associer la commande à l'utilisateur connecté
            items=items, 
            total=total, 
            latitude=latitude if latitude else None, 
            longitude=longitude if longitude else None, 
            adresse=adresse if adresse else None
        )
        com.save()

        return redirect('confirmation')  # Rediriger vers la page de confirmation

    return render(request, 'shop/checkout.html')

def confirmation(request):

    return render(request, 'shop/confirmation.html')
