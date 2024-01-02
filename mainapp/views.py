from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes, permission_classes

class RegistrationAPIView(APIView):
    def post(self, request, *args, **kwargs):
        phone_number = request.data.get('phone_number')
        password = request.data.get('password')
        if User.objects.filter(username=phone_number).exists():
            return Response({'error': 'User with this phone number already exists'}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create_user(username=phone_number, password=password)
        if user is not None:
            login(request, user)
            return Response({'message': 'Registration successful'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Failed to create user'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class LoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        phone_number = request.data.get('phone_number')
        password = request.data.get('password')

        user = authenticate(request, username=phone_number, password=password)

        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated]) 
class ProfileAPIView(APIView):
    def get(self, request, *args, **kwargs):
        user = request.user
        return Response({'username': user.username, 'phone_number': user.username}, status=status.HTTP_200_OK)


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class LogoutAPIView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            request.auth.delete()
        except (AttributeError, Token.DoesNotExist):
            pass
        logout(request)
        return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)