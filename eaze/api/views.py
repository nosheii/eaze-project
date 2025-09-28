from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def hello_world(request):
    return Response({"message": "Hello, world!!!!!!!"})

#http://localhost:8000/api/oppdaterNavn/
@api_view(['POST'])
def oppdaterNavn(request):
    print("HEI JEG KJØRER I PYTHON")
    return Response({"message": "Navn oppdatert!"})
