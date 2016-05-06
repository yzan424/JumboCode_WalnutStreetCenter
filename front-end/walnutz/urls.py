"""walnutz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from nutzserver.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^backend/profile/(?P<profile_id>\d+)/(?P<data>\w+)/$', backend),
    url(r'^profile/(?P<profile_id>\d+)/$', profile, {'edit': False}),
    url(r'^protocol/(?P<profile_id>\d+)/$', protocol, {'edit': False}),
    url(r'^support/(?P<profile_id>\d+)/$', support, {'edit': False}),
    url(r'^behavior/(?P<profile_id>\d+)/$', behavior, {'edit': False}),
    url(r'^edit/(?P<page>\w+)/(?P<profile_id>\d+)/$', edit),
    url(r'^new/$', new),
    url(r'^signin/$', login),
    url(r'^logout/$', logout_page),
    url(r'^search/$', search),
    url(r'^efs/(?P<profile_id>\d+)/$', efs_gen),
    url(r'^$', index),
]
