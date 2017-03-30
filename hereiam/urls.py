"""intern URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from app import views as app_views
 
urlpatterns = [
	url(r'^admin/', admin.site.urls),
    url(r'^$', app_views.home, name='home'),
    url(r'^home/$', app_views.home, name='home'),   
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', app_views.logout_page, name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^register/$', app_views.register),
    url(r'^register/success/$', app_views.register_success),
]
