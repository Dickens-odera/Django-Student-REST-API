from django.shortcuts import render, redirect
from rest_framework.generics import ListAPIView, RetrieveAPIView
from student.models import Student
from student.serializers import StudentSerializer
from student.forms import StudentForm

#import the permission policies
from rest_framework.permissions import (
    AllowAny,
    IsAdminUser,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly
)
#from student.permissions import UserPermission
# Create your views here.
"""
A class to list all the stdudents from our database (API)
"""
class ListStudent(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    #permission_classes = [IsAuthenticated, UserPermission]
"""
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
"""

"""
A class to list only the requested student from the database by id (API)
"""
class RetrieveStudent(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'pk'
    #permission_classes = IsAuthenticated


def StudentFormHelper(request):
    students = Student.objects.all().filter()[:5]
    form = StudentForm(request.POST or None)
    template = 'index.html'
    context = {'form': form, 'students':students}
    if form.is_valid():
        form.save()
        return redirect('list_students')

    return render(request, template, context)
        

def updateStudent(request, id):
    template = 'index.html'
    students_details = Student.objects.get(id = id)
    form = StudentForm(request.POST or None, instance= students_details)
    context = {'form': form, 'students_details':students_details}
    if form.is_valid():
        form.save()
        return redirect('list')
    return render(request, template, context)
    