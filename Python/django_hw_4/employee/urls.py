from django.urls import path

from .views import EmployeeCreateListView, EmployeeReadUpdateDeleteView

urlpatterns = [
    path('', EmployeeCreateListView.as_view()),
    path('<int:pk>', EmployeeReadUpdateDeleteView.as_view())
]
