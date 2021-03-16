from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, get_object_or_404

from company.models import CompanyModel
from company.serializers import CompanySerializer
from employee.serializer import EmployeeSerializer


class CompanyListCreateView(ListCreateAPIView):
    serializer_class = CompanySerializer

    def get_queryset(self, **kwargs):
        queryset = CompanyModel.objects.all()
        city = self.request.query_params.get('city')
        if city:
            queryset = queryset.filter(city__iexact='lviv')

        return queryset

class CompanyReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = CompanyModel.objects.all()
    serializer_class = CompanySerializer


class EmployeeCreate(CreateAPIView):
    serializer_class = EmployeeSerializer

    def perform_create(self, serializer):
        company_id = self.kwargs.get('pk')
        company = get_object_or_404(CompanyModel, pk=company_id)
        serializer.save(company=company)

