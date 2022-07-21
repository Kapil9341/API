from django.shortcuts import render

# Create your views here.
from .models import Student
from .serializers import StudentSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer

from .serializers import serializers


def student_detail(request,pk):
    stu = Student.objects.get(id=pk)
    serializer = StudentSerializer(stu)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type = 'application/json')

def student_list(request):
    stu = Student.objects.all()
    serializers  = StudentSerializer(stu, many=True)
    json_data = JSONRenderer().render(serializers.data)
    # print(json_data)
    return HttpResponse(json_data,content_type = 'application/json')