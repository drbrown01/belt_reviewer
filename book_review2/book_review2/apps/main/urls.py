from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^index/', views.index),
    url(r'^home/$', views.home),
    url(r'^home/success/$', views.success),
    url(r'^success/home/$', views.home),
    url(r'^success/$', views.success),
    url(r'^reviews/$', views.reviews),
]
