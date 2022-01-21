from django.shortcuts import render
from ViewSetApp . models import Employee
from . serializers import EmployeeSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class EmployeeAPIView(APIView):
    def get(self, request,*args, **kwargs):
        id=self.kwargs.get("pk")
        emp =Employee.objects.all()
        serializer = EmployeeSerializers(emp, many=True)
        if id is not None:
            try:
                emp =Employee.objects.get(id=id)
                serializer = EmployeeSerializers(emp)
                return Response(serializer.data)
            except Employee.DoesNotExist:
                return Response(status= status.HTTP_404_NOT_FOUND)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer_obj = EmployeeSerializers(data=request.data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response({"msg":'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer_obj.errors, status = status.HTTP_400_BAD_REQUEST)

    def put(self, request,*args, **kwargs):
        id=self.kwargs.get("pk")
        try:
            emp = Employee.objects.get(id=id)
            empserializer = EmployeeSerializers(emp, data=request.data)
            if empserializer.is_valid():
                empserializer.save()
                return Response(empserializer.data, status=status.HTTP_200_OK)
            return Response(empserializer.errors, status= status.HTTP_400_BAD_REQUEST)
        except Employee.DoesNotExist:
            return Response(status= status.HTTP_404_NOT_FOUND)
        

    def patch(self, request,*args, **kwargs):
        id=self.kwargs.get("pk")
        try:
            emp = Employee.objects.get(id=id)
            empserializer = EmployeeSerializers(emp, data=request.data, partial=True)
            if empserializer.is_valid():
                empserializer.save()
                return Response(empserializer.data, status=status.HTTP_200_OK)
            return Response(empserializer.errors, status= status.HTTP_400_BAD_REQUEST)
        except Employee.DoesNotExist:
            return Response(status= status.HTTP_404_NOT_FOUND)

    def delete(self,request, *args, **kwargs):
        id=self.kwargs.get("pk")
        try:
            emp =Employee.objects.get(pk=id)
            emp.delete()
            return Response(status= status.HTTP_204_NO_CONTENT)   
        except Employee.DoesNotExist:
            return Response(status= status.HTTP_400_BAD_REQUEST)
        
        




