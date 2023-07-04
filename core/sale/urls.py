from django.urls import path
from .views import SaleListApiView, SaleDetailApiView

urlpatterns = [
    path('', SaleListApiView.as_view(), name='sale_list'),
    path('<int:id>/', SaleDetailApiView.as_view(), name='sale_detail'),
]