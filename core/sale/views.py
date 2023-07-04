from django.shortcuts import render
from .models import Sale
from rest_framework import status
from rest_framework.views import APIView
from .serializer import SaleSerializer
from rest_framework.response import Response
import requests

# Create your views here.
class SaleListApiView(APIView):

    def get(self, request):
        sales = Sale.objects.all()
        serializer = SaleSerializer(sales, many=True)
        data = []
        for sale in serializer.data:
            session = requests.Session()
            user = session.get('http://127.0.0.1:8001/api/admin/users/' + str(sale['user']) + '/').json()
            product = session.get('http://127.0.0.1:8001/api/products/' + str(sale['product']) + '/').json()
            obj = {
                "id" : sale['id'],
                "user": user,
                "product": product,
                "quantity": sale['quantity'],
                "total": sale['total'],
                "created_at": sale['created_at'],
                "updated_at": sale['updated_at']
            }
            data.append(obj)
        print(data)
        return render(request, 'sale.html', {'sales': data})
        

    def post(self, request):
        serializer = SaleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SaleDetailApiView(APIView):
    
        def get_object(self, id):
            try:
                sale = Sale.objects.get(id=id)
                session = requests.Session()
                user = session.get('http://127.0.0.1:8001/api/admin/users/' + str(sale.user) + '/').json()
              
                print('---------------------')
                print(sale.product)
                product = session.get('http://127.0.0.1:8001/api/products/' + str(sale.product) + '/')
           

                obj = {
                    "id" : sale.id,
                    "user": user,
                    "product": product.json(),
                    "quantity": sale.quantity,
                    "total": sale.total,
                    "created_at": sale.created_at,
                    "updated_at": sale.updated_at
                }
                
                return obj
            except Sale.DoesNotExist:
                raise Http404
    
        def get(self, request, id):
            sale = self.get_object(id)
            serializer = SaleSerializer(sale)
            return Response(sale)
            #return render(request, 'sale.html', {'sale': sale}')
    
        def put(self, request, id):
            sale = self.get_object(id)
            serializer = SaleSerializer(sale, data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        def delete(self, request, id):
            sale = self.get_object(id)
            sale.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

def sale_view(request):
    sales = Sale.objects.all()
    return render(request, 'sale.html', {'sales': sales})