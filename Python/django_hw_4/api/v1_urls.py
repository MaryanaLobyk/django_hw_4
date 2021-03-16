from django.urls import path, include

urlpatterns = [
    path('/users', include('users.urls')),
    path('/companies', include('company.urls')),
    path('/employee', include('employee.urls')),
]
