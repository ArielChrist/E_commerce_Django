from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import Permission
from orders.models import Produit
from django.contrib.contenttypes.models import ContentType

class Command(BaseCommand):
    help = 'permet de créer des permissions'

    def add_arguments(self, parser):
        parser.add_argument('permission_names', nargs='+', type=str, help='Nom de la permission à créer')

    def handle(self, *args, **options):
        content_type = ContentType.objects.create(app_label='orders', model='Produit')
        for permission_name in options['permission_names']:
            _, created = Permission.objects.get_or_create(
                name=permission_name,
                content_type=content_type,
                codename=f"O-{permission_name}"
            )
            if not created:
                raise CommandError(f'la permission {permission_name} existe déjà')

            self.stdout.write(self.style.SUCCESS(f'la permission {permission_name} a été créer avec succès'))