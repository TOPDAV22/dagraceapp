
from rest_framework.response import Response
from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404
from . serializers import productSerializers, CategorySerializers, SlideimgSerializers
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from django.contrib.auth import login
from rest_framework import permissions, generics
from knox.views import LoginView as KnoxLoginView 

from .models import Product, Slideimg, Category
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, AllowAny,  BasePermission
# Create your views here.


 


class ProductUserWritePermission(BasePermission):
    message = 'Editing articles is restricted to the author only.'

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return obj.owner == request.user


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticated]

    serializer_class = CategorySerializers


class ProductList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = productSerializers



            

class ProductDetail(generics.RetrieveUpdateDestroyAPIView, ProductUserWritePermission):
    permission_classes = [ProductUserWritePermission]
    queryset = Product.objects.all()
    serializer_class = productSerializers





class SliderViewSet(viewsets.ModelViewSet):
    queryset = Slideimg.objects.all()
    serializer_class = SlideimgSerializers
   




# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })













# this code as been move to another app users app

# class login(generics.GenericAPIView):
#     permission_classes = [AllowAny]
  
#     serializer_class = LoginSerializer

#     def post(self, request):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data
#         return Response({

#             "user":UserSerializer(user, context=self.get_serializer_context()).data,
#             "token": AuthToken.objects.create(user)[1]
#         })
        



# class LoginView(KnoxLoginView):
#     permission_classes = (permissions.AllowAny,)

#     def post(self, request, format=None):
#         serializer = AuthTokenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         login(request, user)
#         return super(LoginView, self).post(request, format=None) 



    

     