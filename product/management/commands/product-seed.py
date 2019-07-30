from django.core.management.base import BaseCommand
from django.utils import log
# python manage.py seed --mode=refresh
from product.models import Product , AbstractProduct , Grade , Size 

def products_seed():

    products =
    [
        {
            "product": {

            }
        }
    ]
    


class Command(BaseCommand):
    help = "seed products tables"

    def handle(self, *args, **options):
        self.stdout.write('seeding products...')
        products_seed()
        self.stdout.write('done.')
