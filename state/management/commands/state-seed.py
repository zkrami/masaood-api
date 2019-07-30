from django.core.management.base import BaseCommand
from django.utils import log
# python manage.py seed --mode=refresh

from state.models import State


def state_seed():

    states = [
        {
            "nameEn": "Abu Dhabi",
            "nameAr": "ابو ظبي"
        },
        {
            "nameEn": "Dubai",
            "nameAr": "دبي"
        },
        {
            "nameEn": "Ras Al Khaimah",
            "nameAr": "راس الخيمة"
        },
        {
            "nameEn": "Fujairah",
            "nameAr": "الفجيرة"
        }, {
            "nameEn": "Sharjah",
            "nameAr": "الشارقة"
        }, {
            "nameEn": "Ajman",
            "nameAr": "عجمان"
        }, {
            "nameEn": "Umm Al Quwain",
            "nameAr": "ام القويين"
        }, {
            "nameEn": "Al Ain",
            "nameAr": "العين"
        }
    ]
    for state in states:
        State.objects.update_or_create(nameEn=state["nameEn"] , defaults=state)


class Command(BaseCommand):
    help = "seed states tables"

    def handle(self, *args, **options):
        self.stdout.write('seeding states...')
        state_seed()
        self.stdout.write('done.')
