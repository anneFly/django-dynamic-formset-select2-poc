from django.conf.urls import include, url
from django.contrib import admin

from poc.app.views import BookView

urlpatterns = [
    url(r'^select2/', include('django_select2.urls')),
    url(r'^$', BookView.as_view(), name='home'),

    url(r'^admin/', include(admin.site.urls)),
]
