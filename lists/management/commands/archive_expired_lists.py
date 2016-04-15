from django.core.management import BaseCommand
from django.utils import timezone
from lists.models import List


class Command(BaseCommand):
    def handle(self, *args, **options):
        now = timezone.now().date()
        List.objects.all().filter(expired=False)\
            .filter(expiration_date__lte=now).update(expired=True)
