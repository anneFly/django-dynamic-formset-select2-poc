from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^select2/', include('django_select2.urls')),
    url(r'^', include('poc.app.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
