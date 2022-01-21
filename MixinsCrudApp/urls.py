# from django.urls import path
from django.conf.urls import url
from . import views
from django.urls import include
from rest_framework import routers

router = routers.SimpleRouter()
router.register('employee_details', views.EmployeeViewSet)


urlpatterns = [
    url(r'', include(router.urls)),
]
