from django.contrib import admin
from .models import Kalpana
from .models import Medicine
from .models import Manufacturer
from .models import Disease
# Register your models here.

admin.site.register(Kalpana)
admin.site.register(Medicine)
admin.site.register(Manufacturer)
admin.site.register(Disease)
