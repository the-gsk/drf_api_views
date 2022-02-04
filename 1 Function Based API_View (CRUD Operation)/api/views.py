from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Student
from api.seriallizers import StudentSerializer
from rest_framework import status
# Create your views here.

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def student_api(request,pk=None):
    if request.method =='GET':
        if pk is not None:
            stu = Student.objects.get(id=pk)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu,many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)    
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created'},status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        stu = Student.objects.get(id=pk)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'complete data updated'}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.error_messages, status=status.HTTP_304_NOT_MODIFIED)

    if request.method == 'PATCH':
        stu = Student.objects.get(id=pk)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial data updated'}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        stu = Student.objects.get(id=pk)
        stu.delete()
        return Response({'msg':'Data Deleted'}, status=status.HTTP_202_ACCEPTED)
