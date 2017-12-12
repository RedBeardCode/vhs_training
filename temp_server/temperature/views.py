from django.http import HttpResponse
from django.views import View
from time import sleep
# Create your views here.
from temperature.tasks import get_last_temperature, LAST_TEMPERATURE, get_last_pattern


class TemperatureView(View):

    def get(self, request):
        return HttpResponse(str(get_last_temperature()))


class PatternView(View):

    def get(self, request):
        return HttpResponse(get_last_pattern())

