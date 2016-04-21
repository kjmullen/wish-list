from django.conf import settings
from django.core.management import BaseCommand
from django.utils import timezone
from lists.models import List
import stripe


def refund_list_item(item):

    stripe.api_key = settings.STRIPE_SECRET_KEY

    for pledge in item:
        try:
            refund = stripe.Refund.create(charge=pledge.charge_id)

        except stripe.error.InvalidRequestError as e:
            pass

        pledge.refunded = True
        pledge.save()


class Command(BaseCommand):

    def handle(self, *args, **options):

        now = timezone.now().date()
        old_list = List.objects.all().filter(expired=False)\
            .filter(expiration_date__lte=now)

        for still_old in old_list:
            still_old.expired = True
            still_old.save()

            for item in still_old.items.all():
                if not item.fully_pledged:
                    refund_list_item(item)
