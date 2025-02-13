from django.db import models
from django.contrib.auth.models import User

class Livreur(models.Model):
    photo = models.ImageField(upload_to='images/', blank=True, null=True)
    nom = models.CharField(max_length=200 , null=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    is_active = models.BooleanField(default=True)  # statut pour savoir si le livreur est actif
    created_at = models.DateTimeField(auto_now_add=True)
    




class Livraison(models.Model):
    livreur = models.ForeignKey(Livreur, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.TextField()  # adresse de livraison
    client_name = models.CharField(max_length=100)
    client_phone_number = models.CharField(max_length=15)
    status_choices = [
        ('En Attente', 'En Attente'),
        ('En Cours', 'En Cours'),
        ('Livrée', 'Livrée'),
        ('Échouée', 'Échouée'),
    ]
    status = models.CharField(max_length=10, choices=status_choices, default='En Attente')
    delivery_date = models.DateTimeField(null=True, blank=True)  # Date de livraison prévue
    delivered_at = models.DateTimeField(null=True, blank=True)  # Date de livraison réelle
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Livraison pour {self.client_name} ({self.status})"


class HistoriqueLivraison(models.Model):
    livreur = models.ForeignKey(Livreur, on_delete=models.CASCADE)
    livraison = models.ForeignKey(Livraison, on_delete=models.CASCADE)
    status_at_time = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Historique pour {self.livreur.nom} - {self.livraison.client_name}"



class Feedback(models.Model):
    livraison = models.ForeignKey(Livraison, on_delete=models.CASCADE)
    livreur = models.ForeignKey(Livreur, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # Évaluation de 1 à 5
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback pour {self.livraison.client_name} - Évaluation {self.rating}/5"

