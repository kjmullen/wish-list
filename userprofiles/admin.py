from django.contrib import admin
from userprofiles.models import UserProfile, ShippingAddress, Pledge


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')


@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'full_name', 'street_1', 'street_2', 'city',
                    'state', 'zip_code')


@admin.register(Pledge)
class PledgeAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'item', 'amount')
