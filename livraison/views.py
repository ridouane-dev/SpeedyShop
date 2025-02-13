
from django.shortcuts import render, redirect
from .models import Livreur ,Livraison ,Feedback ,HistoriqueLivraison
from django.contrib.auth.models import User
from boutique.models import Commande
def save_livreur(request):
    if request.method == 'POST':
        # Récupérer les données du formulaire
        nom = request.POST['nom']
        phone_number = request.POST['phone_number']
        address = request.POST['address']
        is_active = 'is_active' in request.POST  # Le champ est un checkbox, il peut être absent ou présent
        photo = request.FILES.get('photo')  # Le champ photo est dans le formulaire comme un fichier

       
        # Créer un livreur
        livreur = Livreur(
              # Lier le livreur à l'utilisateur
            nom=nom,
            phone_number=phone_number,
            address=address,
            is_active=is_active,
            photo=photo
        )
        livreur.save()  # Enregistrer le livreur dans la base de données
        
        return redirect('dashboard')  # Rediriger vers une page après enregistrement (remplace 'some_view' par l'URL ou le nom de vue souhaité)
    
    return render(request, 'dashboardlivreur_form.html')  # Retourner le formulaire en cas de GET


def assign_livraison(request):
    if request.method == 'POST':
        # Récupérer les données du formulaire
        client_name = request.POST.get('client_name')
        client_phone_number = request.POST.get('client_phone_number')
        address = request.POST.get('address')  # Assure-toi que l'adresse est envoyée
        delivery_date = request.POST.get('delivery_date')
        status = request.POST.get('status')
        livreur_id = request.POST.get('livreur')

        # Vérifier si un livreur est sélectionné
        livreur = None
        if livreur_id:
            try:
                livreur = Livreur.objects.get(id=livreur_id)
            except Livreur.DoesNotExist:
                pass  # Gérer le cas où le livreur n'existe pas

        # Créer une instance de Livraison
        livraison = Livraison(
            client_name=client_name,
            client_phone_number=client_phone_number,
            address=address,
            delivery_date=delivery_date if delivery_date else None,
            status=status,
            livreur=livreur
        )
        livraison.save()  # Enregistrement dans la base de données
         # Ajouter une entrée dans l’historique de livraison
        if livreur:
            HistoriqueLivraison.objects.create(
                livreur=livreur,
                livraison=livraison,
                status_at_time=status
            )


        return redirect('dashboard')  # Rediriger après l'enregistrement

    # Récupérer la liste des livreurs pour l'affichage du formulaire
    livreurs = Livreur.objects.all()
    return render(request, 'dashboardassign_livraison.html', {'livreurs': livreurs})



def dashboard(request):
    livraisons = Livraison.objects.all()
    total_livraisons = Livraison.objects.count()  # Calculer le total des livraisons
    livreur_actif = Livreur.objects.count()
    return render(request , 'dashboarddashboard.html',{'livraison' : livraisons,
                                               'total_livraisons':total_livraisons,
                                                'livreur_actif':livreur_actif})

def index (request):
    return render (request , 'livraison.html')



def client_dashboard(request):
    # Récupérer l'historique des livraisons pour ce client
    client_livraisons = HistoriqueLivraison.objects.all()
    return render(request, 'dashboardclient_dashboard.html', {'historiques': client_livraisons})


def confirm_reception(request):
    if request.method == 'POST':
        livraison_id = request.POST['livraison_id']
        livraison = Livraison.objects.get(id=livraison_id)
        livraison.status = 'Livrée'
        livraison.save()
        return redirect('client_dashboard')

def rate_service(request):
    if request.method == 'POST':
        livraison_id = request.POST['livraison_id']
        rating = request.POST['rating']
        comment = request.POST.get('comment', '')

        livraison = Livraison.objects.get(id=livraison_id)
        Feedback.objects.create(
            livraison=livraison,
            livreur=livraison.livreur,
            rating=rating,
            comment=comment
        )
        return redirect('dashboardclient_dashboard')
    
def com(request):
    comm = Commande.objects.all().order_by('-date_commande')
    return render (request , 'com.html',{'com':comm})


