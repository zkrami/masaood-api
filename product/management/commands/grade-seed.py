from django.core.management.base import BaseCommand
from django.utils import log
# python manage.py seed --mode=refresh
from product.models import Grade


def grades_seed():

    grades = [
        {
            "code" : "KG" , 
            "nameAr": "حضانة",
            "nameEn": "KG"
        },
        {
            "code" : "C1", 
            "nameEn": "Cycle One",
            "nameAr": "حلقة أولى",
        },
        {
            "code" : "C2", 
            "nameEn": "Cycle Two",
            "nameAr": "حلقة ثانية",
        },
        {
            "code" : "C3", 
            "nameEn": "Cycle Three",
            "nameAr": "حلقة ثالثة",
        }
    ]

    for grade in grades:
        Grade.objects.update_or_create(code=grade["code"] , defaults=grade)


class Command(BaseCommand):
    help = "seed grades tables"

    def handle(self, *args, **options):
        self.stdout.write('seeding grades')
        grades_seed()
        self.stdout.write('done.')
