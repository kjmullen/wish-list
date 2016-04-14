from django.conf.urls import url
from userprofiles.views import ListUserProfile, ListUser, DetailUser, \
    DetailUserProfile, ListCreatePledge

urlpatterns = [
    url(r'^profiles/$', ListUserProfile.as_view(), name="list_user_profile"),
    url(r"^profiles/(?P<pk>\d+)/$", DetailUserProfile.as_view(),
                                                name="detail_user_profile"),
    url(r'^$', ListUser.as_view(), name="list_user"),
    url(r"^(?P<pk>\d+)/$", DetailUser.as_view(), name="detail_user"),
    url(r'^pledges/$', ListCreatePledge.as_view(), name="list_pledge"),

]