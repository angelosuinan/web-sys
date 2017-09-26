"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from controlcenter.views import controlcenter

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admin/dashboard/', controlcenter.urls),
    url(r'^', include('home.urls', namespace='home')),
    url(r'^inventory/', include('inventory.urls', namespace='inventory')),
    url(r'^dispersal/', include('dispersal.urls', namespace='dispersal')),
    url(r'^attendance/', include('attendance.urls', namespace='attendance')),
    url(r'^production/', include('production.urls', namespace='production')),
    url(r'^profile/', include('employee.urls', namespace='profile')),

    ]
