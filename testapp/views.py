from .models import Medicine, Kalpana, Disease, Manufacturer
from testapp.serializers import MedicineSerializer, KalpanaSerializer, DiseaseSerializer, ManufacturerSerializer
from rest_framework import permissions
from rest_framework import generics

class MedicineList(generics.ListCreateAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer

class KalpanaList(generics.ListCreateAPIView):
    queryset = Kalpana.objects.all()
    serializer_class = KalpanaSerializer

class DiseaseList(generics.ListCreateAPIView):
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer
    
class ManufacturerList(generics.ListCreateAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer