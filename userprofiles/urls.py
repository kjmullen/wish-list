from django.conf.urls import url
from userprofiles.views import ListUserProfile, ListCreateUser, DetailUser, \
    DetailUserProfile, ListPledge, \
    ListCreateShippingAddress, DetailUpdateDeleteShippingAddress, CreateCharge

urlpatterns = [
    url(r'^profiles/$', ListUserProfile.as_view(), name="list_user_profile"),
    url(r"^profiles/(?P<pk>\d+)/$", DetailUserProfile.as_view(),
                                                name="detail_user_profile"),
    url(r'^$', ListCreateUser.as_view(), name="list_create_user"),
    url(r"^(?P<pk>\d+)/$", DetailUser.as_view(), name="detail_user"),
    url(r'^profiles/addresses/$', ListCreateShippingAddress.as_view(),
                                        name="list_create_shipping_address"),
    url(r'^profiles/addresses/(?P<pk>\d+)/$',
        DetailUpdateDeleteShippingAddress.as_view(),
        name="detail_update_delete_shipping_address"),
    url(r'^pledges/$', ListPledge.as_view(), name="list_pledge"),
    url(r'^charges/create/$', CreateCharge.as_view(), name="create_charge"),

]