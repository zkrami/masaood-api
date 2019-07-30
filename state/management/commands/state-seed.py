from django.core.management.base import BaseCommand
from django.utils import log
# python manage.py seed --mode=refresh

from state.models import State

def state_seed():

    states = [
      {
          "nameEn" : "" , 
          "nameAr" : "" 
      }
    ]
    for state in sizes:
        State.objects.update_or_create(**state)


class Command(BaseCommand):
    help = "seed sizes tables"

    def handle(self, *args, **options):
        self.stdout.write('seeding sizes...')
        size_seed()
        self.stdout.write('done.')
