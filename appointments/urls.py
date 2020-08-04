from django.urls import path
from .views import AppointmentList, AppointmentDetail

urlpatterns =[
    path('appointments/', AppointmentList.as_view(), name='appointments-list'),
    path('appointments/<int:pk>', AppointmentDetail.as_view(), name='appointments-detail'),
]
