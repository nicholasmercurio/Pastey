"""pastey URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from pastes.models import Paste
from django.conf.urls import url
from pastes import views
from pages.views import home_view, contact_view, about_view, paste_list_view, detail_view

display_info = {'queryset': Paste.objects.all()}
create_info = {'model': Paste}

urlpatterns = [
    path('home/', home_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('admin/', admin.site.urls, name='admin'),
    path('about/', about_view, name='about'),
    url(r'^signup/$', views.signup, name='signup'),
    path('paste_list/', paste_list_view, name='paste_list'),
    url(r'^$', home_view),
    url(r'^(?P<rand_url>\S{6})/$', detail_view, name='details'),
    path('accounts/', include('django.contrib.auth.urls')),
    #url(r'^(?P<rand_url>\S{10})/$', views.show, name='show'),
]
