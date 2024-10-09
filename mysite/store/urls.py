from .views import ProductViewSet
from django.urls import path

urlpatterns = [
                  path('', ProductViewSet.as_view({'get': 'list', 'post': 'create'
                                                   }, name='product_list')),
                  path('<int:pk>/',ProductViewSet.as_view({'get': 'retrieve',
                                                           'put': 'update',
                                                           'delete': 'destroy'}))
              ]
