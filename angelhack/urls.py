"""angelhack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from locate.views import showZoneDetail,showZonewoTDetail,recommend
from locate.api.views import ZoneList,ZoneCreate
from django.conf import settings

from django.conf.urls.static import static

from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', showZoneDetail, name='zone'),
    url(r'^recommend/(?P<lat>[\d]+)/(?P<lng>[\d]+)$', recommend, name='rhjson'),
    url(r'^zoned/$', showZonewoTDetail, name='zoned'),
 	
 ]

urlpatterns1=[

url(r'^api/zone/$', ZoneList.as_view(), name='ZoneList-list'),
	url(r'^api/zone/create$', ZoneCreate.as_view(), name='ZoneCreate-list'),


 ]

urlpatterns1 = format_suffix_patterns(urlpatterns1)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

