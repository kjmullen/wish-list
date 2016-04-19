from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum
from django.utils import timezone


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
    user = models.ForeignKey(User, related_name="items", null=True)
    amazon_link = models.URLField()
    price = models.IntegerField()

    @property
    def fully_pledged(self):
        total = self.pledges.aggregate(Sum('amount'))
        return self.price > total['amount__sum']

    @property
    def percent_to_complete(self):
        total = self.pledges.aggregate(Sum('amount'))
        return total['amount__sum'] / self.price

    def __str__(self):
        return "{} item on {} for {}".format(self.name, self.list, self.user)
