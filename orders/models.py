from django.db import models
from uuid import uuid4

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, null=True)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    age = models.IntegerField(null= True)


class Commande(models.Model):
    id = models.AutoField(primary_key=True)
    numero_commande = models.UUIDField(default=uuid4)
    create_at = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="commandes")
    
