from rest_framework import viewsets
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status

from account import models
from account import serializers

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    Task 1: User View for CRUD operation
    """

    queryset = models.User.objects.all()
    serializer_class = serializers.CreateUserSerializer
    lookup_field = 'username'

    def create(self, request, *args, **kwargs):
        """
        :param request:username, password, email
        :param args:
        :param kwargs:
        :return:
        """
        username = request.data.get('username')
        email = request.data.get('email')
        if models.User.objects.filter(username=username) or models.User.objects.filter(email=email):
            return Response({'message': 'User already registered'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = serializers.CreateUserSerializer(request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'User created Successfully'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Some error occcurred'}, status=status.HTTP_400_BAD_REQUEST)


class Authenticate(views.APIView):
    """
    Task 2 : View to authenticate password and username
    """

    def post(self, request, *args, **kwargs):
        """
        POST request handler
        :param request:username, password
        :param args:
        :param kwargs:
        :return:
        """
        username = request.data.get('username')
        password = request.data.get('password')
        if models.User.objects.filter(username = username) and models.User.objects.filter(password= password):
            return Response({'message':'Passwords Match'}, status=status.HTTP_200_OK)
        else:
            return Response({'message':'Passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)


