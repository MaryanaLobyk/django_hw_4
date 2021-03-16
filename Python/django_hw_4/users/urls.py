from django.urls import path

from users.views import UserListCreateView, CompanyCreate, UserReadUpdateDeleteView

urlpatterns = [
    path('', UserListCreateView.as_view()),
    path('/<int:pk>/companies', CompanyCreate.as_view()),
    path('/<int:pk>', UserReadUpdateDeleteView.as_view())
]
