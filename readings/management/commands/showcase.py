from django.core.management.base import BaseCommand

from readings.models import Reading


class Command(BaseCommand):
    help = 'Show case django ORM'

    def handle(self, *args, **options):
        print(Reading.objects.get(pk=1))
