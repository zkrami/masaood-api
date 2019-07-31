from django.core.management.base import BaseCommand
from django.utils import log
# python manage.py seed --mode=refresh
from product.models import Size


def size_seed():

    sizes = [
        {
            "nameAr": "4-5",
            "nameEn": "4-5",
            "code": "4-5"
        },
        {
            "nameAr": "5-6",
            "nameEn": "5-6",
            "code": "5-6"
        },
        {
            "nameAr": "6-7",
            "nameEn": "6-7",
            "code": "6-7"
        },
        {
            "nameAr": "7-8",
            "nameEn": "7-8",
            "code": "7-8"
        },
        {
            "nameAr": "8-9",
            "nameEn": "8-9",
            "code": "8-9"
        },
        {
            "nameAr": "9-10",
            "nameEn": "9-10",
            "code": "9-10"
        },
        {
            "nameAr": "10-11",
            "nameEn": "10-11",
            "code": "10-11"
        },
        {
            "nameAr": "11-12",
            "nameEn": "11-12",
            "code": "11-12"
        },
        {
            "nameAr": "12-13",
            "nameEn": "12-13",
            "code": "12-13"
        },
        {
            "nameAr": "13-14",
            "nameEn": "13-14",
            "code": "13-14"
        },
        {
            "nameAr": "14-15",
            "nameEn": "14-15",
            "code": "14-15"
        },
        {
            "nameAr": "15-16",
            "nameEn": "15-16",
            "code": "15-16"
        },
        {
            "nameAr": "صغير",
            "nameEn": "Small",
            "code": "S"
        },
        {
            "nameAr": "متوسط",
            "nameEn": "Medium",
            "code": "M"
        }, {
            "nameAr": "كبير",
            "nameEn": "Large",
            "code": "L"
        },
        {
            "nameAr": "كبير جدا",
            "nameEn": "XLarge",
            "code": "XL"
        }
    ]
    for size in sizes:
        Size.objects.update_or_create(code=size["code"], defaults=size)


class Command(BaseCommand):
    help = "seed sizes tables"

    def handle(self, *args, **options):
        self.stdout.write('seeding sizes...')
        size_seed()
        self.stdout.write('done.')
