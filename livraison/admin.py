from django.contrib import admin
from .models import Livreur , Livraison , Feedback , HistoriqueLivraison
# Register your models here.

class AdminLivraison(admin.ModelAdmin):
    list_display = ('livreur','address','client_name','client_phone_number','status','delivery_date','delivered_at','created_at')

class AdminLivreur(admin.ModelAdmin):
    list_display = ('photo','nom','phone_number','address','is_active','created_at')

class AdminFeedback(admin.ModelAdmin):
    list_display = (
        'livraison',
        'livreur',
        'rating',
        'comment',
        'created_at'
    )

class AdminHistoriqueLivraison(admin.ModelAdmin):
    list_display=(
        'livreur',
        'livraison',
        'status_at_time',
        'timestamp'
    )

admin.site.register(HistoriqueLivraison , AdminHistoriqueLivraison)
admin.site.register(Livraison,AdminLivraison)
admin.site.register(Livreur,AdminLivreur)
admin.site.register(Feedback , AdminFeedback)

