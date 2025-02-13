from django.contrib import admin
from .models import Category, Product ,Commande
# Register your models here.
'''
admin.site.site_header = "E-commerce" 
admin.site.site_title = "SBC shop"
admin.site.index_title = "Manageur"
'''
class AdminCategorie(admin.ModelAdmin):
    list_display = ('name' , 'date_added')


class AdmminProduct(admin.ModelAdmin):
    list_display = ('title', 'price', 'categorie' ,'description','image', 'date_added')
    search_fields = ('description',)
    list_editable = ('price','description',)



class AdminCommande(admin.ModelAdmin):
    list_display = ('items','total','date_commande' ,'status', 'adresse')

admin.site.register(Category,AdminCategorie)
admin.site.register(Product,AdmminProduct)
admin.site.register(Commande , AdminCommande)
 
 