from django.conf.urls import url
from posts.views import PostList


urlpatterns = [
    url(r'^$', PostList.as_view(), name='post-list'),
]
