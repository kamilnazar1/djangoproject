from rest_framework import serializers
from .models import Medicine,Kalpana,Disease,Manufacturer

class KalpanaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kalpana
        field = ('name')

class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
        field = ('name')

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        field = ('name')

class MedicineSerializer(serializers.ModelSerializer):
    #pk = serializers.IntegerField(read_only=True)
    #title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    #code = serializers.CharField(style={'base_template': 'textarea.html'})
    #linenos = serializers.BooleanField(required=False)
    #language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    #style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
    kalpana = KalpanaSerializer(many = False)
    indications = DiseaseSerializer(many = True)
    class Meta:
    	model = Medicine
    	fields = ('id','name','kalpana','indications','properties','compositions','manufacturers','note')