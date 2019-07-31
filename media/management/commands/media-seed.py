from django.core.management.base import BaseCommand
from django.utils import log
# python manage.py seed --mode=refresh

from media.models import Media

def media_seed():

    medias = [{"name":"cycle_one_boys_formal_shirt.png","file":"../media/cycle_one_boys_formal_shirt.png"},{"name":"cycle_one_boys_formal_shoes.png","file":"../media/cycle_one_boys_formal_shoes.png"},{"name":"cycle_one_boys_formal_socks.png","file":"../media/cycle_one_boys_formal_socks.png"},{"name":"cycle_one_boys_formal_trouser.png","file":"../media/cycle_one_boys_formal_trouser.png"},{"name":"cycle_one_boys_sport_jacket.png","file":"../media/cycle_one_boys_sport_jacket.png"},{"name":"cycle_one_boys_sport_shirt.png","file":"../media/cycle_one_boys_sport_shirt.png"},{"name":"cycle_one_boys_sport_shoes.png","file":"../media/cycle_one_boys_sport_shoes.png"},{"name":"cycle_one_boys_sport_trouser.png","file":"../media/cycle_one_boys_sport_trouser.png"},{"name":"cycle_one_girls_formal_dress.png","file":"../media/cycle_one_girls_formal_dress.png"},{"name":"cycle_one_girls_formal_shirt.png","file":"../media/cycle_one_girls_formal_shirt.png"},{"name":"cycle_one_girls_formal_shoes.png","file":"../media/cycle_one_girls_formal_shoes.png"},{"name":"cycle_one_girls_sport_jacket.png","file":"../media/cycle_one_girls_sport_jacket.png"},{"name":"cycle_one_girls_sport_shirt.png","file":"../media/cycle_one_girls_sport_shirt.png"},{"name":"cycle_one_girls_sport_trouser.png","file":"../media/cycle_one_girls_sport_trouser.png"},{"name":"cycle_three_boys_formal_hamdaniah.png","file":"../media/cycle_three_boys_formal_hamdaniah.png"},{"name":"cycle_three_boys_formal_kandoora.png","file":"../media/cycle_three_boys_formal_kandoora.png"},{"name":"cycle_three_boys_formal_shoes.png","file":"../media/cycle_three_boys_formal_shoes.png"},{"name":"cycle_three_boys_sport_jacket.png","file":"../media/cycle_three_boys_sport_jacket.png"},{"name":"cycle_three_boys_sport_shirt.png","file":"../media/cycle_three_boys_sport_shirt.png"},{"name":"cycle_three_boys_sport_trouser.png","file":"../media/cycle_three_boys_sport_trouser.png"},{"name":"cycle_three_girls_formal_jacket.png","file":"../media/cycle_three_girls_formal_jacket.png"},{"name":"cycle_three_girls_formal_shirt.png","file":"../media/cycle_three_girls_formal_shirt.png"},{"name":"cycle_three_girls_formal_skirt.png","file":"../media/cycle_three_girls_formal_skirt.png"},{"name":"cycle_three_girls_sport_jacket.png","file":"../media/cycle_three_girls_sport_jacket.png"},{"name":"cycle_three_girls_sport_shirt.png","file":"../media/cycle_three_girls_sport_shirt.png"},{"name":"cycle_three_girls_sport_trouser.png","file":"../media/cycle_three_girls_sport_trouser.png"},{"name":"cycle_two_boys_sport_jacket.png","file":"../media/cycle_two_boys_sport_jacket.png"},{"name":"cycle_two_boys_sport_shirt.png","file":"../media/cycle_two_boys_sport_shirt.png"},{"name":"cycle_two_boys_sport_trouser.png","file":"../media/cycle_two_boys_sport_trouser.png"},{"name":"cycle_two_girls_formal_dress.png","file":"../media/cycle_two_girls_formal_dress.png"},{"name":"cycle_two_girls_formal_shirt.png","file":"../media/cycle_two_girls_formal_shirt.png"},{"name":"cycle_two_girls_sport_jacket.png","file":"../media/cycle_two_girls_sport_jacket.png"},{"name":"cycle_two_girls_sport_shirt.png","file":"../media/cycle_two_girls_sport_shirt.png"},{"name":"cycle_two_girls_sport_trouser.png","file":"../media/cycle_two_girls_sport_trouser.png"},{"name":"kindergarten_boys_formal_shirt.png","file":"../media/kindergarten_boys_formal_shirt.png"},{"name":"kindergarten_boys_formal_shoes.png","file":"../media/kindergarten_boys_formal_shoes.png"},{"name":"kindergarten_boys_formal_socks.png","file":"../media/kindergarten_boys_formal_socks.png"},{"name":"kindergarten_boys_sport_jacket.png","file":"../media/kindergarten_boys_sport_jacket.png"},{"name":"kindergarten_boys_sport_shirt.png","file":"../media/kindergarten_boys_sport_shirt.png"},{"name":"kindergarten_boys_sport_shoes.png","file":"../media/kindergarten_boys_sport_shoes.png"},{"name":"kindergarten_boys_sport_trouser.png","file":"../media/kindergarten_boys_sport_trouser.png"},{"name":"kindergarten_girls_formal_shirt.png","file":"../media/kindergarten_girls_formal_shirt.png"},{"name":"kindergarten_girls_formal_shoes.png","file":"../media/kindergarten_girls_formal_shoes.png"},{"name":"kindergarten_girls_formal_skirt.png","file":"../media/kindergarten_girls_formal_skirt.png"},{"name":"kindergarten_girls_formal_socks.png","file":"../media/kindergarten_girls_formal_socks.png"},{"name":"kindergarten_girls_sport_jacket.png","file":"../media/kindergarten_girls_sport_jacket.png"},{"name":"kindergarten_girls_sport_shirt.png","file":"../media/kindergarten_girls_sport_shirt.png"},{"name":"kindergarten_girls_sport_shoes.png","file":"../media/kindergarten_girls_sport_shoes.png"},{"name":"kindergarten_girls_sport_trouser.png","file":"../media/kindergarten_girls_sport_trouser.png"}]; 
    for media in medias:
        Media.objects.update_or_create(name=media["name"] , defaults=media)


class Command(BaseCommand):
    help = "seed medias tables"

    def handle(self, *args, **options):
        self.stdout.write('seeding medias...')
        media_seed()
        self.stdout.write('done.')
