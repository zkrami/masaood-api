from django.core.management.base import BaseCommand
from django.utils import log
# python manage.py seed --mode=refresh

from state.models import State


def state_seed():

    states = [
        {
            "state": "Abu Dhabi",        
            "nameAr" : "لولو هايبر ماركت -الخالدية مول" , 
            "lat" : 0 , 
            "lng" : 0 , 
        },
        {
            "state": "Abu Dhabi",        
            "nameAr" : "لولو هايبر ماركت -الكابيتل مول" , 
            "lat" : 0 , 
            "lng" : 0 , 
        },
        {
            "state": "Abu Dhabi",        
            "nameAr" : "لولو هايبر ماركت - بانياس" , 
            "lat" : 0 , 
            "lng" : 0 , 
        },
        {
            "state": "Abu Dhabi",        
            "nameAr" : "لولو هايبر ماركت - المشرف مول" , 
            "lat" : 0 , 
            "lng" : 0 , 
        },
        {
            "state": "Abu Dhabi",        
            "nameAr" : "لولو هايبر ماركت - الرويس مول" , 
            "lat" : 0 , 
            "lng" : 0 , 
        },
        {
            "state": "Abu Dhabi",        
            "nameAr" : "لولو هايبر ماركت -  مركز التجارة العالمي" , 
            "lat" : 0 , 
            "lng" : 0 , 
        },
        {
            "state": "Dubai",        
            "nameAr" : "لولو هايبر ماركت -  الورقاء" , 
            "lat" : 0 , 
            "lng" : 0 , 
        },
         {
            "state": "Dubai",        
            "nameAr" : "لولو هايبر ماركت -  القصيص" , 
            "lat" : 0 , 
            "lng" : 0 , 
        },
         {
            "state": "Dubai",        
            "nameAr" : "لولو هايبر ماركت -  البرشا" , 
            "lat" : 0 , 
            "lng" : 0 , 
        },
         {
            "state": "Dubai",        
            "nameAr" : "لولو هايبر ماركت -  الراشدية" , 
            "lat" : 0 , 
            "lng" : 0 , 
        },
         {
            "state": "Dubai",        
            "nameAr" : "لولو هايبر ماركت -  المركز العربي" , 
            "lat" : 0 , 
            "lng" : 0 , 
        },
         {
            "state": "Ras Al Khaimah",        
            "nameAr" : "لولو هايبر ماركت -  راس الخيمة مول" , 
            "lat" : 0 , 
            "lng" : 0 , 
        },
          {
            "state": "Fujairah",        
            "nameAr" : "لولو هايبر ماركت -  الفجيرة" , 
            "lat" : 0 , 
            "lng" : 0 , 
        },
           {
            "state": "Fujairah",        
            "nameAr" : "لولو هايبر ماركت -  دبا" , 
            "lat" : 0 , 
            "lng" : 0 , 
        },
           {
            "state": "Sharjah",        
            "nameAr" : "لولو هايبر ماركت -  الشارقة" , 
            "lat" : 0 , 
            "lng" : 0 , 
        },
        {
            "state": "Sharjah",        
            "nameAr" : "لولو هايبر ماركت -  الحزانة الشارقة" , 
            "lat" : 0 , 
            "lng" : 0 , 
        },
        {
            "state": "Ajman",        
            "nameAr" : "لولو هايبر ماركت -  عجمان" , 
            "lat" : 0 , 
            "lng" : 0 , 
        },
        {
            "state": "Umm Al Quwain",        
            "nameAr" : "لولو هايبر ماركت -  ام القويين" , 
            "lat" : 0 , 
            "lng" : 0 , 
        },
        {
            "state": "Al Ain",        
            "nameAr" : "لولو هايبر ماركت -الفلاح بلازا-شارع خليفة" , 
            "lat" : 0 , 
            "lng" : 0 , 
        },
         {
            "state": "Al Ain",        
            "nameAr" : "لولو هايبر ماركت -  القويتات" , 
            "lat" : 0 , 
            "lng" : 0 , 
        },
         {
            "state": "Al Ain",        
            "nameAr" : "لولو هايبر ماركت - البراري مول" , 
            "lat" : 0 , 
            "lng" : 0 , 
        },
         {
            "state": "Al Ain",        
            "nameAr" : "لولو هايبر ماركت - الفواه مول" , 
            "lat" : 0 , 
            "lng" : 0 , 
        },
    ]
    for state in states:
        State.objects.update_or_create(nameEn=state["nameEn"] , defaults=state)


class Command(BaseCommand):
    help = "seed states tables"

    def handle(self, *args, **options):
        self.stdout.write('seeding states...')
        state_seed()
        self.stdout.write('done.')
