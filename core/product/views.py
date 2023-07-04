from django.shortcuts import render
from rest_framework.views import APIView
import requests
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status

class ProductListApiView(APIView):
    def get(self, request):
        session = requests.Session()
        response = session.get(settings.SITE_URL + 'api/products/')
        custom_products = []

        for product in response.json():
            product_details = session.get(settings.SITE_URL + 'api/products/' + str(product['id']) + '/').json()
            price = session.get(settings.SITE_URL + 'api/products/' + str(product['id']) + '/price/').json()

            product['price'] = price
            product['images'] = product_details['images']

            if product_details['structure'] != 'child':
                if product_details['children']:
                    product['price'] = session.get(product_details['children'][0]['price']).json()
                   
              
                custom_products.append(product)

        return Response(custom_products, status=status.HTTP_200_OK)

class ProductDetailApiView(APIView):
    def get_object(self, product_id):
        session = requests.Session()
        response = session.get(settings.SITE_URL + 'api/products/' + str(product_id) + '/').json()
        price = session.get(settings.SITE_URL + 'api/products/' + str(product_id) + '/price/').json()
        availability = session.get(settings.SITE_URL + 'api/products/' + str(product_id) + '/availability/').json()
        stockrecords = session.get(settings.SITE_URL + 'api/products/' + str(product_id) + '/stockrecords/').json()

        if response['structure'] != 'child':
            if response['children']:
                price = session.get(response['children'][0]['price']).json()
             
        response['availability'] = availability
        response['price'] = price
        response['stockrecords'] = stockrecords
        return response

    def get(self, request, product_id):
        product_instance = self.get_object(product_id)
        if not product_instance:
            return Response(
                {"res": "Object with client id does not exits"},
                status = status.HTTP_400_BAD_REQUEST
            )
        return Response(
                product_instance,
                status = status.HTTP_200_OK
            )

