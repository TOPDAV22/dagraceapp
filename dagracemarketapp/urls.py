from django.urls import path, include
from .views import ProductVeiw 
from .views import SliderViewSet, CategoryViewSet
from rest_framework.routers import DefaultRouter


from dagracemarketapp import views
from .views import RegisterAPI, login
from knox import views as knox_views

from django.urls import path


   


router = DefaultRouter()
router.register('category', CategoryViewSet),
router.register('slideimg', SliderViewSet),
router.register('product', ProductVeiw, basename = 'product'), 




 



urlpatterns =[
    path('api/', include(router.urls)),
   

] 