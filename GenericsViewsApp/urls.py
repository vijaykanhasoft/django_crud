from django.urls import path
from django.conf.urls import url
from . import views


#Generics Crud Demo using five urls
urlpatterns = [
    url(r'^employee_details/$',views.EmployeeListView.as_view(),name="employee_listview"),
    url(r'^create_employee/',views.EmployeeCreateAPIView.as_view(), name="create_employee"),
    url(r'^employee_details/(?P<pk>\d+)/$',views.EmployeeRetrieveAPIView.as_view(), name="retrive_employee"),
    url(r'^update_employee/(?P<pk>\d+)/$',views.EmployeeUpdateAPIView.as_view(), name="update_employee"),
    url(r'^delete_employee/(?P<pk>\d+)/$',views.EmployeeDestroyAPIView.as_view(), name="delete_employee"),

]
