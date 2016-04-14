from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from rest_framework.authtoken.models import Token


class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True,
                                related_name="profile")

    # if user is just pledging they might not want an address
    # user has list
    # user has listitems
    # profile has pledges

    def __str__(self):
        return self.user.username


class ShippingAddress(models.Model):

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


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        UserProfile.objects.create(user=instance)
