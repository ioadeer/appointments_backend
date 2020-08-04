from django.test import TestCase

# Create your tests here.

from appointments.models import Appointment
from django.contrib.auth import get_user_model

import datetime

class AppointmentModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user_class = get_user_model()
        test_user = test_user_class.objects.create(username="test_user")
        date = datetime.date.today() + datetime.timedelta(days=1)
        Appointment.objects.create(name="Dentist appointment",
                                   date = date,
                                   location="Dental clinic",
                                   owner=test_user,
                                   start="13:00:00",
                                   end="14:00:00")
    
    def test_date_not_in_past(self):
        """ 
        This test should check that the appointment date is not in the past
        It can have date for today
        """
        today_date = datetime.date.today() 
        appointment = Appointment.objects.get(pk = 1)
        appointment_date = appointment.date
        self.assertGreaterEqual(appointment_date, today_date)
    
    def test_end_time_greater_than_start_time(self):
        """
        The appointment end should happend after the appointment start
        """
        appointment = Appointment.objects.get(pk=1)
        start_time = appointment.start
        end_time = appointment.end
        self.assertGreater(end_time, start_time)

    def test_owner_should_be_custom_user(self):
        """
        Base user has been extened to Custom user. Check object's user is
        custom user.
        """
        User = get_user_model()
        appointment = Appointment.objects.get(pk = 1)
        appointment_owner = appointment.owner
        self.assertIsInstance(appointment_owner, User)

