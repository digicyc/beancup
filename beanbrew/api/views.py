from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

from beanbrew.api.serializers import BrewSerializer
from beanbrew.models import Brew

class Brews(APIView):
    def get(self, request):
        brews = Brew.objects.all()
        serializer = BrewSerializer(brews, many=True)

