from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from lists.models import ListItem
from rest_framework.authtoken.models import Token


class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True,
                                related_name="profile")

    # if user is just pledging they might not want an address
    # user has list
    # user has listitems

    def __str__(self):
        return self.user.username


class ShippingAddress(models.Model):

    full_name = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=80,
                            help_text="An easy to remember name like HOME")
    street_1 = models.CharField(max_length=100)
    street_2 = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=10)
    profile = models.ForeignKey(UserProfile, null=True, blank=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return "{} address for {}".format(self.name, self.profile)


class Pledge(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    profile = models.ForeignKey(UserProfile, related_name="pledges")
    item = models.ForeignKey(ListItem, related_name="pledges")
    amount = models.IntegerField()
    charge_id = models.CharField(max_length=60)


    @property
    def amount_value(self):
        return self.amount

    def __str__(self):
        return "{} for {} by {}".format(self.amount, self.item, self.profile)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        UserProfile.objects.create(user=instance)


