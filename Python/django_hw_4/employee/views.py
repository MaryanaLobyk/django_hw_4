from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
# Create your views here.
from employee.models import EmployeeModel
from employee.serializer import EmployeeSerializer


class EmployeeCreateListView(ListCreateAPIView):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer
