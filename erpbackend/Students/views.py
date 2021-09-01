from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Student
from rest_framework.viewsets import ModelViewSet
from .serializers import StudentSerializer


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


"""def index(request):
    #return HttpResponse("hello world")
    stdlist = Student.objects.all()
    students = []
    return JsonResponse(students,safe=False)"""
