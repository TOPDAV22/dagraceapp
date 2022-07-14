
from rest_framework import serializers
from .models import Product, Category,Slideimg
from django.contrib.auth.models import User
from django.contrib.auth import authenticate



class productSerializers(serializers.ModelSerializer):
  
    class  Meta:
        model = Product
        fields = '__all__'
        read_only_fields =['user']


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
   

class SlideimgSerializers(serializers.ModelSerializer):
    class Meta:
        model = Slideimg
        fields = '__all__'




# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')



# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}
        

    def create(self, validated_data):
        
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user







        # done on userApp

# class LoginSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField()

#     def validate(self, data):
#         user = authenticate(**data)
#         if user and user.is_active:
#             return user
#             raise serializers.ValidationError('incorrent credential passed.')


# Register Serializer
# class RegisterSerializer(serializers.ModelSerializer):
#        class Meta:
#         model = User
#         fields = ('id', 'first_name', 'last_name','email','username','password') 
#         extra_kwargs = {'password': {'write_only': True}}
        
#         def validate(self, args):
#             email = args.get('email',None)
#             username = args.get('username', None)
#             if User.objects.filter(email=email).exists():
#                 raise serializers.ValidationError({'email':('email.already exists')})
#             if User.objects.filter(username=username).exists():
#                 raise serializers.ValidationError({'username':('username.already exists')})

#             return super().validate(args)
#         def create(self, validate_data):
#             user= User.objects.create_user(**validate_data)
#             return user 

        





# Register Serializer

# from studygy
