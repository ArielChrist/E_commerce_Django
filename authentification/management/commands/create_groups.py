from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import Group
from authentification.models import CustomUser

class Command(BaseCommand):
    help = 'permet de créer des groupes'

    def add_arguments(self, parser):
        parser.add_argument('group_names', nargs='+', type=str, help='Nom du groupe à créer')

    def handle(self, *args, **options):
        for group_name in options['group_names']:
            _, created = Group.objects.get_or_create(name=group_name)
            if not created:
                raise CommandError(f'le groupe {group_name} existe déjà')

            self.stdout.write(self.style.SUCCESS(f'le groupe {group_name} a été créer avec succès'))