from django.core.management.base import BaseCommand
from django.utils import log
# python manage.py seed --mode=refresh

from center.models import Center , CenterProduct
from product.models import Product


def centers_init():

    for center in Center.objects.all():
        for product in Product.objects.all():
            CenterProduct.objects.update_or_create(product=product , center=center , defaults={'count':1000000})


class Command(BaseCommand):
    help = "add products to centers .."

    def handle(self, *args, **options):
        self.stdout.write('adding products to centers ....')
        centers_init()
        self.stdout.write('done.')
