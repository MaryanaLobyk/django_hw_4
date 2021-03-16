from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

from company.serializers import CompanySerializer

UserModel = get_user_model()


class UserSerializer(ModelSerializer):
    company = CompanySerializer(many=True, required=True)

    class Meta:
        model = UserModel
        fields = ['id', 'email', 'password', 'company']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = UserModel(**validated_data)
        user.set_password(password)
        user.save()
        return user
