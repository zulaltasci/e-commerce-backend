from django.shortcuts import render
from rest_framework.views import APIView
import requests
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class BasketDetailApiView(APIView):
    def get_object(self, id):
        print(settings.SITE_URL + 'api/basket/')
        session = requests.Session()
        response = session.get(settings.SITE_URL + 'api/basket/').json()
        
        return response
    
    def get(self, request, id):
        product_instance = self.get_object(id)
       
        if not product_instance:
            return Response(
                {"res": "Object with id does not exits"},
                status = status.HTTP_400_BAD_REQUEST
            )
        return Response(
                product_instance,
                status = status.HTTP_200_OK
            )