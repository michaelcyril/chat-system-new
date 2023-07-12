from django.db import IntegrityError
from django.shortcuts import render,redirect
from .models import *
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.contrib.auth import login,logout,authenticate
from .serializers import *
from rest_framework.authtoken.models import Token

# Create your views here.
# the builtin function login(request,user) is used on web based but for the case of the
# api we use authenticate and generating the token from rest_framework.authtoken



@api_view(['POST'])
@permission_classes({AllowAny})

def login_user(request):
    username=request.data['username']
    password=request.data['password']
    user=authenticate(username=username,password=password)
    # if user:
    print(user)
    if user is not None:
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        user_id = User.objects.values('id', 'username', 'email').get(id=user.id)
        # tok = [entry for entry in token]
        print(user_id)
        print(token.key)
        return Response({'sms': 'success','token': token.key, 'user': user_id})
    return Response({'sms':'failed'})

# return render(request, 'login.html')

# {
# "username":"mike",
# "password":"123"
# }

@api_view(['POST'])
@permission_classes({AllowAny})

def logout_user(request):
    logout(request)
    return Response({'message': 'successfull logout'})

@api_view(['POST'])
@permission_classes({AllowAny})

def Register_Users(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        print('hey i reach here')
        account = serializer.save()
        account.is_active = True
        account.save()
        return Response({'sms':'success'})

    data = serializer.errors


    return Response(data)


# {
#     "first_name":"Michael",
#     "last_name":"Cyril",
#     "email":"michaelcyril71@gmail.com",
#     "password":"123",
#     "username":"mike"
# }

@api_view(['GET'])
@permission_classes([AllowAny])

def AllUser(request):
    user = User.objects.values('id', 'username', 'email').all()
    return Response(user)