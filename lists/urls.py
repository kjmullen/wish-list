from django.conf.urls import url
from lists.views import DetailUpdateDeleteList, ListCreateListItem, \
    ListCreateList, DetailUpdateDeleteListItem

urlpatterns = [
    url(r'^$', ListCreateList.as_view(), name="list_list"),
    url(r'^(?P<pk>\d+)/$', DetailUpdateDeleteList.as_view(), name="detail_list"),
    url(r'^items/$', ListCreateListItem.as_view(), name="list_list_item"),
    url(r'^items/(?P<pk>\d+)$', DetailUpdateDeleteListItem.as_view(),
        name="detail_list_item"),
]