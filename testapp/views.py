from django.http import HttpResponse
from django.http import JsonResponse
from .models import Kalpana,Medicine

from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from testapp.serializers import MedicineSerializer

"""
def index(request):
    response=Kalpana.objects.all()
    #return HttpResponse("Hello, world. You're at the polls index.")
    return JsonResponse(response,safe=False)
"""
class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def medicine_list(request):
	medicines = Medicine.objects.all()
	serializer = MedicineSerializer(medicines, many = True)
	return JsonResponse(serializer.data, safe = False)