from django.core.management import BaseCommand
from lists.models import List


class Command(BaseCommand):
    def handle(self, *args, **options):
        lists = List.objects.all()
        for list_thing in lists:
            if list_thing.check_expired:
                list_thing.expired = True
                list_thing.save()
