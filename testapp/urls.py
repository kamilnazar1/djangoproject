from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^medicines/$', views.MedicineList.as_view()),
    url(r'^diseases/$', views.DiseaseList.as_view()),
    url(r'^manufacturers/$', views.ManufacturerList.as_view()),
    url(r'^kalpana/$', views.KalpanaList.as_view()),
]
