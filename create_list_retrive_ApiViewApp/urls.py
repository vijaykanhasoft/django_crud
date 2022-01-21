from django.urls import path
from django.conf.urls import url
from . import views


#Generics Crud Demo using two urls
urlpatterns = [
    url(r'^employee_details/$',views.EmployeeListCreateAPIView.as_view(),name="employee_list_and_create_view"),
    url(r'^employee_details/(?P<pk>\d+)/$',views.EmployeeRetrieveUpdateDestroyAPIView.as_view(), name="retrive_employee"),
   

]
