from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from . models import Employee
from . serializers import EmployeeSerializers
# Create your views here.

class EmployeeCrudCBV(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers
