from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('employee_details/',views.EmployeeAPIView.as_view()),
    path('employee_details/<int:pk>/',views.EmployeeAPIView.as_view()),
]
