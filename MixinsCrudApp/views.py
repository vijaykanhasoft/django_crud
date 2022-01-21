from django.shortcuts import render
from ViewSetApp . models import Employee
from . serializers import EmployeeSerializers
from rest_framework import mixins, viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status


class EmployeeViewSet(mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,mixins.ListModelMixin,viewsets.GenericViewSet):
    serializer_class = EmployeeSerializers
    queryset = Employee.objects.all()

    def get(self, request, *args, **kwargs):
        emp = get_object_or_404(self.queryset, id=self.kwargs.get("pk"))
        serializer = EmployeeSerializers(emp)
        return Response(serializer.data)
    
    def patch(self, request, *args, **kwargs):
        emp = get_object_or_404(self.queryset, id=self.kwargs.get("pk"))
        serializer = EmployeeSerializers(emp, data=request.data, partial=True)
        if serializer.is_valid():
            emp = serializer.save()
            return Response(EmployeeSerializers(emp).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
