from django.conf.urls import url

from api import v1
from . import views

urlpatterns = [
    url(r'^v1/register$', v1.Register.as_view(), name='register'),
    url(r'^v1/punch$', v1.Punch.as_view(), name='punch'),
    url(r'^change$', views.Change.as_view(), name="change"),
    url(r'^$', views.Index.as_view(), name='index'),

]
