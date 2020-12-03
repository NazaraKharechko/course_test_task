from django.shortcuts import render, redirect
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin
from .models import CourseModel
from .serializers import Courses_Serializers


def all_courses(request):
    courses = CourseModel.objects.all()
    return render(request, 'all_courses.html', {'courses': courses})


class CreateVieAll(ListModelMixin, CreateAPIView):
    serializer_class = Courses_Serializers
    queryset = CourseModel.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class Find_Date_Beginnings_VieData(ListModelMixin, CreateAPIView):
    serializer_class = Courses_Serializers

    def get_queryset(self, ):
        params = self.request.query_params
        date_beginnings = params.get('date_beginnings', None)

        if not date_beginnings:
            return CourseModel.objects.all()
        return CourseModel.objects.filter(date_beginnings=date_beginnings)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class Find_Name_VieData(ListModelMixin, CreateAPIView):
    serializer_class = Courses_Serializers

    def get_queryset(self, ):
        params = self.request.query_params

        name = params.get('name', None)
        if not name:
            print(name)
            return CourseModel.objects.all()
        return print(CourseModel.objects.filter(name=name))

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class DeteilView(RetrieveUpdateDestroyAPIView):
    serializer_class = Courses_Serializers
    queryset = CourseModel.objects.all()
