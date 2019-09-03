from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from rest_framework.documentation import include_docs_urls

API_TITLE = 'Social Boost API doc'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^my/posts/', include('posts.urls')),
    url(r'^my/likes/', include('activity.urls')),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^docs/', include_docs_urls(title=API_TITLE)),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
