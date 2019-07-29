from django.core.management.base import BaseCommand
from django.utils import log
# python manage.py seed --mode=refresh


def size_seed():

    print("dasd asd asdas djlkaskd l;aksdl; aks d")



class Command(BaseCommand):
    help = "seed database for testing and development."


    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        size_seed()
        self.stdout.write('done.')



