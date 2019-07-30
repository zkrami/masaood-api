from django.core.management.base import BaseCommand
from django.utils import log
from django.core.management import call_command


class Command(BaseCommand):
    help = "initialize all tables"

    def handle(self, *args, **options):
        self.stdout.write('seeding all tables')
        call_command("user-seed")
        call_command("grade-seed")
        call_command("size-seed")
        call_command("state-seed")
        call_command("center-seed")
        call_command("media-seed")


        self.stdout.write('done.')



