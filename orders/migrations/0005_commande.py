# Generated by Django 5.0.6 on 2024-07-01 20:45

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_alter_client_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('numero_commande', models.UUIDField(default=uuid.uuid4)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commandes', to='orders.client')),
            ],
        ),
    ]