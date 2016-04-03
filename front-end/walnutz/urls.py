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
    url(r'^backend/profile/(?P<profile_id>\d+)$', backend),
    url(r'^profile/(?P<profile_id>\d+)/$', profile),
    url(r'^protocol/(?P<profile_id>\d+)/$', protocol),
    url(r'^support/(?P<profile_id>\d+)/$', support),
    url(r'^behavior/(?P<profile_id>\d+)/$', behavior),
    url(r'^update/(?P<profile_id>\d+)/', update),
    url(r'^signin/$', login),

]
