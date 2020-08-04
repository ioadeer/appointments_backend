from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions

# Create your views here.

from .models import CustomUser
from .serializers import UserSerializer

class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
