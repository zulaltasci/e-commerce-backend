from django.urls import path
from .views import (BasketDetailApiView)

urlpatterns = [
    path('<int:id>/', BasketDetailApiView.as_view(), name='basket-detail')
]