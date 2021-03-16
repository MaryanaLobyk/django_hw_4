from rest_framework.serializers import ModelSerializer

from company.models import CompanyModel
from employee.serializer import EmployeeSerializer


class CompanySerializer(ModelSerializer):
    employee = EmployeeSerializer(many=True, required=True)

    class Meta:
        model = CompanyModel
        fields = ['id', 'name', 'country', 'city', 'employee']
