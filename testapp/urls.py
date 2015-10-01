from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.medicine_list, name='medicine_list'),
]
