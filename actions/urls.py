from django.conf.urls import url
from actions.views import LikeList, DeleteLike


urlpatterns = [
    url(r'^$', LikeList.as_view(), name='my-like-list'),
    url(r'^(?P<pk>\d+)/$', DeleteLike.as_view(), name='delete-my-like'),
]
