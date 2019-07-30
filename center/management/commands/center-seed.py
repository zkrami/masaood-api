from django.core.management.base import BaseCommand
from django.utils import log
# python manage.py seed --mode=refresh

from center.models import Center
from state.models import State 
def center_seed():

    centers = [
        {
            "state": "Abu Dhabi",        
            "nameAr" : "لولو هايبر ماركت -الخالدية مول" , 
            "lat" : 24.4699069 , 
            "lng" : 54.3542791 , 
        },
        {
            "state": "Abu Dhabi",        
            "nameAr" : "لولو هايبر ماركت -الكابيتل مول" , 
            "lat" : 24.376023 , 
            "lng" : 54.528178 , 
        },
        {
            "state": "Abu Dhabi",        
            "nameAr" : "لولو هايبر ماركت - بانياس" , 
            "lat" : 24.296276 , 
            "lng" : 54.6339503 , 
        },
        {
            "state": "Abu Dhabi",        
            "nameAr" : "لولو هايبر ماركت - المشرف مول" , 
            "lat" : 24.296276 , 
            "lng" : 54.6339503 , 
        },
        {
            "state": "Abu Dhabi",        
            "nameAr" : "لولو هايبر ماركت - الرويس مول" , 
            "lat" : 24.080912 , 
            "lng" : 52.667154 , 
        },
        {
            "state": "Abu Dhabi",        
            "nameAr" : "لولو هايبر ماركت -  مركز التجارة العالمي" , 
            "lat" : 24.4892523 , 
            "lng" : 54.357904 , 
        },
        {
            "state": "Dubai",        
            "nameAr" : "لولو هايبر ماركت -  الورقاء" , 
            "lat" : 25.197249 , 
            "lng" : 55.4535105 , 
        },
         {
            "state": "Dubai",        
            "nameAr" : "لولو هايبر ماركت -  القصيص" , 
            "lat" : 25.2790975 , 
            "lng" : 55.3645931 , 
        },
         {
            "state": "Dubai",        
            "nameAr" : "لولو هايبر ماركت -  البرشا" , 
            "lat" : 25.117184 , 
            "lng" : 55.205395 , 
        },
         {
            "state": "Dubai",        
            "nameAr" : "لولو هايبر ماركت -  الراشدية" , 
            "lat" : 25.2267762 , 
            "lng" : 55.3849269 , 
        },
         {
            "state": "Dubai",        
            "nameAr" : "لولو هايبر ماركت -  المركز العربي" , 
            "lat" : 25.2345393 , 
            "lng" : 55.4338451 , 
        },
         {
            "state": "Ras Al Khaimah",        
            "nameAr" : "لولو هايبر ماركت -  راس الخيمة مول" , 
            "lat" : 25.7720457 , 
            "lng" : 55.9571018 , 
        },
          {
            "state": "Fujairah",        
            "nameAr" : "لولو هايبر ماركت -  الفجيرة" , 
            "lat" : 25.1201665 , 
            "lng" : 56.3303677 , 
        },
           {
            "state": "Fujairah",        
            "nameAr" : "لولو هايبر ماركت -  دبا" , 
            "lat" : 25.5888325 , 
            "lng" : 56.2704685 , 
        },
           {
            "state": "Sharjah",        
            "nameAr" : "لولو هايبر ماركت -  الشارقة" , 
            "lat" : 25.3031626 , 
            "lng" : 55.3719871 , 
        },
        {
            "state": "Sharjah",        
            "nameAr" : "لولو هايبر ماركت -  الحزانة الشارقة" , 
            "lat" : 25.374719 , 
            "lng" : 55.4189443 , 
        },
        {
            "state": "Ajman",        
            "nameAr" : "لولو هايبر ماركت -  عجمان" , 
            "lat" : 25.406876 , 
            "lng" : 55.4462697 , 
        },
        {
            "state": "Umm Al Quwain",        
            "nameAr" : "لولو هايبر ماركت -  ام القويين" , 
            "lat" : 25.5639134 , 
            "lng" : 55.5496953 , 
        },
        {
            "state": "Al Ain",        
            "nameAr" : "لولو هايبر ماركت -الفلاح بلازا-شارع خليفة" , 
            "lat" : 24.2243751 , 
            "lng" : 55.8321881 , 
        },
         {
            "state": "Al Ain",        
            "nameAr" : "لولو هايبر ماركت -  القويتات" , 
            "lat" : 24.2322083 , 
            "lng" : 55.7719304 , 
        },
         {
            "state": "Al Ain",        
            "nameAr" : "لولو هايبر ماركت - البراري مول" , 
            "lat" : 24.0864593 , 
            "lng" : 55.8321026 , 
        },
         {
            "state": "Al Ain",        
            "nameAr" : "لولو هايبر ماركت - الفواه مول" , 
            "lat" : 24.3438233 , 
            "lng" : 55.790433 , 
        },
    ]
   
    for center in centers:
        
        state = State.objects.get(nameEn=center["state"])
        center.pop("state")
        center["nameEn"] = center["nameAr"]
        centerObj , _ = Center.objects.update_or_create(nameEn=center["nameEn"] , defaults=center)
        centerObj.states.add(state)


class Command(BaseCommand):
    help = "seed centers tables"

    def handle(self, *args, **options):
        self.stdout.write('seeding centers...')
        center_seed()
        self.stdout.write('done.')
