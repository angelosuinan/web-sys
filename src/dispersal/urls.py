from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^add$', views.Add.as_view(), name='add'),
    url(r'^change$', views.Change.as_view(), name='change'),
    url(r'^charts$', views.Chart.as_view(), name='chart'),
    url(r'^stocks$', views.Stock.as_view(), name='stock'),
]
