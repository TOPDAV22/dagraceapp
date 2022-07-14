from django.urls import path, include
from .views import SliderViewSet, CategoryViewSet
from rest_framework.routers import DefaultRouter
from dagracemarketapp import views
from .views import RegisterAPI
from knox import views as knox_views
from django.urls import path
from .views import ProductList,ProductDetail


   


router = DefaultRouter()
router.register('category', CategoryViewSet),
router.register('slideimg', SliderViewSet),
     




 



urlpatterns =[
    path('api/', include(router.urls)),
    path('product/', ProductList.as_view(), name='productList'),
   path('product/<int:pk>/', ProductDetail.as_view(), name='ProductDetail'),
    
   

] 