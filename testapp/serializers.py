from rest_framework import serializers
from .models import Medicine,Kalpana,Disease,Manufacturer

class KalpanaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Kalpana
        field = ('id','name')

class DiseaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Disease
        field = ('id','name')

class ManufacturerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manufacturer
        field = ('id','name')

class MedicineSerializer(serializers.ModelSerializer):

    class Meta:
    	model = Medicine
    	fields = ('id','name','kalpana','indications','properties','compositions','manufacturers','note')