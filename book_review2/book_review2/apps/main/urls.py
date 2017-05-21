from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^index/', views.index, name='index'),
    url(r'^home/$', views.home),
    url(r'^home/success/$', views.success),
    url(r'^success/home/$', views.home),
    url(r'^success/$', views.success, name='success'),
    url(r'^reviews/$', views.reviews, name='reviews'),
    url(r'^account/$', views.account, name='account'),
    url(r'^logout/$', views.logout, name='account'),
]
