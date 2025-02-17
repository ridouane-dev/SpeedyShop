from django.db import models
from django.contrib.auth.models import User  # Import du modèle User

#create models here

class Category(models.Model):
    name= models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
         ordering =['-date_added']

    def __str__(self) :
         return self.name

class Product(models.Model):
     title = models.CharField(max_length=200)
     price = models.FloatField()
     description = models.CharField(max_length=200)
     categorie = models.ForeignKey(Category, related_name='categorie',on_delete=models.CASCADE)
     image = models.ImageField(upload_to='images/')
     date_added = models.DateTimeField(auto_now=True)
     class Meta:
         ordering =['-date_added']

     def __str__(self) :
         return self.title
     def get_image_url(self):
          if self.image:
               return self.image.url
          return None


      
class Commande(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Association avec l'utilisateur
    items = models.CharField(max_length=300)
    total = models.CharField(max_length=200)
    date_commande = models.DateTimeField(auto_now_add=True)
    latitude = models.FloatField(null=True, blank=True)  # Champ pour la latitude
    longitude = models.FloatField(null=True, blank=True)  # Champ pour la longitude
    adresse = models.CharField(max_length=255, null=True, blank=True)  # Adresse optionnelle
    statu_choices = [
        ('Normale 1000 FCFA', 'Normale 1000 FCFA'),
        ('Express 1500 FCFA', 'Express 1500 FCFA'),
    ]
    statu = models.CharField(max_length=108, choices=statu_choices, default='Normale 1000 FCFA')

    class Meta:
        ordering = ['-date_commande']

    def __str__(self):
        return self.user.first_name if self.user else "Commande sans utilisateur"
    
    def __str__(self):
        return f"Commande {self.id} - {self.user.username} - {self.total} €"



 