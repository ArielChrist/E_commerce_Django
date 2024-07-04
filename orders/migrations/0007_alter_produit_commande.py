# Generated by Django 5.0.6 on 2024-07-04 19:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_produit_categorie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='commande',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='produits', to='orders.commande'),
        ),
    ]