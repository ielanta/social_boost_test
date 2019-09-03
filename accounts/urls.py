from django.conf.urls import url
from accounts.views import AccountList, AccountCreate


urlpatterns = [
    url(r'^register/', AccountCreate.as_view(), name='account-registration'),
    url(r'^$', AccountList.as_view(), name='account-list'),
]
