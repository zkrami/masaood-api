from django.core.management.base import BaseCommand
from django.utils import log
# python manage.py seed --mode=refresh
from product.models import Grade


def grades_seed():

    grades = [
        {
            "nameEn": "Kg",
            "nameAr": "حضانة"
        },
        {
            "nameAr": "",
            "nameEn": "",
        },
        {
            "nameAr": "",
            "nameEn": "",
        },
        {
            "nameAr": "",
            "nameEn": "",
        },
        {
            "nameAr": "",
            "nameEn": "",
        }
    ]

    for grade in grades:
        Grade.objects.update_or_create(**grade)


class Command(BaseCommand):
    help = "seed grades tables"

    def handle(self, *args, **options):
        self.stdout.write('seeding grades')
        grades_seed()
        self.stdout.write('done.')
