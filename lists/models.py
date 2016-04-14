
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from userprofiles.models import UserProfile


class List(models.Model):
    name = models.CharField(max_length=150)
    user = models.ForeignKey(User, related_name="lists")
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    modified_at = models.DateTimeField(auto_now=True)
    expiration_date = models.DateField()
    expired = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    @property
    def check_expired(self):
        return timezone.now().date() > self.expiration_date



class ListItem(models.Model):
    name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    modified_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='item_picture/', null=True,
                              blank=True,
                              default='item_picture/default.jpg')
    list = models.ForeignKey(List, related_name="items")
    user = models.ForeignKey(User, related_name="items")
    amazon_link = models.URLField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return "{} on {} for {}".format(self.name, self.list, self.user)


class Pledge(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    profile = models.ForeignKey(UserProfile, related_name="pledges")
    item = models.ForeignKey(ListItem, related_name="pledges")
    amount = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return "{} for {}".format(self.amount, self.item.name)
