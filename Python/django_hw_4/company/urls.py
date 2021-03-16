from django.urls import path

from company.views import CompanyListCreateView, CompanyReadUpdateDeleteView, EmployeeCreate

urlpatterns = [
    path('', CompanyListCreateView.as_view()),
    path('/<int:pk>', CompanyReadUpdateDeleteView.as_view()),
    path('/<int:pk>/employee', EmployeeCreate.as_view())
]
