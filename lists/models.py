
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum
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
    price = models.IntegerField()

    # @property
    # def percent_to_complete(self):
    #     total = []
    #     for pledge in self.pledges.all():
    #         total.append(pledge.amount_value)
    #     return sum(total) / float(self.price)

    def __str__(self):
        return "{} on {} for {}".format(self.name, self.list, self.user)


class Pledge(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    profile = models.ForeignKey(UserProfile, related_name="pledges")
    item = models.ForeignKey(ListItem, related_name="pledges")
    amount = models.IntegerField()
    stripe_token = models.CharField(max_length=40, null=True, blank=True)

    @property
    def amount_value(self):
        return self.amount

    def __str__(self):
        return "{} for {} by {}".format(self.amount, self.item, self.profile)
