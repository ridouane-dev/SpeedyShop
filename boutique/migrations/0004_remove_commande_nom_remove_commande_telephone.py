# Generated by Django 5.1.4 on 2025-02-03 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boutique', '0003_auto_20250201_1228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commande',
            name='Nom',
        ),
        migrations.RemoveField(
            model_name='commande',
            name='Telephone',
        ),
    ]
