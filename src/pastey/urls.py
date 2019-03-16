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
from pages.views import home_view, edit_view, paste_list_view, detail_view, delete_user, delete_confirm_view, share_view

create_info = {'model': Paste}

urlpatterns = [
    url(r'^$', home_view),
    path('home/', home_view, name='home'),
    path('admin/', admin.site.urls, name='admin'),
    path('delete/', delete_user, name='delete'),
    url(r'^signup/$', views.signup, name='signup'),
    path('paste_list/', paste_list_view, name='paste_list'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('delete_confirm_view/', delete_confirm_view, name="delete_confirm_view" ),
    path('<str:custom_uuid>/share', share_view, name='share_paste'),
    path('<str:custom_uuid>/edit', edit_view, name='edit_paste'),
    path('<str:custom_uuid>/', detail_view, name='detail'),
]
