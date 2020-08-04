from django.shortcuts import render

from .models import Appointment
from .serializers import AppointmentSerializer

from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
# Create your views here.

class AppointmentList(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    #queryset = Appointment.objects.filter(owner__exact=request.user.username)
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def list(self, request):
        queryset = Appointment.objects.filter(owner__exact=request.user.id).order_by('date')
        serializer = AppointmentSerializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

from .permissions import IsOwnerOrReadOnly

class AppointmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, 
                          IsOwnerOrReadOnly]


