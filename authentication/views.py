from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import UserSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.contrib.auth import authenticate
import jwt
import requests
import json


# Create your views here.


#Registration View which uses a Userserializer class and post method is used to fill all the parameters(first
# name, lastname,email,password and username) which later return a successful response
class RegisterView(GenericAPIView):
    serializer_class=UserSerializer #Serializer

    def post(self,request):
        serializer=UserSerializer(data=request.data)


        if serializer.is_valid():
            serializer.save()#saving the detials
            return Response(serializer.data, status=status.HTTP_201_CREATED)#on successful the respond is 201 else

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  #on failure response is 400(error)


#LoginView uses Login Serializer class and checking the login authentication
class LoginView(GenericAPIView):

    serializer_class=LoginSerializer
    #post method for filling an getting the required data
    def post(self,request):
        data=request.data
        username=data.get('username','')#username field
        password=data.get('password', '')#password field

        #the below code is used for tracking the ip address of the user who open the app 

        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        
        

        
        
        #Authenticate process for the user
        
        user=authenticate(request,username=username,password=password)

        
        #if we found the user then get the token and its user id

        if user:
            auth_token=jwt.encode(
                {'username': user.username}, settings.JWT_SECRET_KEY
            )##Token process here username is the payload, algo is HS256, type is JWT and the secret key is in settings file 

            id=user.id#id 

            #Sending the webhook to the the given url in which ip address of the request user and its id is stored

            webhook_url='https://encrusxqoan0b.x.pipedream.net/'
            data1={
                'user': id, 'ip': ip
            }
            r=requests.post(webhook_url,data=json.dumps(data1), headers={ 'Content-Type': 'application/json'})
            

            

            serializer=UserSerializer(user)

            data= { 'token': auth_token} #it return token in response 

            return Response(data, status=status.HTTP_200_OK) #if success returns  status 200 else 

        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)    #if fail it returns invalid creds




