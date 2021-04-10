from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile


#Serializer class it is used for translating django models into useful other formats like here is json

#Userserializer for registration
class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=65, min_length=6, write_only=True)
    email=serializers.EmailField(max_length=255, min_length=4)
    first_name=serializers.CharField(max_length=255,min_length=2)
    last_name=serializers.CharField(max_length=255,min_length=2)
    


    class Meta:
        model=User
        fields=('username','first_name', 'last_name', 'email','password') #Creating fields

    #Checking validation if the email is not repeat    

    def validate(self,attrs):

            email=attrs.get('email', '')
            if User.objects.filter(email=attrs['email']).exists():
                raise serializers.ValidationError(
            {'email', ('Email is already in use')})


            return super().validate(attrs)
    # Creating succefully 

    def create(self, validated_data):
            return User.objects.create_user(**validated_data)



#Login serializer for Login
class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=65, min_length=8, write_only=True)#password field
    username = serializers.CharField(max_length=255, min_length=2)#username field

    class Meta:
        model = User
        fields = ['username', 'password']#creating fields for user


class ProfileSerializer(serializers.ModelSerializer):
    

    class Meta:

        model=Profile

        fields=['university_name','course_name','id']












        




