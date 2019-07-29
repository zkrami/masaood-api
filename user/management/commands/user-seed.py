from django.core.management.base import BaseCommand
from django.utils import log
# python manage.py seed --mode=refresh
from django.contrib.auth.models import Group

def group_seed():
    groups = ["admin" , "operator" , "user"]
    for group in groups:
        Group.objects.update_or_create(name=group)



class Command(BaseCommand):
    help = "seed user app tables "

    def handle(self, *args, **options):
        self.stdout.write('seeding user app data ...')
        group_seed()
        self.stdout.write('done.')



